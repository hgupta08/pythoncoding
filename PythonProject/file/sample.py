num_lines =0
mylist=[]
countchar=0
with open('File1.txt',"r") as f:

    for line in f:
        #print(line)
        num_lines += 1
        countchar += len(line)

        for word in line:

            if word != '\n':
                #print(word)
                mylist.append(word)

print(num_lines)
print(countchar)

print(len(set(mylist)))