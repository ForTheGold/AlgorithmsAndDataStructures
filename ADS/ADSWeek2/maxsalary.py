#Uses python3

import sys

def findMax(array):
	maxVal = 0
	for i in range(1, len(array)):
		if int(array[i] + array[maxVal]) > int(array[maxVal] + array[i]):
			maxVal = i
	return int(maxVal)

def largest_number(a):
    res = ""
    while len(a) > 0:
    	maxVal = findMax(a)
    	res += str(a[maxVal])
    	a.pop(maxVal)
    	
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))