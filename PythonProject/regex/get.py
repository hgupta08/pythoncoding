import re

# p = re.compile(r'\d')
# s = "Python 3.10 was released on October 04, 2021"
#
# results = p.findall(s)
# print("".join(results)



s = "Python 3.10 was released on October 04, 2021."

pattern = r'\wnnn'
result = re.search(pattern, s)
print(type(result))
print(result)
result.start()
print('Matched string:',result.group())
print('Starting position:', result.start())
print('Ending position:',result.end())
print('Positions:',result.span())


#findall will return None if nothing matches
import re

s = "5-5-2021 or 05-05-2021 or 5/5/2021"

matches = re.finditer('\d{1,2}-\d{1,2}-\d{4}', s)

for match in matches:
    print(match)
s = '<button type="submit" class="btn">Send</button>'

pattern = '".+"' #it uses greedy mode...goes till last and comes back
# The meaning of the pattern is as follows:
#
# " starts with a quote
# . matches any character except the newline
# + matches the preceding character one or more times
# " ends with a quote
matches = re.finditer(pattern, s)

for match in matches:
    print(match.group())

#lazy mode
patt='".?"   v '