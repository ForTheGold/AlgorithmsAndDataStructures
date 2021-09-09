def minHeapify(array, index):
    left = 2 * index + 1
    right = 2 * index + 2

    if left <= len(array) - 1 and array[left] < array[index]:
        smallest = left
    else:
        smallest = index
    if right <= len(array) - 1 and array[right] < array[smallest]:
        smallest = right
    if smallest != index:
        temp = array[smallest]
        array[smallest] = array[index]
        array[index] = temp

        minHeapify(array, smallest)

def buildMinHeap(array):
    for i in range(len(array)//2, -1, -1):
        minHeapify(array, i)

def insert(array, key):
    array.append(1000000)
    decreaseKey(array, len(array) - 1, key)

def minimum(array):
    return array[0]



def extractMin(array):
    if len(array) == 0:
        return False
    minElement = array[0]
    array[0] = array[len(array) - 1]
    array.pop()
    minHeapify(array, 0)
    return minElement

def decreaseKey(array, element, key):
    if array[element] < key:
        return False

    array[element] = key
    while element > 0 and array[(element - 1) // 2] > array[element]:
        temp = array[element]
        array[element] = array[(element - 1) // 2]
        array[(element - 1) // 2] = temp
        element = (element - 1) // 2


array = [10, 9, 8, 7, 6, 5]

buildMinHeap(array)
num = extractMin(array)
decreaseKey(array, 3, 4)
insert(array, 2)

print(num)
print(array)