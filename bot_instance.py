import telebot
import os
import redis


token = os.environ["TELEGRAM_TOKEN"]
bot = telebot.TeleBot(token)


REDIS_URL=os.environ.get("REDIS_URL")
dict_db={}


def save(key,value):
     if REDIS_URL:
         redis_db = redis.from_url(REDIS_URL)
         redis_db.set(key,value)
     else:
         dict_db[key]=value


def load(key):
    if REDIS_URL:
        redis_db = redis.from_url(REDIS_URL)
        return redis_db.get(key)
    else:
        return dict_db.get(key,default="main")

Data = {"game_score": {"victories": 0, 'defeats': 0, "motions": 0},
        "frases": {
            "greeting": ["Здравствуй)", "Привет!", "Хэллоу!", "Ну,привет."],
            "goodbye": ["Пока", "До встречи", "Пока, пиши еще:)", "Хорошего дня", "Гуд бай", "Счастливо", "Досвидос",
                        "Приходи еще играть"],
            "congratulations": ["Супер! Ты угадал)", "Ты крут!", "Так держать!", "Вот это смекалка) Правильно!",
                                "Это правильный ответ!"]
        },
        "helpers": {}
        }

MAIN_STATE = "main"
COMPLEXITY_STATE = "complexity"
CALLBACK_STATE = "callback"