import requests


def get_daily_sentence():
    """
    获取金山词霸每日一句

    Returns:
      str: 每日一句的内容
    """
    url = "https://open.iciba.com/dsapi"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["content"]
    else:
        raise RuntimeError("请求失败，状态码：{}".format(response.status_code))


if __name__ == "__main__":
    content = get_daily_sentence()
    print(content)
