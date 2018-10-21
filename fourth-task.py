import re
import pymorphy2
import collections as cl
morph = pymorphy2.MorphAnalyzer()
single_word = re.compile(r'\b[А-Яа-яЁёA-Za-z-]+')
with open('stop.txt', 'r+', encoding='utf-8') as stop_file:
    stoplist = re.findall(single_word, stop_file.read())
stoplist += ['автор', 'дата', 'неизвестно']    
with open('News.txt', 'r+', encoding='utf-8') as in_file:
    text = in_file.read()
'''
Создаём список всех слов в тексте.
'''    
wordlist = re.findall(single_word, text)
#print(wordlist)
#print(stoplist)
'''
Приводим каждое слово из списка
к нормальной форме.
'''
for i in range(len(wordlist)):
    wordlist[i] = morph.parse(wordlist[i])[0].normal_form
#print(len(wordlist))

'''
Удаляем все стоп-слова из списка
'''
i = 0
while i < len(wordlist):
    if wordlist[i] in stoplist:
        del wordlist[i]
    else:
        i += 1
'''
С помощью структуры данных "счётчик"
выводим нужное количество самых распространённых слов. 
'''                  
result = list(dict(cl.Counter(wordlist).most_common(30)))
with open('most_common_words.txt', 'w', encoding='utf-8') as out_file:
    for word in result:
        out_file.write(word + '\n')






