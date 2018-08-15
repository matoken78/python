# -*- coding: utf-8 -*-
from collections import Counter

# 英語
string_e = 'This is a pen.'
cnt = Counter(string_e)
print(string_e)
print(cnt)
print('Count of i: ' + str(cnt['i']) + '\n')

# 日本語
string_j = '吾輩は猫である。名前はまだ無い。'
cnt = Counter(string_j)
print(string_j)
print(cnt)
print('\n')

# 吾輩は猫である（夏目漱石＠青空文庫）
# https://www.aozora.gr.jp/cards/000148/card789.html#download
from aozora import Aozora
ao = Aozora('./wagahaiwa_nekodearu.txt')
string_waga = '\n'.join(ao.read())   # パラグラフをすべて結合して1つの文字列にする
cnt = Counter(string_waga)
# 頻度順（値）にソートして出力する
print(sorted(cnt.items(), key=lambda x: x[1], reverse=True)[:50])
print('\n')

# 英文の分割
# python -m nltk.downloader punkt で tokenizer をダウンロードする必要がある
# python -m nltk.downloader inaugural で inaugural コーパスをダウンロードする必要がある
#  (python -m nltk.downloader all なら全コーパスをダウンロードする)
import nltk
from nltk.corpus import inaugural
text = inaugural.raw('1789-Washington.txt')
sents = nltk.tokenize.sent_tokenize(text)
for u in sents:
    print('>>   ' + u + '<<')