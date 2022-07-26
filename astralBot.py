#token 5518753960:AAHMvk67B--_DUwPO8KojPRped3LLnnNBTo
#url t.me/asstralBot
import telebot;
bot = telebot.TeleBot('5518753960:AAHMvk67B--_DUwPO8KojPRped3LLnnNBTo')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text == "Привет":
		bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
	elif message.text == "/help":
		bot.send_message(message.from_user.id, "Напиши привет")
	else:
		bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
bot.polling(none_stop=True, interval=0)