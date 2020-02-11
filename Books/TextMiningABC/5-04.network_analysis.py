import re
import numpy as np
from collections import Counter
import MeCab
import itertools
from jgraph import *

minfreq = 0                     # グラフ描画のときは4に設定し見やすくする
m = MeCab.Tagger('-Ochasen')    # MeCabで品詞分解する

def readin(filename):
    with open(filename, mode='r', encoding='utf-8') as afile:
        whole_str = afile.read()
    sentences = (re.sub('。', '。\n', whole_str)).splitlines()
    return [re.sub(' ', '', u) for u in sentences if len(u) != 0]

filename = 'abe_enzetsu_20170120.txt'
string = readin(filename)

# 文単位で形態素解析し、名詞だけ抽出し、基本形を文ごとのリストにする
sentence_meishi_list = [
    [v.split()[2] for v in m.parse(sentence).splitlines()
        if (len(v.split()) >= 3 and v.split()[3][:2] == '名詞')]
            for sentence in string]

# 文ごとにペアリストを作る
doubletslist = [
    list(itertools.combinations(meishi_list, 2))
        for meishi_list in sentence_meishi_list
        if len(meishi_list) >= 2
]
# 文ごとのペアリストをフラットなリストにする
alldoublets = []
for u in doubletslist:
    alldoublets.extend(u)

# 名詞ペアの頻度を数える
dcnt = Counter(alldoublets)

# 出現頻度順にソートした共起ペアを出力する（上位ペア30）
print('pair frequency',
    sorted(dcnt.items(), key=lambda x: x[1], reverse=True)[:30])

# 名詞ペアの頻度辞書から、頻度が4以上のエントリだけを抜き出した辞書を作る
restrictedcnt = dict(((k, dcnt[k]) for k in dcnt.keys() if dcnt[k] >= minfreq))
charedges = restrictedcnt.keys()
vertices = list(set([v[0] for v in charedges] + [v[1] for v in charedges]))

# charedgesは(['名詞','名詞'])の形なのでvertid(数字)ペア([1,3])に変換する
edges = [(vertices.index(u[0]), vertices.index(u[1])) for u in charedges]

g = Graph(vertex_attrs={'label': vertices, 'name': vertices},
        edges=edges, directed=False)
plot(g, vertex_size=30, bbox=(800, 800), vertex_color='white')