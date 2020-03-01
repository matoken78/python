import re
from collections import Counter
import MeCab
import itertools
from igraph import *

# igraph利用のため
# https://qiita.com/link_to_someone/items/4a8de1824287d3976031

minfreq = 4                     # グラフ描画のときは4に設定し見やすくする
m = MeCab.Tagger('-Ochasen')    # MeCabで品詞分解する


def print_data(label, data):
    can_print = True
    if not can_print:
        return
    print('\n*** ', label)
    print(data)


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
print_data('Restricted Count', restrictedcnt)
charedges = restrictedcnt.keys()
vertices = list(set([v[0] for v in charedges] + [v[1] for v in charedges]))
print_data('Vertices', vertices)

# charedgesは(['名詞','名詞'])の形なのでvertid(数字)ペア([1,3])に変換する
edges = [(vertices.index(u[0]), vertices.index(u[1])) for u in charedges]
print_data('edges', edges)

g = Graph(vertex_attrs={'label': vertices, 'name': vertices},
          edges=edges, directed=False)

# クリーク
#  - グラフ内部で密度が1、つまり張ることのできるすべての辺の数に対する
#    実際に張られている辺の数の比率が1であるような部分グラフ
#  - つながりが多くかたまりをなしている単語集団

# これ以上頂点を追加できないクリーク
print_data('Maximal cliques',
           [[vertices[v]
             for v in u] for u in list(g.maximal_cliques())])
# その中で大きさ（頂点の数）が最大のクリーク
print_data('Largest cliques',
           [[vertices[v]
             for v in u] for u in list(g.largest_cliques())])

# コミュニティ
#  - より実用的なグループ分け
#  - 辺の媒介中心性（edge betweenness）を指標にしてグループ分けする方法
#  - 頂点の媒介中心性での考え方と同様に、ある辺が頂点間の最短経路上にある程度のこと
print_data('Community', g.community_edge_betweenness())
plot(g.community_edge_betweenness(), bbox=(800, 1000))

#   - Community info map
print_data('Community info map', g.community_infomap())
plot(g.community_infomap(), vertex_size=30, bbox=(800, 800))
