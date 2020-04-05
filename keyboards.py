from telebot.types import InlineKeyboardMarkup as ILM
from telebot.types import InlineKeyboardButton as ILbutton

kb = ILM()
bt1 = ILbutton("Легкий\n😏", callback_data="1")
bt2 = ILbutton("Средний)\n🤔", callback_data="2")
bt3 = ILbutton("Взрыв мозга!\n🤯", callback_data="3")
bt4 = ILbutton("Закончить", callback_data="конец")
kb.add(bt1, bt2)
kb.add(bt3, bt4)

