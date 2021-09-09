import random
from time import time

array = []

for i in range(1000000):
	array.append(random.randint(0, 100000000))


def maxTwoProduct(array):
	max1 = 0
	max2 = 1
	for i in range(len(array)):
		if array[i] > array[max1] and array[max1] < array[max2] and i != max2:
			max1 = i
		if array[i] > array[max2] and array[max2]< array[max1] and i != max1:
			max2 = i
	return (array[max1] * array[max2])

def maxProductSort(a):
	a.sort()
	arrayLength = len(a)
	return (a[arrayLength-1] * a[arrayLength-2])


t0 = time()
print(maxTwoProduct(array))
t1 = time()
print(maxProductSort(array))
t2 = time()

print("Algo 1 took: ", (t1 - t0))
print("Algo 2 took: ", (t2 - t1))