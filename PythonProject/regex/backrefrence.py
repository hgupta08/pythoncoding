import re

s = 'Python Python is awesome'

new_s = re.sub(r'(\w+)\s+\1', r'\1', s)

print(new_s)


#here i am backreference the group 1 using \1 and replcing it


import re

s = "Black, blue and brown"
pattern = r'(bl(\w+))'
matches = re.findall(pattern, s, re.IGNORECASE)

print(matches)

