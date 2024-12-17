
from sqlalchemy import create_engine
from db.models.BaseModel import BaseModel
from db.models.AccModel import AccModel
from db.models.ConfigModel import ConfigModel
from db.models.EventModel import EventModel
from db.models.ProxyModel import ProxyModel

engine = create_engine("sqlite:///mainbase.db", echo=False)

BaseModel.metadata.create_all(engine)



def get_engine():
    return engine