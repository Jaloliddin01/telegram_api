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

# sendMessage
def send_message(chat_id, text):
    url_send = url + 'sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    if text is not None:
        requests.post(url_send, json=payload)

# echo
def echo():
    data = get_updates()
    chat_id = data['result'][-1]['message']['chat']['id']
    text = data['result'][-1]['message']['text']
    send_message(chat_id, text)


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
