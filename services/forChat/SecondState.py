import markups
from services.forChat.UserState import UserState
from services.forChat.Response import Response
import config_controller

class SecondState(UserState):
    async def start_msg(self):
        self.edit = "second"
        return Response(text=f"Введіть затримку перед відповіддю (в секундах):", buttons=markups.generate_cancel())


    async def next_msg(self, message: str):
        if self.edit == "second":
            try:
                if int(message) <= 0:
                    return Response(text="Затримка не може бути меншою або дорівнювати нулю! Спробуйте ще раз:", buttons=markups.generate_cancel())
                config_controller.SECOND_FOR_UNSWER = int(message)
                config_controller.write_ini()
                return Response(text="Затримка змінена!", is_end=True, redirect="/menu")
            except Exception as ex:
                return Response(text="Ви впевнені що ввели все коректно? Спробуйте ще раз:", buttons=markups.generate_cancel())

    async def next_btn_clk(self, data_btn: str):
        if data_btn == "/cancel":
            return Response(redirect="/menu")
