#!/usr/bin/env python
# coding: utf-8

import tensorflow_datasets as tfds
import tensorflow as tf

import time
import numpy as np

model = tf.keras.models.load_model('./Model.16H.800AVG.100K.100ITER', compile=False)

examples, metadata = tfds.load('nepali_nlp/dataset', with_info=True, as_supervised=True)
train_examples, val_examples = examples['train'], examples['test']

import sentencepiece as spm

document_id = [x.numpy().decode('utf-8') for x, y in val_examples]
summary_id = [y.numpy().decode('utf-8') for x, y in val_examples]

sp = spm.SentencePieceProcessor()
sp.load('m_bpe.model')

decoder_maxlen = 35
encoder_maxlen = 200

def evaluate(input_document):
    input_document = sp.encode_as_ids(input_document)
    input_document = tf.keras.preprocessing.sequence.pad_sequences([input_document], maxlen=encoder_maxlen, padding='post', truncating='post')

    encoder_input = tf.expand_dims(input_document[0], 0)

    decoder_input = sp.encode_as_ids("this")
    output = tf.expand_dims(decoder_input, 0)
    
    for i in range(decoder_maxlen):
        predictions, attention_weights = model(
            encoder_input, 
            output
        )

        predictions = predictions[: ,-1:, :]
        predicted_id = tf.cast(tf.argmax(predictions, axis=-1), tf.int32)

        if predicted_id == sp.encode_as_ids("wom"):
          return tf.squeeze(output, axis=0), attention_weights

        output = tf.concat([output, predicted_id], axis=-1)

    return tf.squeeze(output, axis=0), attention_weights

def summarize(input_document):
    # not considering attention weights for now, can be used to plot attention heatmaps in the future
    summarized = evaluate(input_document=input_document)[0].numpy()
    summarized = np.expand_dims(summarized[1:], 0)  # not printing this token
    return summarized

def final_summary(input):
    s1 = summarize(input)
    summary = list(s1[0])
    final_summary = [int(x) for x in summary]
    return sp.Decode(final_summary)

short_document_id = document_id[:100]

predicted = [final_summary(x) for x in short_document_id]

from rouge import Rouge

def rouge_score_calc(hyp, ref):
    metric = Rouge()
    
    results_r1 = {'precision': [], 'recall': [], 'fmeasure': []}
    results_r2 = {'precision': [], 'recall': [], 'fmeasure': []}
    results_rL = {'precision': [], 'recall': [], 'fmeasure': []}
    count = 0
    for (h, r) in zip(hyp, ref):
        if h:
            count = count + 1
            score = metric.get_scores(h, r)

            results_r1['precision'].append(score[0]['rouge-1']['p'])
            results_r1['recall'].append(score[0]['rouge-1']['r'])
            results_r1['fmeasure'].append(score[0]['rouge-1']['f'])

            results_r2['precision'].append(score[0]['rouge-2']['p'])
            results_r2['recall'].append(score[0]['rouge-2']['r'])
            results_r2['fmeasure'].append(score[0]['rouge-2']['f'])

            results_rL['precision'].append(score[0]['rouge-l']['p'])
            results_rL['recall'].append(score[0]['rouge-l']['r'])
            results_rL['fmeasure'].append(score[0]['rouge-l']['f'])
        
    return results_r1, results_r2, results_rL

reference = summary_id[:100]

rouge_score_calc(predicted, reference)

count = 0
final_measure = 0
fmeasure = results_r2['fmeasure']
l = list()
for i in range(0, 99):
    final_measure = final_measure + fmeasure[i]
    l.append(i)

final_measure / 99