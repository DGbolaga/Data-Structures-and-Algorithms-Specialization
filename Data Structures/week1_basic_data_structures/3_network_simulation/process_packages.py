# python3

from collections import namedtuple, deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])

# Response(False, -1)

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque()
        self.finish_sum = 0

    def process(self, request):
        #print(request)


        # check if any packet has been processed and remove them.
        while self.finish_time and self.finish_time[0] <= request.arrived_at:
            self.finish_time.popleft()

        # add to buffer if capacity is not reached.
        if len(self.finish_time) < self.size:
            if request.arrived_at > self.finish_sum:
                ans = Response(False, request.arrived_at) # it will start processing only when it arrived
            else:
                ans = Response(False, self.finish_sum) # it will start when every other packet has been processed

            finish = max(self.finish_sum, request.arrived_at) + request.time_to_process
            self.finish_time.append(finish)
            self.finish_sum = finish
            #print(f"1 - {ans}\n Finish_time_arry: {self.finish_time} \n Finish_sum: {self.finish_sum}")
            return ans 
        
        if request.arrived_at >= self.finish_sum:
            finish = request.arrived_at + request.time_to_process
            self.finish_time = deque([finish])
            self.finish_sum = finish

            #print(f"2 - {Response(False, request.arrived_at)}\n Finish_time_arry: {self.finish_time} \n Finish_sum: {self.finish_sum}")
            return Response(False, request.arrived_at) # starts processing immediately when recieved
        
        # continue process if the buffer is full and it arrived earlier than the buffer could compute all the packet.
        # if no packet as been processed drop the incoming packet.
        
        if len(self.finish_time) >= self.size: 
            #print(f"3 - {Response(True, -1)}\n Finish_time_arry: {self.finish_time} \n Finish_sum: {self.finish_sum}")
            return Response(True, -1) # drop packet
        else: 
            #choose max between start processing when the processor is free and when it arrives later
            start_time = max(self.finish_sum, request.arrived_at)
            finish_time = start_time + request.time_to_process
            self.finish_time.append(finish_time)
            self.finish_sum = finish_time
            #print(f"4 - {Response(False, self.finish_sum)}\n Finish_time_arry: {self.finish_time} \n Finish_sum: {self.finish_sum}")
            return Response(False, self.finish_sum) # starts processing when others are completed



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

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
