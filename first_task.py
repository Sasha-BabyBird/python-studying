file = open("anaconda.txt", 'r+')
newline = ''
while True:
    line = file.readline().lower().replace("snake", "python")
    """
    line = line.lower()
    #print(repr(line))
    #line = line.replace("snake", "python")
    print(repr(line))
    """
    if 'anaconda' in line and 'python' in line:
        newline += line 
    if not line:
        break
file.close()
print(newline)
with open("result.txt", 'w') as file:
    file.write(newline)
    