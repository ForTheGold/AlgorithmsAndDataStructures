string = "abcdef"
i = 0
j = 1
k = 1

string = (string[j+1:k+2] + string[i:j+1] + string[k+j+1:])

i = 2
j = 3
k = 5

string = (string[0:k] + string[i:j+1] + string[k:i] + string[j+1:])
print(string)