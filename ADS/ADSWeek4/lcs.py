#Uses python3

import sys

def lcs3(a, b, c):
	matrix = [[[0 for z in range(len(c)+1)] for y in range(len(b)+1)] for x in range(len(a)+1)]

	for x in range(len(a)+1):
		for y in range(len(b)+1):
			for z in range(len(c)+1):
				if x == 0 or y == 0 or z == 0:
					matrix[x][y][z] = 0
				elif a[x-1] == b[y-1] == c[z-1]:
					matrix[x][y][z] = matrix[x-1][y-1][z-1] + 1
				else:
					matrix[x][y][z] = max(matrix[x-1][y][z], matrix[x][y-1][z], matrix[x][y][z-1])

	return matrix[-1][-1][-1]



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))



	# matrix = [[0 for y in range(len(b)+1)] for x in range(len(a)+1)]

	# for x in range(len(a)+1):
	# 	for y in range(len(b)+1):
	# 		if x == 0 or y == 0:
	# 			matrix[x][y] = 0
	# 		elif a[x-1] == b[y-1]:
	# 			matrix[x][y] = matrix[x-1][y-1] + 1
	# 		else:
	# 			matrix[x][y] = max(matrix[x-1][y], matrix[x][y-1])

	# return matrix[-1][-1]


# def lcsalgo(str1, str2):

# 	matrix = [[0 for y in range(len(str2)+1)] for x in range(len(str1)+1)]
# 	for x in range(len(str1)+1):
# 		for y in range(len(str2)+1):
# 			if x == 0 or y == 0:
# 				matrix[x][y] = 0
# 			elif str1[x-1] == str2[y-1]:
# 				matrix[x][y] = matrix[x-1][y-1] + 1
# 			else:
# 				matrix[x][y] = max(matrix[x-1][y], matrix[x][y-1])
# 	return matrix[-1][-1]

# str1 = "ABCDEFGHI"
# str2 = "DEFKKKI"
# print(lcsalgo(str1, str2))