from collections import Counter
import numpy as np
from numpy.random import *
import nltk
from nltk.corpus.reader.chasen import *

def gen_next(words, dic):
    grams = len(words)
    if grams == 2:
        # 2-gramの第2項が欲しい語words[1]であるものを集める
        matched_items = np.array(list(filter((lambda x: x[0][0] == words[1]),
                                    dic.items())))
    else:
        # 3-gramの第2・3項が欲しい語words[1], words[2]であるものを集める
        matched_items = np.array(list(filter((lambda x: x[0][0] == words[1]) and
                                             (lambda x: x[0][1] == words[2]),
                                    dic.items())))
    
    if len(matched_items) == 0:
        print('No matched generator for ', words[1])
        return ''
    
    # N-gram辞書の出現回数部分を取り出す
    probs = [row[1] for row in matched_items]
    # 乱数rand(項数)を要素毎にかける
    weight_list = rand(len(matched_items)) * probs

    # 重み最大になるN-gramのN語目を取り出す
    return matched_items[np.argmax(weight_list)][0][grams - 1]

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

for grams in range(2, 4):
    print('')
    print('***** ' + str(grams) + 'grams')
    for count in range(10):
        words = ['', '子規'] if grams == 2 else ['', '子規', 'の']
        output = words[1:]
        for i in range(50):
            newword = gen_next(words, dic2) if grams == 2 \
                else gen_next(words, dic3)
            output.append(newword)
            if newword in ['', '。', '？', '！', '?', '!']:
                break
            words = output[-len(words):]
        for u in output:
            print(u, end='')
        print()