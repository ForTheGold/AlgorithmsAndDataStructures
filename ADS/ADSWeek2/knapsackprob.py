# Uses python3
import sys

class item():
	def __init__(self, weight, value, index):
		self.index = index
		self.weight = weight
		self.value = value
		self.ratio = weight // value


def get_optimal_value(capacity, weights, values):
    value = 0.
    itemValue = []
    for i in range(len(values)):
    	itemValue.append(item(weights[i], values[i], i))

    for i in itemValue:
    	print(i.value)


    	

    for i in range(1, len(itemValue)): 
        temp = itemValue[i]
        j = i-1
        while j >=0 and temp.ratio < itemValue[j].ratio: 
                itemValue[j+1] = itemValue[j]
                j -= 1
        itemValue[j+1] = temp 




    for i in itemValue:
    	print(i.value)
    	
    for i in itemValue:
    	if capacity - i.weight >= 0:
    		capacity -= i.weight
    		value += i.value
    	else:
    		fractionToTake = capacity / i.weight
    		value += fractionToTake * i.value
    		break


    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
