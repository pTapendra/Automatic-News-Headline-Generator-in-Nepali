import tensorflow_datasets as tfds
import tensorflow as tf

import time
import numpy as np
import matplotlib.pyplot as plt

from tensorflow_text.tools.wordpiece_vocab import bert_vocab_from_dataset as bert_vocab
import tensorflow_text as text

examples, metadata = tfds.load('nepali_nlp/summarizer_dataset', with_info=True,
                               as_supervised=True)
train_examples, val_examples = examples['train'], examples['test']

train_en = train_examples.map(lambda pt, en: en)


bert_tokenizer_params = dict(lower_case=True)
reserved_tokens=["[PAD]", "[UNK]", "[START]", "[END]"]

bert_vocab_args = dict(
    # The target vocabulary size
    vocab_size = 60000,
    # Reserved tokens that must be included in the vocabulary
    reserved_tokens=reserved_tokens,
    # Arguments for `text.BertTokenizer`
    bert_tokenizer_params=bert_tokenizer_params,
    # Arguments for `wordpiece_vocab.wordpiece_tokenizer_learner_lib.learn`
    learn_params={},
)

en_vocab = bert_vocab.bert_vocab_from_dataset(train_en.batch(1000).prefetch(2), **bert_vocab_args)

def write_vocab_file(filepath, vocab):
  with open(filepath, 'w', encoding='utf-8') as f:
    for token in vocab:
      print(token, file=f)

write_vocab_file('en_vocab.txt', en_vocab)

en_tokenizer = text.BertTokenizer('en_vocab.txt', **bert_tokenizer_params)

for pt_examples, en_examples in train_examples.batch(3).take(1):
  for ex in en_examples:
    print(ex.numpy())

token_batch = en_tokenizer.tokenize(en_examples)


a = ["कारणले सुनुवाइ नगरी फिर्ता गरेको भन्ने अधिकार कानुनमा हुने कि नहुने?"]

c = en_tokenizer.tokenize(a)
en_tokenizer.detokenize(c)