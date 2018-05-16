# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
# 確認にはcut, uniq, sortコマンドを用いよ．

# Counter: https://docs.python.jp/3/library/collections.html#collections.Counter

import codecs
from collections import Counter

encode = "utf-8"

def count_items(col_number):
    counts = Counter(line.split("\t")[0] for line in codecs.open(".\hightemp.txt", "r", encode))
    print(counts.most_common())

count_items(0)

# cut -f 1 hightemp.txt | sort | uniq -c | sort -r