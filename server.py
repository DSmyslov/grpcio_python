import logging

import aiohttp

import my_service_pb2_grpc
import my_service_pb2
import grpc

import asyncio


class JustAnotherServiceServicer(my_service_pb2_grpc.JustAnotherServiceServicer):

    _http_client_session = None

    def __init__(self):
        self._http_client_session = aiohttp.client.ClientSession()

    def get_http_client_session(self):
        return self._http_client_session

    async def DoSomeMath(self, request, context):
        x = request.x
        y = request.y
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

    async def ListAnimeByTitle(self, request, context):
        raw_resp = await self._http_client_session.get(f"https://shikimori.one/api/animes?order=popularity&kind=tv,"
                         f"movie&season=2022_2023&limit=50&search={request.title}")
        resp = await raw_resp.json()
        # print(resp)
        for anime in resp:
            # можем выдавать очередное аниме каждые 3 сек.
            await asyncio.sleep(3)
            yield my_service_pb2.Anime(
                title=anime["name"],
                score=float(anime["score"]),
                date=anime["released_on"]
            )

    async def FloodWithMessages(self, request_iterator, context):
        super().FloodWithMessages(request_iterator, context)

    async def SquareTheNumbers(self, request_iterator, context):
        for num in request_iterator:
            yield my_service_pb2.Number(x=num.x ** 2)


async def serve():
    server = grpc.aio.server()
    service = JustAnotherServiceServicer()
    my_service_pb2_grpc.add_JustAnotherServiceServicer_to_server(service, server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    logging.info(f"Запускаем gRPC сервер на {listen_addr}")
    await server.start()
    await service.get_http_client_session().close()
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
