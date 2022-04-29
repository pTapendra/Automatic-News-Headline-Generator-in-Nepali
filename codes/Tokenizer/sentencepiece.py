
import sentencepiece as spm

spm.SentencePieceTrainer.train('--input=test.txt --model_prefix=token --vocab_size=2000')

sp = spm.SentencePieceProcessor()
sp.load('token.model')

sp.encode_as_pieces('कारणले सुनुवाइ नगरी फिर्ता गरेको भन्ने अधिकार कानुनमा हुने कि नहुने?')