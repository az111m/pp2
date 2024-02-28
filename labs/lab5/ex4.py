import re

file = open('mytext.txt', 'r', encoding='utf8')

text = file.read()

matches = re.finditer(r'[A-Z][a-z]+', text)
for match in matches:
    print(match)