# Uses python3
import sys

def optimal_sequence(n):
    starterArray = [-1, 0]
    array = [0, 1]
    for i in range(2, n+1):
        count_3 = count_2 = count_1 = n
        if i % 3 == 0:
            count_3 = starterArray[(i//3)]
        if i % 2 == 0:
            count_2 = starterArray[(i//2)]
        if i - 1 >= 0:
            count_1 = starterArray[i-1]
        starterArray.append(min(count_3+1, count_2+1, count_1+1))
        if count_3 <= min(count_2, count_1):
            array.append((i//3))
        elif count_2 <= min(count_3, count_1):
            array.append(int(i//2))
        elif count_1 <= min(count_3, count_2):
            array.append(i-1)
    array_2 = [n]
    for i in range(starterArray[n]):
        array_2.append(array[n])
        n = array[n]
    array_2.reverse()
    return array_2

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
