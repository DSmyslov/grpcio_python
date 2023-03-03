import asyncio
from concurrent import futures

import my_service_pb2_grpc
import my_service_pb2
import grpc


class JustAnotherServiceServicer(my_service_pb2_grpc.JustAnotherServiceServicer):

    def DoSomeMath(self, request, context):
        x = request.x
        y = request.y
        ans = ""
        match request.op:
            case "+":
                ans = f"{x} + {y} = {x + y}"
            case "-":
                ans = f"{x} - {y} = {x - y}"
            case "*":
                ans = f"{x} * {y} = {x * y}"
            case "/":
                try:
                    ans = f"{x} / {y} = {x // y}"
                except ZeroDivisionError:
                    ans = "You can't divide by zero!!"
            case _:
                ans = "Operation not implemented yet!"
        reply = my_service_pb2.MathResponse()
        reply.ans = ans
        return reply

    def ListAnimeByTitle(self, request, context):
        super().ListAnimeByTitle(request, context)

    def FloodWithMessages(self, request_iterator, context):
        super().FloodWithMessages(request_iterator, context)

    def SquareTheNumbers(self, request_iterator, context):
        for num in request_iterator:
            ans = my_service_pb2.Number()
            ans.x = num.x ** 2
            yield ans.x


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    my_service_pb2_grpc.add_JustAnotherServiceServicer_to_server(JustAnotherServiceServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    print("Starting server...")
    serve()
    