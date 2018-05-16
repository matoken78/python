# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

def combine(str_a, str_b):
    result = ""
    for a, b in zip(str_a, str_b):
        result += a + b
    
    return result

print(combine("パトカー", "タクシー"))
