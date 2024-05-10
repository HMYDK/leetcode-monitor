import requests

if __name__ == '__main__':
    # 指定网址
    url = "https://api.telegram.org/bot6804407144:AAHqEyUxvIFaOuu8uwBx3J--sdBzRnaqJRg/getUpdates"

    # 发送GET请求
    response = requests.get(url)

    # 检查请求是否成功
    if response.status_code == 200:
        # 打印响应内容
        print(response.text)
    else:
        print(f"请求失败,状态码: {response.status_code}")
