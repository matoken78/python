from collections import Counter
import re
import numpy as np
import matplotlib.pyplot as plt
from aozora import Aozora
import MeCab

aozora = Aozora('wagahaiwa_nekodearu.txt')

# 入力テキストを文に分解する。単純に'。'で分割する
string = '\n'.join(aozora.read())
string = re.split('。(?!」)|\n', re.sub(' ', '', string))
while '' in string:
    string.remove('')                         # 空行を除く

# 文ごとに形態素解析して、文あたりの語の出現頻度を数える
m = MeCab.Tagger('-Ochasen')                # MeCab で単語に分割する
wordcountlist = []
for sentence in string:
    mecablist = []
    wlist = m.parse(sentence).splitlines()    # 結果を単語情報リストに整形する
    for u in wlist:
        mecablist.append([v for v in u.split()])
    # 得られた単語情報リストから、単語の部分だけを取り出したリストを作る
    wordbodylist = [u[0] for u in mecablist]
    # 単語数のリストを作る
    wordcountlist.append(len(wordbodylist))

cnt = Counter(wordcountlist)
# 結果をカウント数の降順にソート
print(sorted(cnt.items(), key=lambda x: x[1], reverse=True)[:100])
u = np.array(wordcountlist)
nstring = u[ np.where(u < 150) ]
plt.hist(nstring, bins=nstring.max())
plt.title('『吾輩は猫である』文ごとの単語数分布')
plt.xlabel('文の単語数')
plt.ylabel('出現頻度')
plt.show()