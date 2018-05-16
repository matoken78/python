# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．

import codecs

encode = "utf-8"

def write(source, dest1, dest2):
    with codecs.open(dest1, "w", encode) as file1, codecs.open(dest2, "w", encode) as file2:
        for line in codecs.open(source, "r", encode):
            cols = line.split("\t")
            file1.write(cols[0] + "\n")
            file2.write(cols[1] + "\n")

write("./hightemp.txt", "./col1.txt", "./col2.txt")

# $ cut -f 1 ./hightemp.txt > col1.txt
# $ cut -f 2 ./hightemp.txt > col2.txt