with open('File1.txt') as f:
    for line in f:
        print(line.strip())

lines = ['Readme', 'How to write text files in Python']
with open('readme.txt', 'w') as f:
    f.write('\n'.join(lines))

more_lines = ['', 'Append text files', 'The End']

with open('readme.txt', 'a') as f:
    f.write('\n'.join(more_lines))