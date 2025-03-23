import textAnalyzer

zdanie1 = textAnalyzer.AdvancedTextAnalyzer('Mam dobry dzien! Co za dzien')
print(f'Ocena zdania:"{zdanie1.show_text()}" - {zdanie1.sentiment_analysis()}')