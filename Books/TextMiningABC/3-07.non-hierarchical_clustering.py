# 階層型はグループがわからないときには便利。ただし点の数が多くなると計算量が増える。
# 非階層型は計算量がそれほど増えない。ただし、グループ数を決めておかないといけない。グループ中心の初期値も決めないといけない。
# ・グループ数
# 　・いろいろなグループ数で試してクラスタ内誤差の平方和で比較する（エルボー法）
# 　・グループ内での凝集度や乖離度を使って比較する（シルエット分析）
# ・グループ中心の初期値
# 　・少なくとも不適切な初期中心を選ばないようにする（k-means++法）

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import pandas as pd

# skleran で用意されている iris データ
# http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html
# https://pythondatascience.plavox.info/scikit-learn/scikit-learn%E3%81%AB%E4%BB%98%E5%B1%9E%E3%81%97%E3%81%A6%E3%81%84%E3%82%8B%E3%83%87%E3%83%BC%E3%82%BF%E3%82%BB%E3%83%83%E3%83%88
# “setosa”, “versicolor”, “virginica” という 3 種類の品種のアヤメ
# sepal length (cm)	がく片の長さ
# sepal width (cm)	がく片の幅
# petal length (cm)	花弁の長さ
# petal width (cm)	花弁の幅
iris = load_iris()
species = ['Setosa', 'Versicolour', 'Virginica']
irispddata = pd.DataFrame(iris.data, columns=iris.feature_names)
# iris.data
#      sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
# 0                  5.1               3.5                1.4               0.2
# 1                  4.9               3.0                1.4               0.2
# 2                  4.7               3.2                1.3               0.2
#  ... (中略)
# 149                5.9               3.0                5.1               1.8
irispdtarget = pd.DataFrame(iris.target, columns=['target'])
# iris.target
# array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#        0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#        1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
#        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
#        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
#print(irispddata)
#print(irispdtarget)
# デフォルトで k-means++ になってる。
# k-means  : 最初のクラスタのランダムな割り振りに大きく依存するため、精度が良くない。
#            https://ja.wikipedia.org/wiki/K%E5%B9%B3%E5%9D%87%E6%B3%95
# k-means++: 初期のk個のクラスタ中心は離れている方が良いという考えに基づき、精度が良い。
#            https://ja.wikipedia.org/wiki/K-means%2B%2B%E6%B3%95
kmeans = KMeans(n_clusters=3).fit(irispddata)

# axis=1 で横方向の連結
irispd = pd.concat([irispddata, irispdtarget], axis=1)
#print(irispd)
iriskmeans = pd.concat([irispd, pd.DataFrame(kmeans.labels_, columns=['kmeans'])], axis=1)
#print(iriskmeans)

irispd0 = iriskmeans[iriskmeans.kmeans == 0]
irispd1 = iriskmeans[iriskmeans.kmeans == 1]
irispd2 = iriskmeans[iriskmeans.kmeans == 2]

dic = {}
# 25, 75, 125 は分類わけが必ず合っている前提
dic[ iriskmeans['kmeans'][25] ] = iriskmeans['target'][25]
dic[ iriskmeans['kmeans'][75] ] = iriskmeans['target'][75]
dic[ iriskmeans['kmeans'][125] ] = iriskmeans['target'][125]
d = np.array([dic[u] for u in iriskmeans['kmeans']])
irisdiff = iriskmeans[iriskmeans.target != d]
#print(irisdiff)

plt.scatter(irispd0['petal length (cm)'], irispd0['petal width (cm)'], c='red', label=species[dic[0]], marker='x')
plt.scatter(irispd1['petal length (cm)'], irispd1['petal width (cm)'], c='blue', label=species[dic[1]], marker='.')
plt.scatter(irispd2['petal length (cm)'], irispd2['petal width (cm)'], c='green', label=species[dic[2]], marker='+')
plt.scatter(irisdiff['petal length (cm)'], irisdiff['petal width (cm)'], c='black', label='missed', marker='^')
plt.title('iris scatter by kmeans')
plt.xlabel('petal length cm)')
plt.ylabel('petal width (cm)')
plt.legend()
plt.show()
