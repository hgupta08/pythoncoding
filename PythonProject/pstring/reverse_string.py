
def reversed_string(text):

    result = ""
    for char in text:
        print(char)
        result = char + result
        print(result)


    return result


def reversed_string_whileloop(text):

    index= len(text)-1
    res=""
    while index>0:
        res=res+text[index]
        index=index-1

    return res
def reversed_string_recursive(text):
     print(text)
     if len(text) == 1:
         print(text)
         return text
     return reversed_string(text[1:]) + text[:1]

for char in reversed("greeting"): #traversiing in reverse
     print(char)



if __name__ == "__main__":

    g="asc"

    for char in g[::-1]:

      print(char)

    #print(reversed_string("Hello, World!"))
    #print(reversed_string_whileloop("abcdef"))
    #print(reversed_string_recursive('acdfef'))