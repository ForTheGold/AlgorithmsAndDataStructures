# Uses python3
import sys

def optimal_summands(n):
	summands = []
	nextValue = 1
	while n > 0:
		if n-nextValue == 0 or n-nextValue >= nextValue+1:
			summands.append(nextValue)
			n -= nextValue
		nextValue += 1		
	return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
