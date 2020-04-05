from random import choice

from bot_instance import bot, Data, MAIN_STATE
from keyboards import kb


def choose_rang():
    n = Data["game_score"]["victories"]
    if n == 0:
        Data["game_score"]["rang"] = "лузер"
    elif n <= 5:
        Data["game_score"]["rang"] = "ученик"
    elif n <= 10:
        Data["game_score"]["rang"] = "знаток"
    elif n <= 13:
        Data["game_score"]["rang"] = "мыслитель"
    elif n <= 15:
        Data["game_score"]["rang"] = "мудрец"


def is_end(call):
    if Data["game_score"]["motions"] == 15:
        choose_rang()
        bot.send_message(call.from_user.id, "Поздравляю,прошел игру!\nТвой ранг:" + str(Data["game_score"]["rang"]))
        bot.send_message(call.from_user.id, str(choice(Data["frases"]["goodbye"])))
        Data["states"][call.from_user] = MAIN_STATE
    elif Data["game_score"]["motions"] < 15:
        bot.send_message(call.from_user.id, "Продолжаешь?", reply_markup=kb)
