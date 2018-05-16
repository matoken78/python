# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
# 確認にはtailコマンドを用いよ．

import codecs
import itertools
import sys

encode = "utf-8"

def last(file_path, n):
    line_count = count("./hightemp.txt")
    with codecs.open(file_path, "r", encode) as f:
        for line in itertools.islice(f, line_count - n, None):
            print(line, end = "")

def count(file_path):
    return sum(1 for line in codecs.open(file_path, "r", encode))

last("./hightemp.txt", int(sys.argv[1]))

# $ tail -n 4 ./hightemp.txt