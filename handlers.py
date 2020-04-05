from bot_instance import bot, Data,  COMPLEXITY_STATE, MAIN_STATE
from random import choice
from api_request import api_request
from functions import  is_end
from keyboards import kb


def main_handler(message):
    if message.text == "/start" or message.text.lower() == 'привет':
        bot.send_message(message.chat.id, str(choice(
            Data["frases"]["greeting"])) + "\nХочешь проверить свою эрудированность? Тогда напиши \"Хочу задание\"")
        Data["states"][message.from_user.id] = COMPLEXITY_STATE
    else:
        bot.send_message(message.chat.id, 'Я уже ушёл')
        Data["states"][message.from_user.id] = MAIN_STATE


def complexity_handler(message):
    if message.text.lower() == "привет" or message.text.lower() == "да" or "хочу" in message.text.lower() or "задание" in message.text.lower():
        bot.send_message(message.from_user.id, "Выбери сложность:", reply_markup=kb)
        Data["states"][message.from_user.id] = MAIN_STATE
    else:
        bot.send_message(message.from_user.id, "Я тебя не понял")
        Data["states"][message.from_user.id] = COMPLEXITY_STATE


def callback_handler(call):
    if call.data == "1":
        api_request(call, "1")

    elif call.data == "2":
        api_request(call, "2")

    elif call.data == "3":
        api_request(call, "3")

    elif call.data == "конец":
        bot.send_message(call.from_user.id,
                         "Отвеченых вопросов: " + str(
                             Data["game_score"]["victories"]) + "\nА тут ты не справился: " + str(
                             Data["game_score"]["defeats"]))
        bot.send_message(call.from_user.id, str(choice(Data["frases"]["goodbye"])))

    elif call.data == Data["helpers"]["right_answer"]:
        Data["game_score"]["motions"] += 1
        Data["game_score"]["victories"] += 1
        bot.answer_callback_query(call.id, str(choice(Data["frases"]["congratulations"])), show_alert=True)
        is_end(call)

    else:
        Data["game_score"]["motions"] += 1
        Data["game_score"]["defeats"] += 1
        bot.answer_callback_query(call.id,
                                  "К сожадению неверно. Правильный ответ: " + str(Data["helpers"]["right_answer"]),
                                  show_alert=True)
        is_end(call)
