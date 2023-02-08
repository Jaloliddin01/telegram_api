import requests
import json
import time

TOKEN = '6191178599:AAGh5qxNbT2bgkYe_LnDvBIxaRcF6SM4mng'
url = f'https://api.telegram.org/bot{TOKEN}/'

# getUpdates
def get_updates():
    url_get = url + 'getUpdates'
    r = requests.get(url_get)
    return json.loads(r.content)

# forwardMessage
def forward_message(chat_id, from_chat_id, message_id):
    url_forward = url + 'forwardMessage'
    data = {'chat_id': chat_id, 'from_chat_id': from_chat_id, 'message_id': message_id, 'protect_content': True}
    r = requests.post(url_forward, data=data)
    return json.loads(r.content)

# sendMessage
def send_message(chat_id, text):
    url_send = url + 'sendMessage'
    data = {'chat_id': chat_id, 'text': text}
    r = requests.post(url_send, data=data)
    print(r.headers)
    return json.loads(r.content)

# sendPhoto
def send_photo(chat_id, photo):
    url_send = url + 'sendPhoto'
    data = {'chat_id': chat_id, 'photo': photo}
    r = requests.post(url_send, data=data)
    return json.loads(r.content)

# sendVideo
def send_video(chat_id, video):
    url_send = url + 'sendVideo'
    data = {'chat_id': chat_id, 'video': video}
    r = requests.post(url_send, data=data)
    return json.loads(r.content)

# sendAudio
def send_audio(chat_id, audio):
    url_send = url + 'sendAudio'
    data = {'chat_id': chat_id, 'audio': audio}
    r = requests.post(url_send, data=data)
    return json.loads(r.content)

# sendDocument
def send_document(chat_id, document):
    url_send = url + 'sendDocument'
    data = {'chat_id': chat_id, 'document': document}
    r = requests.post(url_send, data=data)
    return json.loads(r.content)

# sendVoice
def send_voice(chat_id, voice):
    url_send = url + 'sendVoice'
    data = {'chat_id': chat_id, 'voice': voice}
    r = requests.post(url_send, data=data)
    return json.loads(r.content)

# sendSticker
def send_sticker(chat_id, sticker):
    url_send = url + 'sendSticker'
    data = {'chat_id': chat_id, 'sticker': sticker}
    r = requests.post(url_send, data=data)
    return json.loads(r.content)

# sendContact
def send_contact(chat_id, phone_number, first_name, last_name):
    url_send = url + 'sendContact'
    data = {'chat_id': chat_id, 'phone_number': phone_number, 'first_name': first_name, 'last_name': last_name}
    r = requests.post(url_send, data=data)
    return json.loads(r.content)

# sendLocation
def send_location(chat_id, latitude, longitude):
    url_send = url + 'sendLocation'
    data = {'chat_id': chat_id, 'latitude': latitude, 'longitude': longitude}
    r = requests.post(url_send, data=data)
    return json.loads(r.content)
   

# echo
def echo():

    data = get_updates()
    # chat_id = data['result'][-1]['message']['chat']['id']
    # message_id = data['result'][-1]['message']['message_id']
    if 'text' in data['result'][-1]['message']:
        text = data['result'][-1]['message']['text']
    else:
        text = 'content is not a text'
    # first_name = data['result'][-1]['message']['chat']['first_name']
    # last_name = data['result'][-1]['message']['chat']['last_name']
    # username = data['result'][-1]['message']['chat']['username']
    # date = data['result'][-1]['message']['date']
    # print(f'chat_id: {chat_id}')
    # print(f'message_id: {message_id}')
    print(f'text: {text}')
    # print(f'first_name: {first_name}')
    # print(f'last_name: {last_name}')
    # print(f'username: {username}')
    # print(f'date: {date}')


# main
def main():
    last_update_id = get_updates()['result'][-1]['update_id']
    while True:
        current_update_id = get_updates()['result'][-1]['update_id']
        if last_update_id != current_update_id:
            last_update_id = current_update_id
            echo()
        time.sleep(2)

if __name__ == '__main__':
    main()
