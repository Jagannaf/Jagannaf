import telebot
from extensions import APIException, Convertor
from botconfig import TOKEN, exchange
import traceback

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = "Здравствуйте. Чтобы начать работу дайте команду боту в следующем формате: \n<имя валюты> \
<в какую валюту перевести> <количество переводимой валюты>" \
    "\n увидеть список всех доступных валют поможет команда /values"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in exchange.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    values = message.text.split(" ")
    try:
        if len(values) != 3:
            raise APIException('Слишком много параметров либо неверный ввод данных!')

        answer = Convertor.get_price(*values)
    except APIException as e:
        bot.reply_to(message, f"Ошибка в команде:\n{e}")
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(message, f"Неизвестная ошибка:\n{e}")
    else:
        bot.reply_to(message, answer)




bot.polling(none_stop=True)
