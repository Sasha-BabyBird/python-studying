newline = ''
line = '*'
with open("anaconda.txt", 'r+') as in_file:
    while line:
        line = in_file.readline().lower().replace("snake", "python")
        if 'anaconda' in line and 'python' in line:
            newline += line 
#print(newline)
with open("result.txt", 'w') as out_file:
    out_file.write(newline)
    