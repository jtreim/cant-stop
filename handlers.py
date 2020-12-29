import os

from aiohttp import web


class BaseHandler:
    def __init__(self):
        pass

    def index(self, request):
        return web.Response(text='Please connect using socket.io too.')

    async def register_player(self, request):
        pass


class GameHandler:
    def __init__(self, game):
        pass

    def index(self, request):
        return webResponse(text='This is the game index')

    async def register_player(self, request):
        pass
