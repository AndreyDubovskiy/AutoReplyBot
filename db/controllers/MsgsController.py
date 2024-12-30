from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy import select
from typing import List
from sqlalchemy.orm import joinedload
from db.controllers.TemplateController import Controller
from db.models.MsgModel import MsgModel

class MsgsController(Controller):
    def get_all(self):
        with Session(self.engine) as session:
            query = select(MsgModel)
            res: List[MsgModel] = session.scalars(query).all()
        return res

    def get_by(self, id = None, acc_id = None, msg_text = None, offset = None, limit = None):
        with Session(self.engine) as session:
            query = select(MsgModel)
            if id != None:
                query = query.where(MsgModel.id == id)
            if acc_id != None:
                query = query.where(MsgModel.acc_id == acc_id)
            if msg_text != None:
                query = query.where(MsgModel.msg_text == msg_text)
            if offset != None:
                query = query.offset(offset)
            if limit != None:
                query = query.limit(limit)
            res: List[MsgModel] = session.scalars(query).all()
        return res

    def create(self, acc_id: int, msg_text: str):
        with Session(self.engine) as session:
            tmp = MsgModel(acc_id, msg_text)
            session.add(tmp)
            session.commit()
            session.refresh(tmp)
        return tmp

    def delete(self, id):
        with Session(self.engine) as session:
            query = select(MsgModel).where(MsgModel.id == id)
            tmp: MsgModel = session.scalars(query).first()
            session.delete(tmp)
            session.commit()
        return tmp