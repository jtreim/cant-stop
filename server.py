#!/usr/bin/env python3

from aiohttp import web
import asyncio
from argparse import ArgumentParser
from datetime import datetime
import os
import socketio
import uuid

from config.settings import *
from config.events import *
from config.keys import *
from handlers import BaseHandler, GameHandler
from game import CantStop

EVENT_LOOP = asyncio.get_event_loop()


class GameServer:
    def __init__(self, verbose=False):
        self.sio = socketio.AsyncServer()
        self.app = web.Application()
        self.sio.attach(self.app)
        self.sockets = {}
        self.unregistered_sockets = []
        self.records = {}
        self.game = CantStop()
        self.verbose = verbose

        """
        Setup Handlers
        Not worrying too much about this yet. If we want to add HTML
        board displays, this is where we could do those.
        """
        # base_handler = BaseHandler()
        # game_handler = GameHander(self.game)
        # self.app.router.add_get('/', handler=base_handler.index)
        # self.app.router.add_get('/game', handler=game_handler.index)

        # Setup Socket IO
        self.init_socketio()

    def serve(self, port=PORT):
        web.run_app(self.app, port=port)

    async def send(self, event, data):
        await self.sio.emit(event, data)

    async def sendall(self, event, data):
        await self.sio.emit(event, data)

    def init_socketio(self):
        @self.sio.on(CONNECT)
        async def connect(sid, environ):
            if self.verbose:
                print('{} -- ID={} -- {}'.format(datetime.now(), sid, CONNECT))
            self.unregistered_sockets.append(sid)
            await self.send(REQUEST_REGISTER, {
                MSG: 'Please identify yourself as a player.'})

        @self.sio.on(CONNECT_ERROR)
        def connect_error(sid, data):
            if self.verbose:
                print('{} -- ID={} -- {}'.format(datetime.now(), sid, CONNECT_ERROR))
                print('\tdata={}'.format(data))

        @self.sio.on(REGISTER_PLAYER)
        async def register_player(sid, data):
            if self.verbose:
                print('{} -- ID={} -- {}'.format(datetime.now(), sid, REGISTER_PLAYER))
                print('\tdata={}'.format(data))
            if ID not in data:
                await self.send(REQUEST_REGISTER, {
                    MSG: 'Please identify yourself as a player.'})

        @self.sio.on(DISCONNECT)
        def diconnect(sid):
            if self.verbose:
                print('{} -- ID={} -- {}'.format(datetime.now(), sid, DISCONNECT))
            if sid in self.sockets:
                self.sockets.remove(sid)


if __name__ == '__main__':
    parser = ArgumentParser(description='Process server settings')
    parser.add_argument('-p', '--port', type=int,
                        required=False, help='Server port number')
    args = parser.parse_args()
    server = IOServer()

    async def on_shutdown(app):
        print('{} >>>>> Server shutdown <<<<<'.format(datetime.now()))

        await server.sendall(SERVER_SHUTDOWN, {})

        for sid in server.unregistered_sockets:
            await server.send(SERVER_SHUTDOWN, {})
            # await server.sio.disconnect(sid)
    server.app.on_shutdown.append(on_shutdown)

    if args.port:
        server.serve(port=args.port)
    else:
        server.serve()
