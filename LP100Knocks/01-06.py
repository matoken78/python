# 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

def make_ngram(sentence: str, num, mode = 0):

    if mode == 0:
        chars = sentence.split()
    else:
        dic = str.maketrans("", "", " ")
        chars = sentence.translate(dic)

    ngram = []
    for i in range(1, len(chars)):
        ngram.append(chars[i - 1: i + 1])

    return ngram

sentence_a = "paraparaparadise"
sentence_b = "paragraph"

# list は、和集合などに対応していないので、set に変換
x = set(make_ngram(sentence_a, 2, 1))
y = set(make_ngram(sentence_b, 2, 1))

print("和集合")
print(x | y)

print("積集合")
print(x & y)

print("差集合")
print(x - y)

print("\"se\"がXに含まれるかどうか")
print("se" in x)
print("\"se\"がYに含まれるかどうか")
print("se" in y)
