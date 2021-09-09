word_list = ["world", "HellO", "World", "luck", "GooD"]
m = 5
array = [[] for _ in range(m)]

def hash(string, m):
    code = 0
    for i in range(len(string)):
        code += (ord(string[i]) * (263**i))
    code %= 1000000007
    code %= m
    return code 

def addWords(string, array, m):
    code = hash(string, m)
    array[code] = [string] + array[code]
    return array

def delWords(string, array, m):
    code = hash(string, m)
    try:
        array[code].remove(string)
    except:
        pass
    return array

def findWords(string, array, m):
    code = hash(string, m)
    if string in array[code]:
        return "yes"
    return "no"

def check(array, index):
    outString = ""
    for i in array[index]:
        outString += i + " "
    if outString == "None":
        print()
    else:
        print(outString)

for word in word_list:
    array = addWords(word, array, m)
array = delWords("GooD", array, m)
print(findWords("GooD", array, m))
print(findWords("World", array, m))
print(array)
print(check(array, 4))
