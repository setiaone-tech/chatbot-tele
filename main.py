import telebot
import requests
import json
import datetime
import random

def log(message, perintah):
    nama_awal = message.chat.first_name
    nama_akhir = message.chat.last_name
    ttd = datetime.datetime.now().strftime('%d-%B-%Y')
    text_log = '{}, {} {}, {}\n'.format(ttd, nama_awal, nama_akhir, perintah)
    log_bot = open('log_bot.txt', 'a')
    log_bot.write(text_log)
    log_bot.close()

api = "1308184622:AAE_82J5UWi5LLsuEgSxu7nSgDiR-G7xdk4"
bot = telebot.TeleBot(api)
headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Connection": "keep-alive",
        "Authorization": "Bearer EnOZgYrqJu72S55MQLU6BBwo2pHQtS"
    }

@bot.message_handler(commands=['start'])
def send_welcome(message):
    log(message, 'start')
    bot.reply_to(message, "Hai beb, ketik /menu untuk ngeliat full command yakk")
    bot.reply_to(message, "Untuk saat ini aku blm bisa buat chat-an, lagi dikembangin sama si boss, mohon bersabar yakk beb:3")

@bot.message_handler(commands=['menu'])
def send_menu(message):
    log(message, 'menu')
    chat_id = message.chat.id
    bot.reply_to(message, "/ig : [username] = untuk nge-stalk akun ig\n/wiki : [cari] = Untuk mencari di wikipedia\n/ytm4 [link] = Untuk mendownload MP4 dari youtube\n/ytm3 [link] = Untuk mendownload MP3 dari youtube\n/prank : [no.hp] = Untuk melakukan prank telepon\n/gambar : [cari] : [banyaknya] = Untuk mencari gambar sebanyak yang diinginkan\nfilm : [cari] = Untuk mencari film dan link download-nya\n/animepict = Menampilkan gambar anime secara random\n/sholat : [daerah] = Menampilkan jadwal sholat berdasarkan daerah\n/nulis : [teks] = Untuk menulis teks secara online\n/kuso : [cari] = Untuk mencari anime dan link download-nya\n/twt : [username] = Untuk men-stalk akun twitter\n/chat : [kata] = Untuk ngobrol dengan Cindy\n/anime : [cari] = Untuk mencari anime]\n/google : [cari] = Untuk mencari dari google\n/quotes = Menampilkan quotes secara random")
    bot.send_message(chat_id, 'Ketik perintah tanpa tanda [ ], harap perhatikan command apakah menggunakan tanda ":" atau "spasi"')

@bot.message_handler(commands=['ig'])
def send_ig(message):
    chat_id = message.chat.id
    bagi = message.text
    if ':' in bagi:
        user = bagi.split(':')
        username = user[1]
        url = requests.get('https://mhankbarbar.herokuapp.com/api/stalk?username='+username+'&apiKey=qZOpWeYe2QqxGTQkUZ2L').json()
        print(url)
        if url['status'] == 200:
            bot.send_photo(chat_id, url['Profile_pic'])
            bot.send_message(chat_id, "Username : "+url['Username']+"\nNama :"+url['Name']+"\nBio : "+url['Biodata']+"\nPengikut : "+url['Jumlah_Followers']+"\nMengikuti : "+url['Jumlah_Following'])
        else:
            bot.send_message(chat_id, url['error'])
    else:
        bot.reply_to(message, 'Command Salah!')

@bot.message_handler(commands=['wiki'])
def send_wiki(message):
    bagi = message.text
    chat_id = message.chat.id
    if ':' in bagi:
        user = bagi.split(':')
        cari = user[1]
        url = requests.get('https://mhankbarbar.herokuapp.com/api/wiki?q='+cari+'&lang=id&apiKey=qZOpWeYe2QqxGTQkUZ2L').json()
        if url['status'] == 200:
            hasil = url['result'].split('===')
            n = 0
            for i in hasil:
                if n < 4:
                    n = n+1
                    bot.send_message(chat_id, i)
        else:
            bot.send_message(chat_id, url['error'])
    else:
        bot.reply_to(message, 'Command Salah!')

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
    if ':' in bagi:
        nomer = bagi.split(':')
        cari = nomer[1]
        data = {
            "number":cari
        }
        response = requests.get("https://afara.my.id/api/prank-call-greater-jakarta", data = json.dumps(data), headers = headers).json()
        if response['result'] == 1:
            bot.reply_to(message, 'Sukses Beb;)')
        else:
            bot.reply_to(message, response['message'])
    else:
        bot.reply_to(message, 'Command Salah!')

@bot.message_handler(commands=['ytm3'])
def send_ytm3(message):
    chat_id = message.chat.id
    pesan = message.text
    bagi = pesan.split(' ')
    cari = bagi[1]
    url = requests.get('https://mhankbarbar.herokuapp.com/api/yta?url='+cari+'&apiKey=qZOpWeYe2QqxGTQkUZ2L').json()
    if url['status'] == 200:
        bot.send_audio(chat_id, url['result'])
    else:
        bot.send_message(chat_id, url['error'])

@bot.message_handler(commands=['twt'])
def send_twt(message):
    chat_id = message.chat.id
    bagi = message.text
    if ':' in bagi:
        user = bagi.split(':')
        username = user[1]
        url = requests.get('https://mhankbarbar.herokuapp.com/api/twstalk?username='+username+'&apiKey=qZOpWeYe2QqxGTQkUZ2L').json()
        if url['status'] == 200:
            bot.send_photo(chat_id, url['profile_pic'])
            bot.send_message(chat_id, "ID : "+url['id']+"\nNama :"+url['full_name']+"\nJumlah Status : "+url['status_count']+"\nPengikut : "+url['followers_count'])
        else:
            bot.send_message(chat_id, url['error'])
    else:
        bot.reply_to(message, 'Command Salah!')

@bot.message_handler(commands=['kuso'])
def send_kuso(message):
    chat_id = message.chat.id
    bagi = message.text
    if ':' in bagi:
        pesan = bagi.split(':')
        cari = pesan[1]
        url = requests.get('https://mhankbarbar.herokuapp.com/api/kuso?q='+cari+'&apiKey=qZOpWeYe2QqxGTQkUZ2L').json()
        if url['status'] != 200:
            bot.send_message(chat_id, "Judul Tidak Ditemukan!")
        else:
            bot.send_photo(chat_id, url['thumb'])
            bot.send_message(chat_id, "Judul : "+url['title']+"\nSinopsis :"+url['sinopsis']+"\nInfo : "+url['info']+"\nLink : "+url['link_dl'])
    else:
        bot.reply_to(message, 'Command Salah!')

@bot.message_handler(commands=['nulis'])
def send_nulis(message):
    chat_id = message.chat.id
    pesan = message.text
    if ':' in pesan:
        bagi = pesan.split(':')
        tulis = bagi[1]
        url = requests.get('https://mhankbarbar.herokuapp.com/nulis?text='+tulis+'&apiKey=qZOpWeYe2QqxGTQkUZ2L').json()
        hasil = url['result']
        bot.send_photo(chat_id, hasil)
    else:
        bot.reply_to(message, 'Command Salah!')

@bot.message_handler(commands=['sholat'])
def send_sholat(message):
    chat_id = message.chat.id
    pesan = message.text
    if ':' in pesan:
        bagi = pesan.split(':')
        cari = bagi[1]
        url = requests.get('https://mhankbarbar.herokuapp.com/api/jadwalshalat?daerah='+cari+'&apiKey=qZOpWeYe2QqxGTQkUZ2L').json()
        bot.send_message(chat_id, 'Imsyak : '+url['Imsyak']+'\nSubuh : '+url['Subuh']+'\nDzuhur : '+url['Dzuhur']+'\nAshar : '+url['Ashar']+'\nMaghrib : '+url['Maghrib']+'\nIsya : '+url['Isya']+'\nMalam : '+url['Dhuha'])
    else:
        bot.reply_to(message, 'Command Salah!')

@bot.message_handler(commands=['animepict'])
def send_animepict(message):
    chat_id = message.chat.id
    response = requests.get("https://afara.my.id/api/anime-random-image", headers = headers).json()
    bot.send_photo(chat_id, response['image'])

@bot.message_handler(commands=['ytm4'])
def send_ytm4(message):
    chat_id = message.chat.id
    pesan = message.text
    bagi = pesan.split(' ')
    cari = bagi[1]
    data = {
    "url":cari
    }
    response = requests.get("https://afara.my.id/api/get-youtube-video-link",data = json.dumps(data),headers = headers).json()
    if response['status'] == 'success':
        bot.send_video(chat_id, response['data']['urls'][0]['url'])
    else:
        bot.send_message(chat_id, response['message'])

@bot.message_handler(commands=['film'])
def send_film(message):
    chat_id = message.chat.id
    pesan = message.text
    if ':' in pesan:
        bagi = pesan.split(':')
        cari = bagi[1]
        data = {
        "q":cari
        }
        response = requests.get("https://afara.my.id/api/cinema21-scraper", data = json.dumps(data), headers = headers).json()
        if 'error' in response:
            bot.send_message(chat_id, response['error'])
        elif 'message' in response:
            bot.send_message(chat_id, response['message'])
        else:
            for i in response:
                bot.send_message(chat_id, 'Judul : '+i['title']+'\nLink : '+i['link'])
    else:
        bot.reply_to(message, 'Command Salah!')

@bot.message_handler(commands=['gambar'])
def send_gambar(message):
    chat_id = message.chat.id
    pesan = message.text
    if ':' in pesan:
        bagi = pesan.split(':')
        cari = bagi[1]
        banyak = int(bagi[2])
        data = {
        "q":cari
        }
        response = requests.get("https://afara.my.id/api/image-scraper", data = json.dumps(data), headers = headers).json()
        for i in response:
            link = i['url']
        for j in range(0, banyak):
            bot.send_photo(chat_id, link)
    else:
        bot.reply_to(message, 'Command Salah!')

@bot.message_handler(commands=['chat'])
def chatbot(message):
    pesan = message.text
    if ':' in pesan:
        bagi = pesan.split(':')
        cari = bagi[1]
        body = {
            "text": cari
        }
        response = requests.get("https://afara.my.id/api/sim-simi", data = json.dumps(body), headers = headers ).json()
        if response['response'] == None:
            bot.reply_to(message, 'Cindy lagi tidur, tolong jangan diganggu yakk:)')
        else:
            bot.reply_to(message, response['response'])
    else:
        bot.reply_to(message, 'Command Salah!')

@bot.message_handler(commands=['quotes'])
def send_quotes(message):
    response = requests.get("https://afara.my.id/api/quote-generator", headers = headers).json()
    bot.reply_to(message, '==Quotes==\n'+response['quote'])

@bot.message_handler(commands=['google'])
def send_google(message):
    pesan = message.text
    if ':' in pesan:
        bagi = pesan.split(':')
        cari = bagi[1]
        body = {
            "q": cari
        }
        response = requests.get("https://afara.my.id/api/google-scraper", data = json.dumps(body), headers = headers).json()
        for i in response:
            bot.reply_to(message, 'Judul : '+i['title']+'\n'+'Deskripsi : '+i['description']+'\n'+'Sumber : '+i['url'])
    else:
        bot.reply_to(message, 'Command Salah!')

@bot.message_handler(commands=['anime'])
def send_anime(message):
    chat_id = message.chat.id
    pesan = message.text
    if ':' in pesan:
        bagi = pesan.split(':')
        cari = bagi[1]
        body = {
            "q": cari
        }
        response = requests.get("https://afara.my.id/api/anime-video-scraper/search", data = json.dumps(body), headers = headers).json()
        if 'error' in response:
            bot.send_message(chat_id, response['error'])
        else:
            bot.send_message(chat_id, 'Ditemukan sebanyak '+str(len(response))+' hasil pencarian.')
            for i in response:
                bot.send_message(chat_id, 'Judul :\n'+i['title']+'\nLink :\n'+i['link'])
    else:
        bot.reply_to(message, 'Command Salah!')

@bot.message_handler(commands=['igm4'])
def send_igm4(message):
    chat_id = message.chat.id
    pesan = message.text
    bagi = pesan.split(' ')
    cari = bagi[1]
    url = requests.get('https://mhankbarbar.herokuapp.com/api/ig?url='+cari+'&apiKey=qZOpWeYe2QqxGTQkUZ2L').json()
    if url['status'] == 200:
        bot.send_video(chat_id, url['result'])
    else:
        bot.send_message(chat_id, url['error'])

@bot.message_handler(commands=['igjpg'])
def send_jpg(message):
    chat_id = message.chat.id
    pesan = message.text
    bagi = pesan.split(' ')
    cari = bagi[1]
    url = requests.get('https://mhankbarbar.herokuapp.com/api/ig?url='+cari+'&apiKey=qZOpWeYe2QqxGTQkUZ2L').json()
    if url['status'] == 200:
        bot.send_photo(chat_id, url['result'])
    else:
        bot.send_message(chat_id, url['error'])

@bot.message_handler(commands=['animewp'])
def send_animewp(message):
    chat_id = message.chat.id
    lst = ['wallpaper','anime','nsfwneko']
    url = requests.get('https://mhankbarbar.herokuapp.com/api/random/'+random.choice(lst)+'?apiKey=qZOpWeYe2QqxGTQkUZ2L').json()
    if url['status'] == 200:
        hasil = url['result']
        bot.send_photo(chat_id, hasil)
    else:
        bot.send_message(chat_id, url['error'])

print('Bot Running....')
bot.polling()
