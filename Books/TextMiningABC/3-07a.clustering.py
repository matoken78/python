# 説明  : https://pythondatascience.plavox.info/scikit-learn/%E3%82%AF%E3%83%A9%E3%82%B9%E3%82%BF%E5%88%86%E6%9E%90-k-means
# コード: http://archive.ics.uci.edu/ml/index.php

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

customer_df = pd.read_csv('http://pythondatascience.plavox.info/wp-content/uploads/2016/05/Wholesale_customers_data.csv')
#customer_df = pd.read_csv('3-07a.wholesale_customers_data.csv')

# 不要なカラムを削除
del(customer_df['Channel'])
del(customer_df['Region'])
#print(customer_df)

# Pandas のデータフレームから、Numpy の行列（Array）に変換
customer_array = np.array(
    [ customer_df['Fresh'].tolist(),
      customer_df['Milk'].tolist(),
      customer_df['Grocery'].tolist(),
      customer_df['Frozen'].tolist(),
      customer_df['Detergents_Paper'].tolist(),
      customer_df['Delicassen'].tolist()],
      np.int32)
#print(customer_array)

# 行列を転置
customer_array = customer_array.T

# クラスタ分析
# fit_predict() でクラスタ番号を付与
num_clusters = 4
pred = KMeans(n_clusters=num_clusters).fit_predict(customer_array)

# Pandas のデータフレームにクラスタ番号を追加
customer_df['cluster_id'] = pred

# 各クラスタに属するサンプル数の分布
customer_df['cluster_id'].value_counts()
# 各クラスタの各部門の購買額の平均値
for i in range(num_clusters):
    print('Cluster number: ' + str(i))
    print(customer_df[customer_df['cluster_id'] == i].mean())

cluster_info = pd.DataFrame()
for i in range(num_clusters):
    cluster_info['cluster' + str(i)] = customer_df[customer_df['cluster_id'] == i].mean()
cluster_info = cluster_info.drop('cluster_id')
#print(cluster_info)

# pandas の T は行列の入れ替え
my_plot = cluster_info.T.plot(kind='bar', stacked=True, title='Mean Value of 4 Clusters')
my_plot.set_xticklabels(my_plot.xaxis.get_majorticklabels(), rotation=0)
plt.show()