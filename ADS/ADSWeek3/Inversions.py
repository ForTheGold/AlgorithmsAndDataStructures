# Uses python3
import sys

def mergeSort(a, b, left, ave, right):
	i = k = left
	j = ave + 1
	number_of_inversions = 0
  
	while i <= ave and j <= right:
		if a[i] <= a[j]:
			b[k] = a[i]
			k += 1
			i += 1	
		else:
			b[k] = a[j]
			number_of_inversions += (ave-i + 1)
			k += 1
			j += 1	
 
	while i <= ave:
		b[k] = a[i]
		k += 1
		i += 1
 
	while j <= right:
		b[k] = a[j]
		k += 1
		j += 1
 
	for loop_var in range(left, right + 1):
		a[loop_var] = b[loop_var]
         
	return number_of_inversions

def get_number_of_inversions(a, b, left, right):
	number_of_inversions = 0
	if right - left <= 0:
		return number_of_inversions
	ave = (left + right) // 2
	number_of_inversions += get_number_of_inversions(a, b, left, ave)
	number_of_inversions += get_number_of_inversions(a, b, ave + 1, right)	
	number_of_inversions += mergeSort(a, b, left, ave, right)
    
	return number_of_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)-1))