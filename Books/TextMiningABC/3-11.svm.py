import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets

iris = datasets.load_iris()
x = iris.data[:, :2]    # iris データのうち花弁の長さと花弁の幅のみ使うことにする
y = iris.target

h = .02 # メッシュのステップサイズ
c = 1.0 # SVM のコストパラメータ（大きいほど誤分類を許さない）
svc = svm.SVC(kernel='linear', C=c).fit(x, y)                       # SVC クラスで linear を選択
rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=c).fit(x, y)           # SVC クラスで rbf(ラジアル基底関数)を選択
poly_svc = svm.SVC(kernel='poly', degree=3, C=c).fit(x, y)          # SVC クラスで poly(多項式:3次)を選択
poly4_svc = svm.SVC(kernel='poly', degree=4, C=c).fit(x, y)         # SVC クラスで poly(多項式:4次)を選択
sigmoid_svc = svm.SVC(kernel='sigmoid', gamma=0.01, C=c).fit(x, y)   # SVC クラスで sigmoid を選択
lin_svc = svm.LinearSVC(C=c).fit(x, y)                              # linearSVC クラス

x_min, x_max = x[:, 0].min() - 1, x[:, 0].max() + 1
y_min, y_max = x[:, 1].min() - 1, x[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

titles = ['SVC:linear', 'LinearSVC', 'SVC:rbf',
          'SVC:3poly', 'SVC:4poly', 'SVC:sigmoid']

for i, clf in enumerate((svc, lin_svc, rbf_svc, poly_svc, poly4_svc, sigmoid_svc)):
    plt.subplot(2, 3, i + 1)
    plt.subplots_adjust(wspace=0.4, hspace=0.4)

    z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    z = z.reshape(xx.shape)

    # 区分ごとの色分けを等高線で描画
    plt.contourf(xx, yy, z, cmap=plt.cm.coolwarm, alpha=0.8)

    # 教師データを重ねてプロット
    plt.scatter(x[:, 0], x[:, 1], c=y, cmap=plt.cm.coolwarm, marker='.')
    plt.xlabel('花弁の長さ')
    plt.ylabel('花弁の幅')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title(titles[i])

plt.show()