import requests
import json
import time

TOKEN = '6199899958:AAFqup1isw2HYkcwMIpL4Bb5I68o1EGO8FA'
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
    

# echo
def echo():
    data = get_updates()
    chat_id = data['result'][-1]['message']['chat']['id']
    from_chat_id = data['result'][-1]['message']['from']['id']
    message_id = data['result'][-1]['message']['message_id']
    # if data['result'][-1]['message']['text']:
    #     ans = data['result'][-1]['message']['text']
    # elif data['result'][-1]['message']['photo']:
    #     ans = data['result'][-1]['message']['photo']
    # elif data['result'][-1]['message']['video']:
    #     ans = data['result'][-1]['message']['video']
    # elif data['result'][-1]['message']['audio']:
    #     ans = data['result'][-1]['message']['audio']
    # elif data['result'][-1]['message']['document']:
    #     ans = data['result'][-1]['message']['document']
    # elif data['result'][-1]['message']['voice']:
    #     ans = data['result'][-1]['message']['voice']
    # elif data['result'][-1]['message']['sticker']:
    #     ans = data['result'][-1]['message']['sticker']
    # elif data['result'][-1]['message']['contact']:
    #     ans = data['result'][-1]['message']['contact']
    # elif data['result'][-1]['message']['location']:
    #     ans = data['result'][-1]['message']['location']
    # else:
    #     ans = '' #nothing
    forward_message(chat_id, from_chat_id, message_id)


# main
def main():
    last_update_id = get_updates()['result'][-1]['update_id']
    while True:
        current_update_id = get_updates()['result'][-1]['update_id']
        if last_update_id != current_update_id:
            last_update_id = current_update_id
            echo()
        time.sleep(1)

if __name__ == '__main__':
    main()
