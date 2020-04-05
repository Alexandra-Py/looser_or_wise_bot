from handlers import main_handler,callback_handler,complexity_handler
from bot_instance import bot, COMPLEXITY_STATE, CALLBACK_STATE, MAIN_STATE, Data



@bot.message_handler(func=lambda message: True)
def despatcher(message):
    user_id = message.from_user.id
    current_user_state = Data["states"].get(user_id,MAIN_STATE)
    if current_user_state == MAIN_STATE:
        main_handler(message)
    elif current_user_state == COMPLEXITY_STATE:
        complexity_handler(message)



@bot.callback_query_handler(func=lambda call: True)
def call_despatcher(call):
    user_id = call.from_user
    current_user_state = Data["call_states"].get(user_id,CALLBACK_STATE)
    if current_user_state == CALLBACK_STATE:
        callback_handler(call)


bot.polling()
