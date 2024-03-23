import json
from datetime import datetime
import requests


def do_query(name: str):
    url = 'https://leetcode.cn/graphql/noj-go/'
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Origin': 'https://leetcode.cn',
        'Referer': 'https://leetcode.cn/u/' + name + '/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'authorization': ';',
        'content-type': 'application/json',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"'
    }
    data = {
        "query": "query userProfileCalendar($userSlug: String!, $year: Int) {\n userCalendar(userSlug: $userSlug, year: $year) {\n streak\n totalActiveDays\n submissionCalendar\n activeYears\n monthlyMedals {\n name\n obtainDate\n category\n config {\n icon\n iconGif\n iconGifBackground\n }\n progress\n id\n year\n month\n }\n recentStreak\n }\n}",
        "variables": {"userSlug": name},
        "operationName": "userProfileCalendar"
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = response.json()

    # 反序列化submissionCalendar字符串为Python字典
    submission_calendar = json.loads(response_json['data']['userCalendar']['submissionCalendar'])

    # 获取字典中的所有键(时间戳)
    timestamps = list(submission_calendar.keys())

    # 最后一个时间戳即为最后一天
    last_day_timestamp = int(timestamps[-1])

    # 将时间戳转换为datetime对象
    last_day_datetime = datetime.fromtimestamp(last_day_timestamp)

    # 格式化日期为年-月-日
    last_day_date = last_day_datetime.strftime('%Y-%m-%d')

    # 获取该日期对应的提交数
    last_day_submissions = submission_calendar[str(last_day_timestamp)]

    return name, last_day_date, last_day_submissions


if __name__ == '__main__':
    users = ['dijia-light', 'oddcc']
    results = []
    for user in users:
        result = do_query(user)
        results.append(result)

    for name, last_day_date, last_day_submissions in results:
        print(f"{name}最后一天({last_day_date})的提交数: {last_day_submissions}")
