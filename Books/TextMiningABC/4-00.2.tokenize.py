# -*- coding: utf-8 -*-

# 英文の分割
# python -m nltk.downloader punkt で tokenizer をダウンロードする必要がある
# python -m nltk.downloader inaugural で inaugural コーパスをダウンロードする必要がある
#  (python -m nltk.downloader all なら全コーパスをダウンロードする)
import nltk
from nltk.corpus import inaugural
text = inaugural.raw('1789-Washington.txt')
sents = nltk.tokenize.sent_tokenize(text)
for u in sents:
    print('>>   ' + u + '<<')