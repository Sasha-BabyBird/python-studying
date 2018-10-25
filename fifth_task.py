import re
import pymorphy2
import collections as cl
morph = pymorphy2.MorphAnalyzer()
single_word = re.compile(r'\b[А-Яа-яЁё]+')
'''
Создаём список всех возможных форм
пяти наиболее распространённых слов из текста
'''
with open('most_common_words.txt', 'r+', encoding='utf-8') as in_file:
    five_words = re.findall(single_word, in_file.read())[0:5]
#print(five_words)
formlist = []
for i in range(5):
    for j in range(len(morph.parse(five_words[i])[0].lexeme)):
        formlist.append(morph.parse(five_words[i])[0].lexeme[j].word)
        formlist.append(morph.parse(five_words[i])[0].lexeme[j].word.capitalize())
#print(list(set(formlist)))
'''
Проходя через список всех слов из текста,
создаём список словосочетаний с указанными словами.
'''
with open('News.txt', 'r+', encoding='utf-8') as in_file:
    wordlist = re.findall(r'\b[А-Яа-яЁёA-Za-z.,»:;?!-]+', in_file.read())
#print(wordlist)
phrases = []
for i in range(len(wordlist) - 1):
    '''
    проверка на in formlist отсеивает в т.ч. и 
    слова, стоящие перед знаками препинания
    '''
    if wordlist[i] in formlist:
        phrases.append(wordlist[i] + ' ' + wordlist[i+1])
phrases = re.findall(r'\b[А-Яа-яЁёA-Za-z-]+\s[А-Яа-яЁёA-Za-z-]+', str(phrases))
phrases_counter = sorted(cl.Counter(phrases).items())
#print(phrases_counter)
with open('phrases.txt', 'w', encoding='utf-8') as out_file:
    for i in range(len(phrases_counter)):
        out_file.write(f'{str(phrases_counter[i])}\n')