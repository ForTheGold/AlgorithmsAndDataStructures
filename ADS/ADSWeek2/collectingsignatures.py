# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def find_min_seg(segments):
    minSeg = 0
    for i in range(1, len(segments)):
        if segments[minSeg].end > segments[i].end:
            minSeg = i
    return minSeg


def optimal_points(segments):
    points = []
    while len(segments) > 0:
        if len(segments) == 1:
            points.append(segments[0].end)
            segments.pop()
        else:
            minSeg = find_min_seg(segments)
            temp = segments[minSeg].end
            points.append(temp)
            for x in segments[:]:
                if x.start <= temp and temp <= x.end:
                    segments.remove(x)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
