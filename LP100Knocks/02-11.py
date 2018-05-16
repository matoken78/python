# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．
# 確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

import codecs

def change_tab_to_space(file_path):
    for line in codecs.open(file_path, "r", "utf-8"):
        print(line.replace("\t", " "))

change_tab_to_space("./hightemp.txt")

# $ cat ./hightemp.txt | sed -e 's/\t/ /g'