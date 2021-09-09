# Uses python3
import math

def calc_fib():
    array = []
    for i in range(60):
        fib = (1 + math.sqrt(5)) / 2
        fib = round(fib**i / math.sqrt(5))
        array.append(fib%10)
    return array

def calcLastDig(n):
    fibarray = calc_fib()
    return fibarray[n%60]


fibarray = calc_fib()
s = 0
for i in fibarray:
	s += i
print(s)
