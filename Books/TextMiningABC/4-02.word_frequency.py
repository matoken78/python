from collections import Counter
from aozora import Aozora
import MeCab

aozora = Aozora('wagahaiwa_nekodearu.txt')
string = '\n'.join(aozora.read())       # 1つの文字列データにする

# 形態素解析して、語の出現頻度を数える
m = MeCab.Tagger('-Ochasen')            # MeCab で単語に分割する
mecablist = []
wlist = m.parse(string).splitlines()
for u in wlist:
    mecablist.append([v for v in u.split()])

# 得られた単語情報リストから、単語の部分だけを取り出したリストを作る
wordbodylist = [u[0] for u in mecablist]

# 単語のリストで出現頻度を数える
cnt = Counter(wordbodylist)

# 頻度順に100個表示
print(sorted(cnt.items(), key=lambda x: x[1], reverse=True)[:100])