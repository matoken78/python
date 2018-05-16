# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
# N-gram：https://sakuhindb.com/pj/6_B4C9CDFDBFCDA4B5A4F3/20060203.html
#         http://gihyo.jp/dev/serial/01/make-findspot/0005

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

sentence = "I am an NLPer"
print("単語bi-gram")
print(make_ngram(sentence, 2, 0))

print("文字bi-gram")
print(make_ngram(sentence, 2, 1))