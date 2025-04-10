import re

s = 'Make the World a *Better Place*'
pattern = r'\*(.*?)\*'
replacement = r'<b>\1<\\b>'
html = re.sub(pattern, replacement, s)

print(html)


import re

email = 'no-reply@pythontutorial.net'
pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
match = re.fullmatch(pattern, email)

if match is not None:
    print(f'The email "{match.group()}" is valid')
else:
    print(f'The email "{email}"" is not valid')