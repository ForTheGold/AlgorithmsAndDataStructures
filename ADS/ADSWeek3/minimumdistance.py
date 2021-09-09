#Uses python3
import sys
import math




def solution(x, y):
	a = list(zip(x, y)) 
	ax = sorted(a, key=lambda x: x[0])  
	ay = sorted(a, key=lambda x: x[1])  
	p1, p2, mi = closest_pair(ax, ay)  
	return mi

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
