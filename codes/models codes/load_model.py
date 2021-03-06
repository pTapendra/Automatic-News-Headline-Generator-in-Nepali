# -*- coding: utf-8 -*-
"""savedModelLoadingCode.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TGz78_i0hO5VAL5V-BIDHcHDJJbsogUj
"""

import tensorflow as tf
import numpy as np
import sentencepiece as spm

model = tf.keras.models.load_model('/path-to-saved-models', compile=False)

sp = spm.SentencePieceProcessor()
sp.load('./path-to-model/m_bpe.model')

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
    # return summary_tokenizer.sequences_to_texts(summarized)[0]  # since there is just one translated document

s1 = summarize(
    "स्थानीय तह निर्वाचन आउन १४ दिन मात्रै बाँकी छ । ७ सय ५३ स्थानीय तहले जेठ ६ देखि नयाँ जनप्रतिनिधि पाउनेछन् । उम्मेदवारी मनोनयन दर्ता भएसँगै मुलुक निर्वाचनमय भएको छ । निर्वाचनलाई व्यवस्थित बनाउन निर्वाचन आयोगले भरपर्दो व्यवस्था गरेको जनाए पनि आचारसंहिता उल्लंघनको घटना बढ्न सक्ने आशंका गरेको छ । निर्वाचन तयारीलगायतको विषयमा प्रमुख निर्वाचन आयुक्त दिनेशकुमार थपलियासँग कान्तिपुरका दुर्गा खनाल र मकर श्रेष्ठले गरेको कुराकानी"
)

summary = list(s1[0])
final_summary = [int(x) for x in summary]

sp.Decode(final_summary)