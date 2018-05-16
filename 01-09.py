# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．

import random

def randomize(sentence):
    words = sentence.split()
    new_words = []
    for w in words:
        length = len(w)
        if length > 4:
            sampling = random.sample(w[1:-1], length - 2)
            new_words.append(w[0] + "".join(sampling) + w[-1])
        else:
            new_words.append(w)
    
    return " ".join(new_words)

sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print("Sentence")
print(sentence)
print("Randomized")
print(randomize(sentence))