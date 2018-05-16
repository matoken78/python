# 10. 行数のカウント
# 行数をカウントせよ．
# 確認にはwcコマンドを用いよ．

import codecs

def count(file_path):
    return sum(1 for line in codecs.open(file_path, "r", "utf-8"))

print(count("./hightemp.txt"))

# $ wc -l ./hightemp.txt