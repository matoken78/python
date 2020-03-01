# download from this
# http://www2.imm.dtu.dk/pubdb/views/edoc_download.php/6010/zip/imm6010.zip

from nltk.tokenize import sent_tokenize, word_tokenize


def print_data(label, data):
    can_print = True
    if not can_print:
        return
    print('\n*** ', label)
    print(data)


AFINNfile = './sentiment/AFINN-111.txt'
sentiment_dictionary = {}
for line in open(AFINNfile):
    word, score = line.split('\t')
    sentiment_dictionary[word] = int(score)

str = 'The first music is good, but the second and third musics are terrible and boring. It is a bad idea to buy this CD.'

# Sentence Sentiment
print('\n*** Sentence sentiment:')
for sent in sent_tokenize(str):
    words = word_tokenize(sent.lower())
    score = sum(sentiment_dictionary.get(word, 0) for word in words)
    print(score, ': ', sent)

print('\n*** Sentence sentiment with detail:')
for sent in sent_tokenize(str):
    words = word_tokenize(sent.lower())
    pos = 0
    neg = 0
    for word in words:
        score = sentiment_dictionary.get(word, 0)
        if score > 0:
            pos += score
        elif score < 0:
            neg += score
    print([pos, neg], ': ', sent)
