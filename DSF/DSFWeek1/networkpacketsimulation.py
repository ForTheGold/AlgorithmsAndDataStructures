# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, max_size, curr_size):
        self.max_size = max_size
        self.curr_size = curr_size
        self.finish_time = []

    def process(self, request):
        while len(self.finish_time) > 0 and request.arrived_at >= self.finish_time[len(self.finish_time)-1]:
            self.curr_size += 1
            self.finish_time.pop()

        if len(self.finish_time) > 0:
            if request.arrived_at >= self.finish_time[0]:
                #self.curr_size -= 1
                self.finish_time.insert(0, request.arrived_at + request.time_to_process)
                return Response(False, request.arrived_at)
            elif request.arrived_at <= self.finish_time[0] and self.curr_size >= 1 and self.curr_size != 0:
                self.curr_size -= 1
                self.finish_time.insert(0, max(request.arrived_at, self.finish_time[0]) + request.time_to_process)
                return Response(False, self.finish_time[1])
        else:
            self.curr_size -= 1
            self.finish_time.insert(0, request.arrived_at + request.time_to_process)
            return Response(False, request.arrived_at)
        return Response(True, -1)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size, buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
