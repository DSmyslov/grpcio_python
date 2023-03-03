import asyncio
import logging

import grpc
import my_service_pb2
import my_service_pb2_grpc


async def run():

    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = my_service_pb2_grpc.JustAnotherServiceStub(channel=channel)

        # print("Trying to make a simple gRPC call...")
        # ans = await stub.DoSomeMath(my_service_pb2.MathRequest(x=1024, y=0, op="/"))
        # print(ans)
        # print("Finished!")

        print("Trying to make response-streaming gRPC call...")
        title = input("Введите тайтл: ")
        async for anime in stub.ListAnimeByTitle(my_service_pb2.AnimeTitle(title=title)):
            print(anime)
        print("Finished!")


if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(run())
