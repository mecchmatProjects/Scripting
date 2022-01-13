import re

messages = ''
with open('T21.6/messages.txt', 'r') as f:
    messages = f.read()


for email in set(re.findall('([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', messages)):
    print(email)