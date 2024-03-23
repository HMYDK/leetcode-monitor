# Webhook地址
import json

import requests


def send(msg: str):
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=ed5117bd15d23ce4d52c77d284e6f461de874ffcd5782177da7c9cabd0d514da"

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
        r = requests.post(url=webhook, headers=header, data=message.encode("utf-8"))
        print(r.text)
    except Exception as e:
        print(e)
