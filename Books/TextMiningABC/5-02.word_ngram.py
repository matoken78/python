from collections import Counter
import numpy as np
from numpy.random import *
import nltk
from nltk.corpus.reader.chasen import *

# 下記から JEITA のコーパスをダウンロードできる
# http://masatohagiwara.net/files/jeita_aozora.tar.bz2
jeita = ChasenCorpusReader('./jeita_aozora', '1000.chasen', encoding='utf-8')
delimiter = ['「', '」', '…', ' ']
string = jeita.words()
doublets = list(zip(string[:-1], string[1:]))
doublets = filter(lambda x: not((x[0] in delimiter) or (x[1] in delimiter)), doublets)
triplets = list(zip(string[:-2], string[1:-1], string[2:]))
triplets = filter(lambda x: not((x[0] in delimiter) or \
                                (x[1] in delimiter) or \
                                (x[2] in delimiter)), triplets)

dic2 = Counter(doublets)    # 2-gramの出現回数リスト 
dic3 = Counter(triplets)    # 3-gramの出現回数リスト
for u, v in dic2.items():
    print(u, v)
for u, v in dic3.items():
    print(u, v)
