import re

with open('T21.2.txt', 'r', encoding='utf8') as f:
    text = f.read()

text = re.findall('\S.*?\."?(?=\s|$)', text)

for i in range(len(text)):
    print(f'{i+1}) {text[i]}')