from aozora import Aozora
import MeCab
import nltk


def print_data(label, data):
    can_print = True
    if not can_print:
        return
    print('\n*** ', label)
    print(data)


aozora = Aozora('wagahaiwa_nekodearu.txt')
m = MeCab.Tagger('-Owakati -b65535')
all_text = m.parse('\n'.join(aozora.read()))
text = nltk.Text(nltk.word_tokenize(all_text))

word = '吾輩'
c = nltk.text.ConcordanceIndex(text)
c.print_concordance(word, width=40)
print_data('KWICの位置情報', c.offsets(word))
