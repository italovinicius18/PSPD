import logging
import random

import grpc
import lab_pb2
import lab_pb2_grpc

from functools import wraps
import time

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

def generateList(size):
    list = []
    for i in range(size):
        vI = (i-(random.randint(0, size)/2))**2 # v[i] = (i – (f_aleat(0-X)/2)) ** 2;
        vI = vI**(1/2) # v[i] = raiz_quadrada(v[i]);
        list.append(vI) 
    return list

@timeit
def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.

    size = 500000

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = lab_pb2_grpc.LabStub(channel)

        request = lab_pb2.LabRequest()
        request.values.extend(generateList(size))
        request.size = size

        response = stub.BigSmall(request)

        biggest = response.biggest
        biggestIndex = response.biggestIndex
        smallest = response.smallest
        smallestIndex = response.smallestIndex

        print("Biggest: " + str(biggest))
        print("Biggest Index: " + str(biggestIndex))
        print("Smallest: " + str(smallest))
        print("Smallest Index: " + str(smallestIndex))


if __name__ == '__main__':
    logging.basicConfig()
    run()
