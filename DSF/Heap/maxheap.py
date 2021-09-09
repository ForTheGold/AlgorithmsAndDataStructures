def maxHeapify(array, index):
    left = 2 * index + 1
    right = 2 * index + 2

    if left <= len(array) - 1 and array[left] > array[index]:
        largest = left
    else:
        largest = index
    if right <= len(array) - 1 and array[right] > array[largest]:
        largest = right
    if largest != index:
        temp = array[largest]
        array[largest] = array[index]
        array[index] = temp

        maxHeapify(array, largest)

def buildMaxHeap(array):
    for i in range(len(array)//2, -1, -1):
        maxHeapify(array, i)

def insert(array, key):
    array.append(0)
    increaseKey(array, len(array) - 1, key)

def maximum(array):
    return array[0]



def extractMax(array):
    if len(array) == 0:
        return False
    maxElement = array[0]
    array[0] = array[len(array) - 1]
    array.pop()
    maxHeapify(array, 0)
    return maxElement

def increaseKey(array, element, key):
    if array[element] > key:
        return False

    array[element] = key
    while element > 0 and array[(element - 1) // 2] < array[element]:
        temp = array[element]
        array[element] = array[(element - 1) // 2]
        array[(element - 1) // 2] = temp
        element = (element - 1) // 2


array = [1, 2, 3, 4, 5, 6]

buildMaxHeap(array)
num = extractMax(array)
increaseKey(array, 4, 10)
insert(array, 1000)

print(num)
print(array)