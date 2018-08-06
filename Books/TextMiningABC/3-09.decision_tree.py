# 事前に下記をダウンロードしてインストールしておくこと
# graphviz: http://www.graphviz.org/download/

# graphviz.py を下記のように変更した
# def find_graphviz():
#    return __find_executables("C:\\Program Files (x86)\\Graphviz2.38\\bin")

from sklearn.datasets import load_iris
from sklearn import tree

# 学生番号, 40歳以上か, 男性か, 70点以上か
table = [
    [ 1, False, True,  True],
    [ 2, False, False, True],
    [ 3, False, True,  True],
    [ 4, False, True,  True],
    [ 5, True,  True,  True],
    [ 6, False, True,  False],
    [ 7, True,  False, False],
    [ 8, True,  False, False],
    [ 9, True,  True,  False],
    [10, True,  False, False]]

data = [u[1:3] for u in table]      # 説明変数(年齢、性別)を抽出
target = [u[3] for u in table]      # 目的変数(点数)を抽出
clf = tree.DecisionTreeClassifier() # インスタンスを作成
clf = clf.fit(data, target)         # データで学習
for i in range(len(data)):          # 元データを分類(予想)してみる
    # 予測値と予測した確率
    print(i + 1, clf.predict([data[i]]), clf.predict_proba([data[i]]))

import pydotplus                    # グラフ化するためのパッケージを読み込む
# clf を graphviz のデータとして出力
dot_data = tree.export_graphviz(clf, out_file=None)
graph = pydotplus.graph_from_dot_data(dot_data) # グラフを pdf ファイルに変換
graph.write_pdf('3-09.gakusei-DecisionTree.pdf')
