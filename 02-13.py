# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

import codecs

def make(source1, source2, dest):
    encode = "utf-8"
    with codecs.open(source1, "r", encode) as f1 \
         , codecs.open(source2, "r", encode) as f2 \
         , codecs.open(dest, "w", encode) as f3:
         for col1, col2 in zip(f1, f2):
             f3.write(col1.strip() + "\t" + col2.strip() + "\n")

make("./col1.txt", "./col2.txt", "./col1and2.txt")

# $ paste ./col1.txt ./col2.txt