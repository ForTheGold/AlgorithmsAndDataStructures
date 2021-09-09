# Uses python3
import sys

def pisanoPeriod(m):
    last, curr = 0, 1
    for i in range(0, m * m):
        last, curr = curr, (last + curr) % m
        if (last == 0 and curr == 1):
            return i + 1
 
def fib(n, m):
    pisano = pisanoPeriod(m)
    n = n % pisano
     
    last = 0
    curr = 1

    if n <= 1:
    	return n

    for _ in range(n-1):
        last, curr = curr, last + curr
         
    return (curr % m)

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(fib(n, m))
