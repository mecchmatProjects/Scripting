import os
import datetime

filename = 'LOG'

def get_file(filename, file=None):
    if file != None:
        file.close
    if (file == None) or (os.path.getsize(file.name) > 1000):
        dt = str(datetime.datetime.now()).replace(':', '_')
        file = open(f'T22.6/{filename} {dt}.txt', 'w', encoding='utf8')
    else:
        file = open(file.name, 'a', encoding='utf8')
    return file

f = open('T22.6.txt', 'r', encoding='utf8')
file = get_file(filename)
for line in f.readlines():
    file = get_file(filename, file)
    print(line+'\n', file=file)

f.close
file.close