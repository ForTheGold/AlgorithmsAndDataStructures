# Uses python3
import sys
import math

def calc_fib():
    array = []
    for i in range(60):
        fib = (1 + math.sqrt(5)) / 2
        fib = round(fib**i / math.sqrt(5))
        array.append(fib%10)
    return array

def calc_sum(m, n):
    array = calc_fib()
    s = 0

    while m <= n:
        s += array[m%60]
        m += 1
        if m % 60 == 0:
            m -= 60
            n-=60
    return s%10

def calc_sum2(m, n):
    array = calc_fib()
    s = 0
    diff = n - m
    diff %= 60
    n = m + diff
    while m <= n:
        s += array[m%60]
        m += 1
    return s%10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(calc_sum2(from_, to))


# m and n are both in array, no problem
# n and m and more than 60 spaces apart, n - m 