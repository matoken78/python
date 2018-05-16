# 17. １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．
# 確認にはsort, uniqコマンドを用いよ．

import codecs

encode = "utf-8"

def get_unique_items(col_number):
    items = set()
    for line in codecs.open(".\hightemp.txt", "r", encode):
        cols = line.split("\t")
        items.add(cols[0])
    
    return items

print(get_unique_items(0))

# cat ./src/hightemp.txt | cut -f1 | sort | uniq