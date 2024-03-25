# Webhook地址
import json

import requests

CONFIG_FILE = 'config.json'


def load_config():
    with open(CONFIG_FILE) as f:
        return json.load(f)


def send(msg: str):
    config = load_config()
    webhook_url = config['webhook_url']

    # 构造消息体
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    text_msg = {
        "msgtype": "text",
        "text": {"content": msg}
    }
    message = json.dumps(text_msg)

    # 发送请求
    try:
        r = requests.post(url=webhook_url, headers=header, data=message.encode("utf-8"))
        print(r.text)
    except Exception as e:
        print(e)
