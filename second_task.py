import re
with open("anaconda.txt", 'r+') as in_file:
    line = in_file.read()
    words = sorted(list(set(re.findall(r'\b[a-zA-Z]+', re.sub('II', '2', line)))))
    #чтобы не учитывать "II" и "III" в списке слов
    #list(set(...)) - для удаления повторений, sorted - для единообразия
    #print(words)
    years = sorted(re.findall(r'[12]\d{3}', line))
    #print(years)
with open("words.txt", 'w') as out_file:
    for word in words:
        out_file.write(f'{word}\n')
with open("years.txt", 'w') as out_file:
    for year in years:
        out_file.write(f'{year}\n')