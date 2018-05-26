import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt
import random

xlist = []
for _ in range(30):
    # random の方法もいくつかあるんだね。
    # random.seed(25) とかで seed を固定化することもできる。
    xlist.append([random.randrange(200), random.randint(20, 300)])
x = np.array(xlist)
z = linkage(x, 'single')
dendrogram(z)

plt.title('Hierarchical Clustering(Tree)')
plt.ylabel('Distance')
plt.show()

# Original
# x = np.array([[1, 2], [2, 1], [3, 4], [4, 3]])
# z = linkage(x, 'single')
# dendrogram(z, labels=['a', 'b', 'c', 'd'])

# plt.title('Hierarchical Clustering(Tree)')
# plt.ylabel('Distance')
# plt.show()
