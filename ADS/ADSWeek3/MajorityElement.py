# Uses python3
import sys

def get_majority_element(a, left, right):
	hashMap = {}
	for i in a:
		if i in hashMap:
			hashMap[i] += 1
		else:
			hashMap[i] = 1

	for i in hashMap:
		if hashMap[i] > (len(a) // 2):
			return i
	return -1

if __name__ == '__main__':
	input = sys.stdin.read()
	n, *a = list(map(int, input.split()))
	if get_majority_element(a, 0, n) != -1:
		print(1)
	else:
		print(0)