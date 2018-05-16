# 18. 各行を3コラム目の数値の降順にソート
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

import codecs

encode = "utf-8"

def sort_items(colnumber, isreverse):
    for line in sorted(codecs.open(".\hightemp.txt", "r", encode), key=lambda line: float(line.split("\t")[colnumber]), reverse=isreverse):
        print("".join(line), end = "")

sort_items(2, True)

# sort -r -n -k 3,3 hightemp.txt