# Uses python3
import sys

def get_change(m):
    array = [0] * (m+1)
    possibleCoins = [1, 3, 4]
    for i in range(m+1):
    	minCoins = i
    	for j in [coin for coin in possibleCoins if coin <= i]:
    		if array[i-j] + 1 < minCoins:
    			minCoins = array[i - j] + 1
    	array[i] = minCoins
    return array[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
