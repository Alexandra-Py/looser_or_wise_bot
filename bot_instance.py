import telebot
import os


token = os.environ["TELEGRAM_TOKEN"]
bot = telebot.TeleBot(token)





Data = {"game_score": {"victories": 0, 'defeats': 0, "motions": 0},
        "frases": {
            "greeting": ["Здравствуй)", "Привет!", "Хэллоу!", "Ну,привет."],
            "goodbye": ["Пока", "До встречи", "Пока, пиши еще:)", "Хорошего дня", "Гуд бай", "Счастливо", "Досвидос",
                        "Приходи еще играть"],
            "congratulations": ["Супер! Ты угадал)", "Ты крут!", "Так держать!", "Вот это смекалка) Правильно!",
                                "Это правильный ответ!"]
        },
        "states" : {},
        "call_states" : {},
        "helpers": {}
        }

MAIN_STATE = "main"
COMPLEXITY_STATE = "complexity"
CALLBACK_STATE = "callback"