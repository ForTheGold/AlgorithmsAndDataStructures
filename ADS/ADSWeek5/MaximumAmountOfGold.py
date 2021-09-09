# Uses python3
import sys

def optimal_weight(knapsack_weight, goldbar_array):
	weight_array = [[0 for x in range(knapsack_weight + 1)] for y in range(len(goldbar_array) + 1)]

	for i in range(len(goldbar_array) + 1):
		for j in range(knapsack_weight + 1):
			if i == 0 or j == 0:
				weight_array[i][j] = 0
			elif goldbar_array[i-1] <= j:
				weight_array[i][j] = max(goldbar_array[i-1] + weight_array[i-1][j-goldbar_array[i-1]], weight_array[i-1][j])
			else:
				weight_array[i][j] = weight_array[i-1][j]
	return weight_array[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

