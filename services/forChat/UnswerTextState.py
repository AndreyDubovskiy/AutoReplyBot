import markups
from services.forChat.UserState import UserState
from services.forChat.Response import Response
import config_controller

class UnswerTextState(UserState):
    async def start_msg(self):
        self.edit = "unswer_text"
        return Response(text=f"Введіть новий текст повідомлення-відповіді:", buttons=markups.generate_cancel())


    async def next_msg(self, message: str):
        if self.edit == "unswer_text":
            if len(message) > 4096:
                return Response(text="Ви ввели забагато символів! (максимум 4096 символи)\n\nСпробуйте ще раз:", buttons=markups.generate_cancel())
            config_controller.UNSWER_TEXT = message
            config_controller.write_ini()
            return Response(text="Текст повідомлення-відповіді змінено!", is_end=True, redirect="/menu")

    async def next_btn_clk(self, data_btn: str):
        if data_btn == "/cancel":
            return Response(redirect="/menu")
