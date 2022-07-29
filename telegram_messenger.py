import requests
from controls import chat_id, bot_token

chat_id = chat_id
bot_token = bot_token

def send_message(message):
    send_text = "https://api.telegram.org/bot" + \
                bot_token + \
                "/sendMessage?chat_id=" + \
                chat_id + \
                "&parse_mode=Markdown&text=" + \
                message

    response = requests.get(send_text)

    return response.json()
