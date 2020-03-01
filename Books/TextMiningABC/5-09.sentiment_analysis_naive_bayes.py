# download from this 'sentence polarity dataset'
# http://www.cs.cornell.edu/people/pabo/movie-review-data/

from nltk.tokenize import word_tokenize
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy


def format_sentence(sentence):
    return {word: True for word in word_tokenize(sentence)}


with open('./sentiment/rt-polarity.pos', encoding='latin-1') as f:
    pos_data = [[format_sentence(line), 'pos'] for line in f]
with open('./sentiment/rt-polarity.neg', encoding='latin-1') as f:
    neg_data = [[format_sentence(line), 'neg'] for line in f]

training_data = pos_data[:4000] + neg_data[:4000]
test_data = pos_data[4000:] + neg_data[4000:]

model = NaiveBayesClassifier.train(training_data)

sentences = ['This is a nice article',
             'This is a bad article',
             'This is not a nice article']

for sentence in sentences:
    result = model.classify(format_sentence(sentence))
    print(result, ': ', sentence)

print('accuracy', accuracy(model, test_data))
