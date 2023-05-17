import telebot;
from aiget import sendQuestion;
token="6041454646:AAHukeZBNmyX22AM6gTHjF67MzGilNJfxxg"
bot = telebot.TeleBot(token);
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "/help":
      bot.send_message(message.from_user.id, "Напиши мне сообщение, а я запрошу помощи исскуственного интилекта")
  else:
      bot.send_message(message.from_user.id, "Направляю вопрос...")
      anwser = sendQuestion(message.text)
      bot.send_message(message.from_user.id, anwser)
          

bot.polling(none_stop=True, interval=0)



