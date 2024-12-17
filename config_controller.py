import pickle
import os
from db.controllers.ConfigsController import ConfigsController
controller = ConfigsController()
PASSWORD_ADMIN = "admin"
UNSWER_TEXT = "Test Text"
SECOND_FOR_UNSWER = 60

API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')

list_is_loggin_admins = []

def preload_config():
    if controller.get_config(name="config").binary_data != None:
        read_ini()
    else:
        write_ini()
def write_ini():
    config = {}
    config["PASSWORD_ADMIN"] = PASSWORD_ADMIN
    config["UNSWER_TEXT"] = UNSWER_TEXT
    config["SECOND_FOR_UNSWER"] = SECOND_FOR_UNSWER
    config["list_is_loggin_admins"] = list_is_loggin_admins
    controller.set_config(name="config",
                          binary_data=pickle.dumps(config))


def read_ini():
    global PASSWORD_ADMIN, UNSWER_TEXT, SECOND_FOR_UNSWER, list_is_loggin_admins
    config = pickle.loads(controller.get_config(name="config").binary_data)
    PASSWORD_ADMIN = str(config["PASSWORD_ADMIN"])
    UNSWER_TEXT = str(config["UNSWER_TEXT"])
    SECOND_FOR_UNSWER = int(config["SECOND_FOR_UNSWER"])
    list_is_loggin_admins = config["list_is_loggin_admins"]

def log(chat_id, password):
    global list_is_loggin_admins
    if password == PASSWORD_ADMIN and (not chat_id in list_is_loggin_admins):
        list_is_loggin_admins.append(chat_id)
        write_ini()
        return True
    elif chat_id in list_is_loggin_admins:
        return True
    return False

def change_password_admin(chat_id, password):
    global PASSWORD_ADMIN, list_is_loggin_admins
    if chat_id in list_is_loggin_admins:
        PASSWORD_ADMIN = password
        write_ini()
        list_is_loggin_admins = []
        write_ini()
        return True
    else:
        return False