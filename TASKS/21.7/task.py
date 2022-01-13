""" У текстовому файлі міститься текст укр.мовою. Стиснути цей текст, видаливши у словах усі голосні літери.
Якщо у слові тільки голосні літери або солво має довжину не більше 2 символів, - голосні не видаляти.
Використати регулярні вирази """

import re

textfile = open('text.txt', 'r', encoding='UTF-8')
text = ""
for line in textfile:
	text += line

text2 = []
text = text.split()
    
for word in text:
	if(len(word)>2):
	    text2.append(re.sub(r'[аоуіие]', '', word, flags=re.IGNORECASE))
	else:
	    text2.append(word)
	    
text = ''
for i in range(len(text2)):
    text += text2[i] + ' '
    
print(text)
textfile.close()