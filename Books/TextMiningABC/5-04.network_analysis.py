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
plot(g, vertex_size=30, bbox=(800, 800), vertex_color='white')

# 最短経路の平均経路長と経路長の分布
print_data('Average path length', g.average_path_length())
print_data('Path length hist', g.path_length_hist())

# 頂点の次数 = 頂点が持つ辺の数 = 他の語といかに共起しているか
degreelist = zip(vertices, g.degree())
print_data('Degree list',
           sorted(degreelist,
                  key=lambda x: x[1], reverse=True)[:30])
# 中心性
#  離心中心性 (Eccentricity centrality)
#   - 他の頂点との距離が小さい頂点ほど、より中心的である
#   - 友達がより近くに集まっている人ほど中心にいるイメージ
#   - 他の頂点との距離の最大値を取る決め方
#   - 「とにかくあるノードから他のノードへの距離の最大値を最小化したい」時に目安となる
#   - 全ノードで最短経路長が非ゼロでないと色々不都合の多い指標
#  近接中心性 (Closeness centrality)
#   - 他の頂点との距離が小さい頂点ほど、より中心的である
#   - 友達がより近くに集まっている人ほど中心にいるイメージ
#   - 他の頂点との距離の合計を用いる決め方
#   - 「とにかく距離の総和や平均距離を小さくしたい」時に目安となる
#   - 全ノードで最短経路長が非ゼロでないと色々不都合の多い指標
print_data('Eccentricity centrality',
           sorted(zip(vertices,
                      [1/u for u in list(g.eccentricity())]),
                  key=lambda x: x[1], reverse=True)[:30])
print_data('Closeness centrality',
           sorted(zip(vertices,
                      list(g.closeness())),
                  key=lambda x: x[1], reverse=True)[:30])

#  次数中心性 (Degree centrality)
#   - 頂点が持つ辺の数が最も多い頂点を中心とする考え方
print_data('Degree centrality',
           sorted(zip(vertices,
                      [u/len(g.degree()) - 1 for u in list(g.degree())]),
                  key=lambda x: x[1], reverse=True)[:30])

#  固有ベクトル中心性 (Eigenvalue-based centrality)
#   - 次数を利用し、隣接頂点の重要性も加味した中心性
#   - 人脈を広げるという観点から言えば「交友関係の広い友人を何人も持っている」ような人、
#     つまり他の次数中心性の高いノード「とつながっている」ノードを評価するような指標
print_data('Eigenvalue-based centrality',
           sorted(zip(vertices, list(g.evcent())),
                  key=lambda x: x[1], reverse=True)[:30])

#  PageRank
#   - 固有ベクトル中心性をさらに踏み込んで Web サイト間の重要性を算出するために
#     「リンク（流入）」を重視するようにした上で
#     さらに分離グラフや強連結でない有向グラフにも適用できるようにした
#   - Sergey BrinとLawrence "Larry" Pageの2人が考案してGoogle検索の基になった
print_data('PageRank',
           sorted(zip(vertices, list(g.pagerank())),
                  key=lambda x: x[1], reverse=True)[:30])
