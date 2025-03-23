import textAnalyzer

zdanie1 = textAnalyzer.AdvancedTextAnalyzer('Mam dobry dzien! Co za dzien')
zdanie2 = textAnalyzer.AdvancedTextAnalyzer('Mam zły dzien! Co za dzien')
zdanie3 = textAnalyzer.AdvancedTextAnalyzer('Mam dzien! Co za dzien')
print(f'Ocena zdania:"{zdanie1.show_text()}" - {zdanie1.sentiment_analysis()}')
print(f'Ocena zdania:"{zdanie2.show_text()}" - {zdanie2.sentiment_analysis()}')
print(f'Ocena zdania:"{zdanie3.show_text()}" - {zdanie3.sentiment_analysis()}')