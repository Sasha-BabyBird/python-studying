import re
with open('News.txt', 'r+', encoding='utf-8') as in_file:
    #news_piece = re.compile(r'[^-_\s](?:.*?\s*?)+?(?=-+\n_+)')
    line = in_file.read()
#date = re.compile(r'(?<=Дата: ).*(?=$)', flags=re.MULTILINE) 
'''
Создаём два списка: один содержит все новости,
другой - все даты.
'''
news = re.split(r'-{11}\n*', line)
del news[-1:0]
dt = re.findall(r'(?<=Дата: ).*(?=$)', line, flags=re.MULTILINE)
ln = len(dt)
'''
Разбиваем список дат так,
чтобы дни, месяцы, года и время
хранились в разных ячейках.
'''
datestring = ''
for date in dt:
    datestring += date + ','
dt = re.split(r'[.,]', datestring)
#print(dt)
'''
Сборка обратно в единый список дат
в таком формате, чтобы эти даты
можно было упорядочить обычной сортировкой.
'''
for i in range(ln):
    dt[i*4], dt[i*4+2] = dt[i*4+2], dt[i*4]
    dt[i] = (dt[i*4] + dt[i*4+1] +
                  dt[i*4+2] + dt[i*4+3] + f', {i}') 
del dt[ln:]  
#print(dt)
'''
Определяем, как были переставлены даты
в процессе сортировки,
и выводим новости в нужном порядке.
'''
indices = re.findall(r'(?<=, )\d+', str(sorted(dt)))
#print(indices)
with open ('SortedNews.txt', 'w', encoding='utf-8') as out_file:
    for ind in indices:
        out_file.write(news[int(ind)])





