# import re
# print(bool(re.search(r'are$', 'spare')))
#
# elements = ['spare\ntool', 'par\n', 'dare']
# for e in elements:
#     if re.search('are$',e):
#         print(e)

import re

# s = 'news/100'
# pattern = r'\w+/\d+'
#
# matches = re.finditer(pattern, s)
# for match in matches:
#     print(match)

import re

s = 'news/100'
pattern = r'\w+/(\d+)'

matches = re.finditer(pattern, s)
for match in matches:
    for index in range(0, match.lastindex + 1):
        print(index)
        print(match.group(index))


import re

s = 'news/2021/12/31'
pattern = '(?P<resource>\w+)/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})'

matches = re.finditer(pattern, s)
for match in matches:
    print(match.groupdict())

