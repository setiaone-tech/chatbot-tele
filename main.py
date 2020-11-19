import telebot
import requests
import json
import wget

api = "1308184622:AAFBgBhot6tj7k-LyaSqHgbFq4XCBv9In7I"
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hai beb, mau ngajak ngobrol apa ngasih tugas nih?")

@bot.message_handler(commands=['ig'])
def send_ig(message):
    bagi = message.text
    user = bagi.split(' ')
    username = user[1]
    url = requests.get('https://mhankbarbar.herokuapp.com/api/stalk?username='+username+'&apiKey=qZOpWeYe2QqxGTQkUZ2L').json()
    bot.reply_to(message,"Username : "+url['Username']+"\nNama :"+url['Name']+"\nBio : "+url['Biodata']+"\nPengikut : "+url['Jumlah_Followers']+"\nMengikuti : "+url['Jumlah_Following'])

@bot.message_handler(commands=['wiki'])
def send_wiki(message):
    bagi = message.text
    user = bagi.split(' ')
    cari = user[1]
    url = requests.get('https://mhankbarbar.herokuapp.com/api/wiki?q='+cari+'&lang=id&apiKey=qZOpWeYe2QqxGTQkUZ2L').json()
    bot.reply_to(message, url['result'])

@bot.message_handler(commands=['hen'])
def send_hentai(message):
    chat_id = message.chat.id
    url = requests.get('https://mhankbarbar.herokuapp.com/api/random/hentai').json()
    hasil = url['result']
    bot.send_photo(chat_id, hasil)

@bot.message_handler(commands=['trap'])
def send_trap(message):
    chat_id = message.chat.id
    url = requests.get('https://mhankbarbar.herokuapp.com/api/random/trap').json()
    hasil = url['result']
    bot.send_photo(chat_id, hasil)

@bot.message_handler(commands=['prank'])
def send_prank(message):
    bagi = message.text
    nomer = bagi.split(' ')
    cari = nomer[1]
    data = {
        "number":cari
    }
    response = requests.get("https://afara.my.id/api/prank-call-greater-jakarta", data = json.dumps(data), headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Connection": "keep-alive",
        "Authorization": "Bearer EnOZgYrqJu72S55MQLU6BBwo2pHQtS"
    }).json()
    if response['result'] == 1:
        bot.reply_to(message, 'Sukses')
    else:
        bot.reply_to(message, response['message'])
        
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