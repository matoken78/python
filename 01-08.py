# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# •英小文字ならば(219 - 文字コード)の文字に置換
# •その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．


def cipher(sentence):
    ciphered = ""

    for char in sentence:
        if char.islower():
            ciphered += chr(219 - ord(char))
        else:
            ciphered += char
    
    return ciphered

sentence = "I am NOT a python Engineer yet."

print("Sentence")
print(sentence)

ciphered_sentence = cipher(sentence)
print("Ciphered")
print(ciphered_sentence)

print("Decoded")
print(cipher(ciphered_sentence))
