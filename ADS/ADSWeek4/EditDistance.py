# Uses python3
def edit_distance(s, t):
    x = len(s)
    y = len(t)
    matrix = [[0 for j in range(y + 1)] for i in range(x + 1)]

    for i in range(x + 1):
        for j in range(y + 1):
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                matrix[i][j] = i
            elif s[i-1] == t[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = 1 + min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1])
    return matrix[x][y]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
