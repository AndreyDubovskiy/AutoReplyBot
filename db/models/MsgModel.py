from db.models.BaseModel import BaseModel
from db.models.imports import *

class MsgModel(BaseModel):
    __tablename__ = 'msgs'

    id: Mapped[int] = mapped_column(primary_key=True)
    acc_id: Mapped[int] = mapped_column(Integer())
    msg_text: Mapped[str] = mapped_column(String())


    def __init__(self,acc_id:int, msg_text: str):
        self.acc_id = acc_id
        self.msg_text = msg_text
