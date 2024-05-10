import requests
import json


def telegram_notification(epoch, avg_test_scalars):

    CHAT_ID: int = 5082065337
    # telegram bot token
    TOKEN = "6804407144:AAHqEyUxvIFaOuu8uwBx3J--sdBzRnaqJRg"

    url = 'https://api.telegram.org/bot{}/sendMessage'.format(TOKEN)
    headers = {
        'Content-Type': 'application/json'
    }
    # main text
    text = "Epoch: {} has completed!\n".format(epoch)
    text += json.dumps(avg_test_scalars)
    # pack data
    data = {
        'chat_id': '{}'.format(CHAT_ID),
        'text': text
    }
    print(data)
    # send request
    response = requests.post(url=url, headers=headers, json=data)
    print("====")
    print(response)
    return


if __name__ == "__main__":
    telegram_notification(1, {'a': '1', 'b': '2'})
