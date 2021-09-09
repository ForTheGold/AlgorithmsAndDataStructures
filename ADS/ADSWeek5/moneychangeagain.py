# Uses python3
import sys

def get_change(m):
    array = [0] * (m+1)
    possibleCoins = [1, 3, 4]
    counter = 0
    while counter <= m:
        for coin in possibleCoins:
            number_of_coins = array[counter] + 1
            try:
                if array[counter + coin] == 0 or array[counter + coin] > number_of_coins:
                    array[counter + coin] = number_of_coins
            except:
                continue
        counter += 1
    return array[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
