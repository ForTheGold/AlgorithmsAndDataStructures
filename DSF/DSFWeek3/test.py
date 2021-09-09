dictionary = {}

dictionary[1] = "good"
dictionary[4] = "great"
dictionary[3] = "grand"
dictionary[2] = "wonderful"
dictionary[5] = "no yelling on the bus"

print(dictionary[1])
print(dictionary[4])
print(dictionary[3])
print(dictionary[2])
print(dictionary[5])
try:
    print(dictionary[6])
except:
    print("No he didn't")