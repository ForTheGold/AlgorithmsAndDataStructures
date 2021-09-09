#Uses python3
import sys
import math

def closest_pair_bruteforce(points):
    mind = sys.maxsize
    cpairs = None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance_sq(points[i], points[j])
            if dist < mind:
                mind = dist 
                cpairs = (points[i], points[j])
    return mind, cpairs[0], cpairs[1]

def closest_split_pair(Px, Py, d):
    # get the point in the boundary x-coordinate
    xbar = Px[len(Px)/2].x

    # get all the points between xbar - d and xbar + d
    # sorted by y-coordinates
    Sy = []
    for point in Py:
        if xbar - d <= point.x <= xbar + d:
            Sy.append(point)

    # compare each point with at most 7 neighboring points
    best = d
    best_pair = Px[0].x, Px[0].y

    for i in range(len(Sy)):
        for j in range(1, min(8, len(Sy) - i)):
            if distance_sq(Sy[i], Sy[i + j]) < best:
                best = distance_sq(Sy[i], Sy[i + j])
                best_pair = Sy[i], Sy[i + j]

    return best, best_pair[0], best_pair[1]

def minimum_distance(Px, Py):
    # base case
    if len(Px) < 4:
        return closest_pair_bruteforce(Px)
    mid = len(Px)//2
    print(mid)
    # divide px into left and right halves
    Q = Px[:mid]
    R = Px[mid:]

    # sort Q and R both by x and y coordinates
    Qx = sorted(Q, key = lambda p: p.x) # complexity can be imporved
    Qy = sorted(Q, key = lambda p: p.y) # complexity can be imporved
    Rx = sorted(R, key = lambda p: p.x) # complexity can be imporved
    Ry = sorted(R, key = lambda p: p.y) # complexity can be imporved

    # conquer step, recursively find closest pairs on
    # left and right halves
    dl, p1, q1 = minimum_distance(Qx, Qy)
    dr, p2, q2 = minimum_distance(Rx, Ry)
    d = min(dl, dr)
    # closest pair split pair. One point is in left half
    # and other in right half
    dc, p3, q3 = closest_split_pair(Px, Py, d)

    # find the minimum and return the pair
    mind = min(dl, dr, dc)
    if mind == dl:
        return dl
    elif mind == dr:
        return dr
    else:
        return dc

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))