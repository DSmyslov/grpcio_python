import grpc
import my_service_pb2
import my_service_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = my_service_pb2_grpc.JustAnotherServiceStub(channel)
    print("Trying to make a simple gRPC call...")
    ans = stub.DoSomeMath(my_service_pb2.MathRequest(x=5, y=17, op="+"))
    print(ans)
    print("Finished!")


if __name__ == '__main__':
    run()
