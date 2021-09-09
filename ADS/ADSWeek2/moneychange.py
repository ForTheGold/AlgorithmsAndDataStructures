# Uses python3
import sys

def get_change(m):
	outVal = 0
	while m > 0:
		if m >= 10:
			m -= 10
		elif m >= 5:
			m -= 5
		elif m >= 1:
			m -= 1
		outVal += 1
	return outVal

if __name__ == '__main__':
	m = int(sys.stdin.read())
	print(get_change(m))
