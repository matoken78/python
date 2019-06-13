import matplotlib.pyplot as plt
import numpy as np
import nltk
from nltk.corpus import inaugural
from collections import Counter
text = inaugural.raw('1789-Washington.txt')
sents = nltk.tokenize.sent_tokenize(text)
# sents の文ごとの文字数のリストを作り、Counterで頻度を数える
cnt = Counter(len(x) for x in sents)
# 長さと頻度の降順にソートして表示（頻度は全て1なので実質長さでソート）
print('ワシントン大統領就任演説 長さ×頻度')
print(sorted(cnt.items(), key=lambda x: [x[1], x[0]], reverse=True))

import utils
utils.adapt_japanese_font(plt)

# ヒストグラムの表示
nstring = np.array([len(x) for x in sents])
plt.hist(nstring)
plt.title('1789年ワシントン大統領就任演説の文ごとの文字数分布')
plt.xlabel('文の文字数')
plt.ylabel('出現頻度')
plt.show()

import re
from aozora import Aozora

aozora = Aozora('wagahaiwa_nekodearu.txt')

# 文に分解してから、文ごとに文字数をカウントする
string = '\n'.join(aozora.read())
# 全角空白を取り除く。句点・改行で分割、。」の。は改行しない
string = re.split('。(?!」)|\n', re.sub('　', '', string))
# 空行を除く
while '' in string:
    string.remove('')
# string の要素（文）の長さをリストにする
cnt = Counter([len(x) for x in string])
# 文の長さを頻度順にソートして出力する
print('吾輩は猫である 長さ×頻度')
print(sorted(cnt.items(), key=lambda x: x[1], reverse=True)[:100])
nstring = np.array([len(x) for x in string if len(x) < 150])
print('max', nstring.max())
plt.hist(nstring, bins=nstring.max())
plt.title('「吾輩は猫である」文ごとの文字数分布')
plt.xlabel('文の文字数')
plt.ylabel('出現頻度')
plt.show()