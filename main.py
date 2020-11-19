import telebot
import requests
import json

api = "1220919806:AAGD4zn3oSYfwZiNaQQrjyOr1p63HXSdM-s"
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Eh kamu, apa kabar?")

@bot.message_handler()
def chatbot(message):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Connection": "keep-alive",
        "Authorization": "Bearer EnOZgYrqJu72S55MQLU6BBwo2pHQtS"
    }
    body = {
        "text": message.text
    }
    response = requests.get("https://afara.my.id/api/sim-simi", data = json.dumps(body), headers = headers ).json()
    bot.reply_to(message, response['response'])


bot.polling()