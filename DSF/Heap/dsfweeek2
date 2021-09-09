# python3

from collections import namedtuple
import heapq

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def minHeapify(array, index):
    left = 2 * index + 1
    right = 2 * index + 2

    if left <= len(array) - 1 and array[left][0] < array[index][0]:
        smallest = left
    else:
        smallest = index
    if right <= len(array) - 1 and array[right][0] < array[smallest][0]:
        smallest = right
    if smallest != index:
        if left <= len(array) - 1 and right <= len(array) - 1 and array[left][0] == array[right][0]:
            if array[left][1] < array[right][1]:
                smallest = left
            else:
                smallest = right
        temp = array[smallest]
        array[smallest] = array[index]
        array[index] = temp

        minHeapify(array, smallest)

def increaseFirst(array, num):
    array[0][0] += num
    minHeapify(array, 0)

def assign_jobs(n_workers, jobs):
    result = []
    next_free_time = [[0, i] for i in range(n_workers)]
    heapq.heapify(next_free_time)
    for job in jobs:
        worker, index = heapq.heappop(next_free_time)
        result.append(AssignedJob(index, worker))
        worker += job
        heapq.heappush(next_free_time, [worker, index])

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()


