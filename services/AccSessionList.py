from telethon.errors import SessionPasswordNeededError
from telethon import TelegramClient, events
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, FloodWaitError, UserDeletedError, UserInvalidError, UserDeactivatedError, UsernameInvalidError
from db.controllers.AccsController import AccsController
from db.controllers.EventsController import EventsController
from db.controllers.MsgsController import MsgsController
import config_controller
import random
import asyncio

class AccSessionList:
    def __init__(self):
        self.ses_list = {} #{"name_session": {"session": obj; "count": int}}
        self.accs_controller = AccsController()
        self.events_controller = EventsController()
        self.msgs_controller = MsgsController()

        self.path_sessions = "saved/sessions/"

    async def handle_message(self, event):
        if event.is_private:
            sender = await event.get_sender()
            sender_id = event.sender_id
            me = await event.client.get_me()
            my_id = me.id
            ses_name = event.client.session.filename.replace(".session", "").replace(self.path_sessions, "")

            print(f"[{event.client.session.filename}] Msg at {sender_id}: {event.text}")

            tmp = self.events_controller.get_by(tg_id=str(sender_id), tg_id_group=str(my_id))
            if len(tmp) > 0:
                return

            count_sec = config_controller.SECOND_FOR_UNSWER
            delay = random.randint(count_sec-(count_sec*0.2), count_sec+(count_sec*0.2))
            await asyncio.sleep(delay)

            tmp = self.events_controller.get_by(tg_id=str(sender_id), tg_id_group=str(my_id))
            if len(tmp) > 0:
                return

            tmp_msg = self.msgs_controller.get_by(acc_id=int(ses_name))
            text_send = ""
            if len(tmp_msg) == 0:
                text_send = config_controller.UNSWER_TEXT
            else:
                text_send = tmp_msg[0].msg_text

            await event.client.send_message(sender_id, text_send)
            self.events_controller.create(acc_id=1,
                                          name_type="msg",
                                          tg_id=str(sender_id),
                                          tg_id_group=str(my_id))

    async def start_session(self, phone: str):
        print("Start session", phone)
        tmp = self.accs_controller.get_by(phone=phone, is_active=True)
        if len(tmp) == 0:
            return False
        acc = tmp[0]
        if acc.proxy_id == None:
            self.ses_list[phone] = {"session": TelegramClient(session=self.path_sessions+acc.session_name,
                                                             api_id=acc.api_id,
                                                             api_hash=acc.api_hash),
                                   "count": 0}
        else:
            self.ses_list[phone] = {"session": TelegramClient(session=self.path_sessions+acc.session_name,
                                                             api_id=acc.api_id,
                                                             api_hash=acc.api_hash,
                                                             proxy=(
                                                                 acc.proxy.type_proxy,
                                                                 acc.proxy.ip,
                                                                 acc.proxy.port,
                                                                 True,
                                                                 acc.proxy.login,
                                                                 acc.proxy.password
                                                             )),
                                   "count": 0}
        self.ses_list[phone]["session"].add_event_handler(self.handle_message, events.NewMessage)
        await self.ses_list[phone]["session"].connect()
        return True

    async def end_session(self, phone:str):
        acc = self.ses_list.get(phone, None)
        if acc == None:
            return False
        await acc["session"].disconnect()
        self.ses_list.pop(phone)
        return True

    async def get_session(self, phone:str):
        acc = self.ses_list.get(phone, None)
        if acc == None:
            res = await self.start_session(phone)
            if res:
                self.ses_list[phone]["count"] += 1
                return self.ses_list[phone]["session"]
            else:
                raise Exception("Session dont start")
        else:
            self.ses_list[phone]["count"] += 1
            return self.ses_list[phone]["session"]

    async def give_away_session(self, phone:str):
        acc = self.ses_list.get(phone, None)
        if acc == None:
            return False
        self.ses_list[phone]["count"] -= 1
        if self.ses_list[phone]["count"] <= 0:
            await self.end_session(phone)
        return True


session_list = AccSessionList()