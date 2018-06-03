import pandas as pd
df1 = pd.read_excel(u'2-02.pivot.xlsx', u'販売履歴')
df2 = pd.read_excel(u'2-02.pivot.xlsx', u'商品')

df3 = pd.merge(df1, df2, on='商品ID')
print()
print('***** merge table *****')
print(df3)

print()
print('***** pivot table *****')
print(df3.pivot_table(u'金額', [u'店舗ID', u'商品名'], u'売上日', aggfunc='sum'))

def category(row):
    return {101: u'食料品'}.get(row[u'商品ID'], u'その他')

df1[u'商品カテゴリ'] = df1.apply(category, axis=1)
print()
print('***** original category *****')
print(df1)