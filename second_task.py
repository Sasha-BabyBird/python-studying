import re
with open("anaconda.txt", 'r+') as in_file:
    line = in_file.read()
    words = sorted(list(set(re.findall(r'\b[a-zA-z]+', re.sub('II', '2', line)))))
    #чтобы не учитывать "II" и "III" в списке слов
    #list(set(...)) - для удаления повторений, sorted - для единообразия
    #print(words)
    years = sorted(re.findall(r'[12]\d{3}', line))
    print(years)
with open("words.txt", 'w') as out_file:
    for i in range(1, len(words)):
        out_file.write(words[i] + '\n')
with open("years.txt", 'w') as out_file:
    for i in range(1, len(years)):
        out_file.write(years[i] + "\n")

 