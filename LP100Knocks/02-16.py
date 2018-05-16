# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

import codecs
import itertools
import sys

def last(file_path, n):
    line_count = count("./hightemp.txt")
    with codecs.open(file_path, "r", "utf-8") as f:
        for line in itertools.islice(f, line_count - n, None):
            print(line, end = "")

def count(file_path):
    return sum(1 for line in codecs.open(file_path, "r", "utf-8"))

last("./hightemp.txt", int(sys.argv[1]))