from db.controllers.AccsController import AccsController
from db.controllers.ProxysController import ProxysController
from db.controllers.EventsController import EventsController
import services.AccSessionList as session_list
import asyncio


class AccWaitController:
    def __init__(self):
        self.accs = AccsController()
        self.proxys = ProxysController()
        self.events = EventsController()
        self.phones = []
        self.clients = []
        self.tastks = []

    async def preload_clients(self):
        self.clients = []
        self.tastks = []
        self.phones = []
        tmp = self.accs.get_by(is_active=True)
        for i in tmp:
            tt = await session_list.session_list.get_session(i.phone)
            self.phones.append(i.phone)
            self.clients.append(tt)

    async def start_all(self):
        try:
            await self.preload_clients()
            for i in self.clients:
                task = asyncio.create_task(i.run_until_disconnected())
                self.tastks.append(task)
            await asyncio.gather(*self.tastks)
        except asyncio.CancelledError as ex:
            print(ex)

    async def stop_all(self):
        for i in self.tastks:
            i.cancel()
        for i in self.phones:
            await session_list.session_list.give_away_session(i)

