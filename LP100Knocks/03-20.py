# 20. JSONデータの読み込み
# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
# 問題21-29では，ここで抽出した記事本文に対して実行せよ．

# https://docs.python.jp/3/library/json.html

import codecs
import json

def read(word):
    for line in codecs.open(".\jawiki-country.json", "r", "utf-8"):
        article = json.loads(line)
        if article["title"] == word:
            print(article["text"])

read("イギリス")