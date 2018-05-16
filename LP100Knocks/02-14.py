# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
# 確認にはheadコマンドを用いよ．

import codecs
import itertools
import sys

encode = "utf-8"

def top(file_path, n):
    with codecs.open(file_path, "r", encode) as f:
        for line in itertools.islice(f, n):
            print(line, end = "")

top("./hightemp.txt", int(sys.argv[1]))

# $ head -n 4 ./hightemp.txt