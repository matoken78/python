# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ．

import codecs
import sys

encode = "utf-8"

def my_split(file_path, n):
    line_count = count("./hightemp.txt")

    with codecs.open(file_path, "r", encode) as f1:
        for i, lines in enumerate(split_count(line_count, n)):
            with codecs.open(".\split{0}.txt".format(i + 1), "w", encode) as f2:
                for _ in range(lines):
                    f2.write(f1.readline())

def count(file_path):
    return sum(1 for line in codecs.open(file_path, "r", encode))

def split_count(line_count, split_count):
    div = line_count // split_count
    high_num = line_count % split_count

    return [div + 1] * high_num + [div] * (split_count - high_num)

my_split("./hightemp.txt", int(sys.argv[1]))

# split -l 5 hightemp.txt