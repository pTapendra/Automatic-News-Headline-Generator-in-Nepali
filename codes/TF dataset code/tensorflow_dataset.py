import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_datasets as tfds

df = pd.read_csv("total.csv",encoding='utf-8',quotechar="'",quoting=1, delimiter=",")
df = df.dropna()
df = df.reset_index(drop=True)

document = df['News']
summary = df['Title']

document_lengths = pd.Series([len(x) for x in document])
summary_lengths = pd.Series([len(x) for x in summary])

def _bytes_feature(value):
  """Returns a bytes_list from a string / byte."""
  if isinstance(value, type(tf.constant(0))):
    value = value.numpy() # BytesList won't unpack a string from an EagerTensor.
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

total_size = len(df)
train_size = 112310
test_size = total_size - train_size


df_train = df[:train_size]
df_test = df[train_size:]
df_train = df_train.sample(frac=1).reset_index(drop=True)

document_train = df_train['News']
summary_train = df_train['Title']

df_test = df_test.sample(frac=1).reset_index(drop=True)

document_test = df_test['News']
summary_test = df_test['Title']

document_train = document_train.tolist()
summary_train = summary_train.tolist()

document_test = document_test.tolist()
summary_test = summary_test.tolist()

document_train = [x.encode('utf-8') for x in document_train]
summary_train = [x.encode('utf-8') for x in summary_train]

document_test = [x.encode('utf-8') for x in document_test]
summary_test = [x.encode('utf-8') for x in summary_test]

document_train = np.array(document_train, dtype=np.bytes_)
summary_train = np.array(summary_train, dtype=np.bytes_)

document_test = np.array(document_test, dtype=np.bytes_)
summary_test = np.array(summary_test, dtype=np.bytes_)

def serialize_example(document, summary):
    feature = {
        'document' : _bytes_feature(document),
        'summary' : _bytes_feature(summary),
    }
    
    example_proto = tf.train.Example(features=tf.train.Features(feature=feature))
    return example_proto.SerializeToString()

dataset_train = tf.data.Dataset.from_tensor_slices((document_train, summary_train))
dataset_test = tf.data.Dataset.from_tensor_slices((document_test, summary_test))

def tf_serialize_example(document, summary):
    tf_string = tf.py_function(serialize_example, 
                              (document, summary),
                               tf.string)
    return tf.reshape(tf_string, ())

serialized_dataset_train = dataset_train.map(tf_serialize_example)
serialized_dataset_test = dataset_test.map(tf_serialize_example)

import os
cwd = os.getcwd()

filename = cwd + '\\nepali_nlp\\dataset\\1.0.0\\summary-train.tfrecord-00000-of-00001'
writer = tf.data.experimental.TFRecordWriter(filename)
writer.write(serialized_dataset_train)
writer.close()

# filename = cwd + '\\nepali_nlp\\dataset\\1.0.0\\summary-test.tfrecord-00000-of-00001'
# writer = tf.data.experimental.TFRecordWriter(filename)
# writer.write(serialized_dataset_test)

# filename1 = cwd + '\\nepali_nlp\\dataset\\1.0.0\\summary-train.tfrecord-00000-of-00001'
# writer1 = tf.data.experimental.TFRecordWriter(filename1)
# writer1.write(serialized_dataset_train)

features = tfds.features.FeaturesDict({
    'document': tfds.features.Text(),
    'summary': tfds.features.Text()
})

split_infos = [
    tfds.core.SplitInfo(
        name='train',
        shard_lengths=[train_size],  # Num of examples in shard0, shard1,...
        num_bytes=0,  # Total size of your dataset (if unknown, set to 0)
    ),
    tfds.core.SplitInfo(
        name='test',
        shard_lengths=[test_size],
        num_bytes=0,
    ),
]

tfds.folder_dataset.write_metadata(
    data_dir=cwd + '\\nepali_nlp\\dataset\\1.0.0\\',
    features=features,
    # Pass the `out_dir` argument of compute_split_info (see section above)
    # You can also explicitly pass a list of `tfds.core.SplitInfo`
    split_infos=split_infos,

    # Optionally, additional DatasetInfo metadata can be provided
    # See:
    # https://www.tensorflow.org/datasets/api_docs/python/tfds/core/DatasetInfo
    description="""This is dataset for minor project""",
    homepage='http://my-project.org',
    supervised_keys=('document', 'summary'),
    citation="""BibTex citation.""",
)


# Loading code
path = 'nepali_nlp/dataset'
examples, metadata = tfds.load(path, with_info=True,
                               as_supervised=True)
train_examples, val_examples = examples['train'], examples['test']