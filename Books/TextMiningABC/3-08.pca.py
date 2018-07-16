import math
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt

colors = ['red', 'blue', 'green']
markers = ['x', '.', '+']

# Prepare data
iris = load_iris()
species = ['Setosa', 'Versicolour', 'Virginica']

# Extract data of the base
irisdata = pd.DataFrame(iris.data, columns=iris.feature_names)
# Extract data of the kind
iristarget = pd.DataFrame(iris.target, columns=['target'])
# Join data
irispd = pd.concat([irisdata, iristarget], axis=1) # axis=1 means horizontal join

num_components = 4
pca = PCA(n_components=num_components)
pca.fit(irisdata)   # Analyze data

# Show result
print('主成分', pca.components_)
print('平均', pca.mean_)
print('分散', pca.explained_variance_)
print('寄与率', pca.explained_variance_ratio_)
print('累積寄与率', np.cumsum(pca.explained_variance_ratio_))

# Plot data transformed principal component
num_rows = math.ceil(num_components / 2)
fig, axes = plt.subplots(nrows=num_rows, ncols=2)

for i in range(len(species)):
    trans = pca.transform(irisdata[irispd.target == i])
    for j in range(num_components - 1):
        row = int(j / 2)
        col = j % 2
        axes[row, col].scatter([u[0] for u in trans], \
                               [u[j + 1] for u in trans], \
                               c=colors[i], \
                               label=species[i], \
                               marker=markers[i])
        axes[row, col].set_xlabel('pc1')
        axes[row, col].set_ylabel('pc' + str(j + 2))
axes[1, 1].axis('off')
plt.legend()
plt.show()

# Original is the followings
# # Plot data transformed principal component
# for i in range(3):
#     trans = pca.transform(irisdata[irispd.target == i])
#     plt.scatter([u[0] for u in trans], \
#                 [u[1] for u in trans], \
#                 c=colors[i], \
#                 label=species[i], \
#                 marker=markers[i])

# plt.title('PCA for iris data')
# plt.xlabel('pc1')
# plt.ylabel('pc2')
# plt.legend()
# plt.show()

