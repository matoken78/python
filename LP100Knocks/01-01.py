# 01. 「パタトクカシーー」
# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

def extract(str):
    return str[::2]

print(extract("パタトクカシーー"))