from telebot import types
import db.database as db
import config_controller
from db.models.AccModel import AccModel
from db.models.ProxyModel import ProxyModel
from typing import List


def generate_yes_no():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton(text="✅Так✅", callback_data="/yes"))
    markup.add(types.InlineKeyboardButton(text="❌Відмінити❌", callback_data="/cancel"))
    return markup

def generate_ready_exit():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton(text="✅Готово✅", callback_data="/yes_ready"))
    markup.add(types.InlineKeyboardButton(text="❌Відмінити❌", callback_data="/cancel"))
    return markup

def generate_delete_cancel():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton(text="🗑Видалити🗑", callback_data="/delete"))
    markup.add(types.InlineKeyboardButton(text="❌Відмінити❌", callback_data="/cancel"))
    return markup

def generate_delete_cancel_msg():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton(text="❇️Змінити текст повідомлення❇️", callback_data="/msg_edit"))
    markup.add(types.InlineKeyboardButton(text="🗑Видалити🗑", callback_data="/delete"))
    markup.add(types.InlineKeyboardButton(text="❌Відмінити❌", callback_data="/cancel"))
    return markup


def generate_list_acc(accs: List[AccModel], page = False):
    markup = types.InlineKeyboardMarkup(row_width=2)
    for i in accs:
        markup.add(types.InlineKeyboardButton(text=i.name+"["+i.phone+"]", callback_data=i.phone))
    if page:
        markup.add(types.InlineKeyboardButton(text="➡️️", callback_data="/next"))
        markup.add(types.InlineKeyboardButton(text="⬅️", callback_data="/back"))
    markup.add(types.InlineKeyboardButton(text="❇️Додати❇️", callback_data="/add"))
    markup.add(types.InlineKeyboardButton(text="❌Відмінити❌", callback_data="/cancel"))
    return markup

def generate_list_proxy(proxys: List[ProxyModel], page = False):
    markup = types.InlineKeyboardMarkup(row_width=2)
    for i in proxys:
        markup.add(types.InlineKeyboardButton(text=i.ip+":"+str(i.port), callback_data=i.id))
    if page:
        markup.add(types.InlineKeyboardButton(text="➡️️", callback_data="/next"))
        markup.add(types.InlineKeyboardButton(text="⬅️", callback_data="/back"))
    markup.add(types.InlineKeyboardButton(text="❇️Додати❇️", callback_data="/add"))
    markup.add(types.InlineKeyboardButton(text="❌Відмінити❌", callback_data="/cancel"))
    return markup

def generate_proxy():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton(text="🗑Видалити🗑", callback_data="/delete"))
    markup.add(types.InlineKeyboardButton(text="❌Відмінити❌", callback_data="/cancel"))
    return markup

def generate_groupswords():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton(text="❇️Додати коментарі❇️", callback_data="/addc"))
    markup.add(types.InlineKeyboardButton(text="🗑Видалити🗑", callback_data="/delete"))
    markup.add(types.InlineKeyboardButton(text="❌Відмінити❌", callback_data="/cancel"))
    return markup

def generate_cancel():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton(text="❌Відмінити❌", callback_data="/cancel"))
    return markup

def generate_markup_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton(text="Список акаунтів", callback_data="/accs"))
    markup.add(types.InlineKeyboardButton(text="Список проксі", callback_data="/proxys"))
    markup.add(types.InlineKeyboardButton(text="Змінити текст відповіді", callback_data="/unswer"))
    markup.add(types.InlineKeyboardButton(text="Змінити затримку відповіді", callback_data="/second"))

    markup.add(types.InlineKeyboardButton(text="Змінити пароль адміна", callback_data="/passwordadmin"))
    markup.add(types.InlineKeyboardButton(text="Перезавантажити", callback_data="/reload"))

    return markup