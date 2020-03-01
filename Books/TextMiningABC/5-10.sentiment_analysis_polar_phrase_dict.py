# download from the following dictionary
# http://www.lr.pi.titech.ac.jp/~takamura/pndic_ja.html

from pprint import pprint
import re
from statistics import mean
import MeCab
from aozora import Aozora

pndicfname = './sentiment/pn_ja.dic'
aozora = Aozora('./wagahaiwa_nekodearu.txt')


def read_pndic(filename):
    with open(filename, 'r') as dicfile:
        items = dicfile.read().splitlines()
    return {u.split(':')[0]: float(u.split(':')[3]) for u in items}


pndic = read_pndic(pndicfname)

# 文に分解する
text = '\n'.join(aozora.read())
text = re.sub(' ', '', text)
sentences = re.split('。(?!」)|\n', text)
# 空行を除く
while '' in sentences:
    sentences.remove('')
print('\n***** Sentences')
pprint(sentences)

# MeCabで品詞分解する
m = MeCab.Tagger('-Ochasen')

# 文単位で形態素解析し、名詞だけ抽出し、基本形を文ごとにリストにする
sentence_word_list = [
    [v.split()[2] for v in m.parse(sentence).splitlines()
        if (len(v.split()) >= 3 and v.split()[3][:2]
            in ['名詞', '形容', '動詞', '副詞'])]
    for sentence in sentences
]

# 文3から文8までの単語リストに対して
# それぞれの単語について感情極性値の辞書を引いて出力する
print('\n***** Sentiment value for each word for each sentence')
for sentence in sentence_word_list[3:9]:
    for v in sentence:
        print(v, pndic.get(v))

# それぞれの文の感情極性値を計算する
print('\n***** Sentiment value for each sentence')
for sentence in sentence_word_list[3:9]:
    value_list = [pndic.get(v) for v in sentence if pndic.get(v)]
    if value_list == []:
        print(sentence, 'None')
        continue
    mean_value = mean(value_list)
    print(sentence, mean_value)
