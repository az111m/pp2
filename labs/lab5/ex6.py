import re

file = open('mytext.txt', 'r', encoding='utf8')

text = file.read()
file.close()

pattern = r"[\s.,]"
modified_text = re.sub(pattern, ":", text)
matches = re.finditer(pattern, modified_text)
for match in matches:
    print(match)