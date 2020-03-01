from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

# compound は、総合的な評価値


def print_data(label, data):
    can_print = True
    if not can_print:
        return
    print('\n*** ', label)
    print(data)


vader_analyzer = SentimentIntensityAnalyzer()

sentences = ['I am happy',
             'I am happy :-)',
             'I am happy :-) :-)',
             'I am sad',
             'I am sad :-(']
for sentence in sentences:
    result = vader_analyzer.polarity_scores(sentence)
    print(result, ': ', sentence)
