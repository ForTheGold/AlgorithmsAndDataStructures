# Uses python3
import sys

def find_best_item(weights, values):
    best = 0
    maxVal = values[0] / weights[0]
    for i in range(1, len(weights)):
        if values[i] /weights[i] > maxVal:
            maxVal = values[i]/weights[i]
            best = i
    return best


def get_optimal_value(capacity, weights, values):
    value = 0.
    while capacity > 0:
        try:
            maxVal = find_best_item(weights, values)
        except:
            capacity = 0
            break
        if capacity > weights[maxVal]:
            value += values[maxVal]
            capacity -= weights[maxVal]
            values.pop(maxVal)
            weights.pop(maxVal)
        else:
            value += (values[maxVal] / weights[maxVal]) * capacity
            capacity = 0
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
