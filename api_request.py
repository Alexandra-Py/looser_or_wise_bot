import random

import requests
from telebot.types import InlineKeyboardButton as ILbutton
from telebot.types import InlineKeyboardMarkup as ILM

from bot_instance import bot, Data


def api_request(call, complexity):
    api_url = "https://stepik.akentev.com/api/millionaire"
    data = requests.get(api_url, params={
        "complexity": complexity
    }).json()
    Data["helpers"]["right_answer"] = data["answers"][0]
    random.shuffle(data["answers"])
    Data["helpers"]["answers"] = data["answers"]
    bot.send_message(call.message.chat.id, str(data["question"]) + "\n" + "a)" + Data["helpers"]["answers"][0] +
                     "\nb)" + Data["helpers"]["answers"][1] + "\nc)" + Data["helpers"]["answers"][2] + "\nd)" +
                     Data["helpers"]["answers"][3])
    kb2 = ILM()
    bt1 = ILbutton("a", callback_data=Data["helpers"]["answers"][0])
    bt2 = ILbutton("b", callback_data=Data["helpers"]["answers"][1])
    bt3 = ILbutton("c", callback_data=Data["helpers"]["answers"][2])
    bt4 = ILbutton("d", callback_data=Data["helpers"]["answers"][3])
    kb2.add(bt1, bt2)
    kb2.add(bt3, bt4)
    bot.send_message(call.message.chat.id, "Выбери вариант:", reply_markup=kb2)
