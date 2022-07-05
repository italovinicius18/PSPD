from concurrent import futures
import logging

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

class Lab(lab_pb2_grpc.LabServicer):

  @timeit
  def BigSmall(self, request, context):
    
    biggest = request.values[0]
    biggestIndex = 0
    smallest = request.values[0]
    smallestIndex = 0

    for i in range(request.size):
      if request.values[i] > biggest:
        biggest = request.values[i]
        biggestIndex = i
      if request.values[i] < smallest:
        smallest = request.values[i]
        smallestIndex = i

    return lab_pb2.LabResponse(
      biggest=biggest,
      smallest=smallest,
      biggestIndex=biggestIndex,
      smallestIndex=smallestIndex
    )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    lab_pb2_grpc.add_LabServicer_to_server(Lab(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
