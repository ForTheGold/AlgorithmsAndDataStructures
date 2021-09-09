# Uses python3
import sys
import itertools

def partition3(A):
    suM = 0
    for i in A:
         suM += i
    if suM % 3 != 0:
        return 0
    else:
        suM /= 3
    return partition3handler(A, [0, 0, 0], 0, suM)



def partition3handler(A, array, pointer, target):
    table = {}
    def helper(A, array, pointer, target):
        if (pointer == len(A)) and (array[0] == array[1] == array[2]):
            return 1

        if pointer == len(A):
            return 0

        for i in range(len(array)):
            if f"{array[0]},{array[1]},{array[2]}" in table.values():
                return table[f"{array[0]},{array[1]},{array[2]}"]
            newArray = array.copy()
            newArray[i] = newArray[i] +  A[pointer]        
            result = helper(A, newArray, pointer + 1, target)
            table[f"{array[0]},{array[1]},{array[2]}"] = result
            if result == 1:
                return 1
        return 0
    return helper(A, array, pointer, target)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))