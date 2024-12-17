import markups
from services.forChat.UserState import UserState
from services.forChat.Response import Response
import config_controller
import sys

class OffState(UserState):
    async def start_msg(self):

        await self.bot.send_message(chat_id=self.user_chat_id, text="Перезавантажую...\n\nЩоб викликати меню напишіть /menu")
        sys.exit()