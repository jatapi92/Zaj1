from sentimentpl.models import SentimentPLModel

class TextAnalyzer:


    def __init__(self, text):
        self.text = text

    def showText(self):
        print(self.text)

    def word_count(self):
        newText = replace_special_chars(self.text)
        words = newText.split()
        wordsNo = len(words)
        return f'Zdanie składa się z {wordsNo} słów.'

    def char_count(self):
        chars = len(self.text)
        return f'Zdanie sklada sie z {chars} znaków.'

    def unique_words(self):
        newText = replace_special_chars(self.text)
        words = newText.split()
        uniqueWordsNo = len(set(words))
        return uniqueWordsNo

class AdvancedTextAnalyzer(TextAnalyzer):


    def __init__(self, text):
        super().__init__(text)

    def sentiment_analysis(self):
        model = SentimentPLModel(from_pretrained='latest')
        moodValue = model(self.text).item()
        if moodValue > 0.4:
            return 'Possitive sentiment'
        elif moodValue < -0.1:
            return 'Negative sentiment'
        else:
            return 'Neutral sentiment'

def replace_special_chars(text):
    return text.replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace('/', '').replace(':', '').replace(';', '').replace('(', '').replace(')', '')


zdanie1 = AdvancedTextAnalyzer('Mam 1 dzien! Co za dzien')
print(zdanie1.sentiment_analysis())