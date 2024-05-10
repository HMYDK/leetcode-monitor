import json
from datetime import datetime
import requests
import asyncio

from channel_bot import dingding_bot, telegram_bot
import iciba
import config as project_config

LEETCODE_GRAPHQL_URL = 'https://leetcode.cn/graphql/noj-go/'

HEADERS = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Origin': 'https://leetcode.cn',
    'Referer': 'https://leetcode.cn/u/{}/',
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


# 获取用户的提交日历
def get_user_submission_calendar(name: str):
    data = {
        "query": "query userProfileCalendar($userSlug: String!, $year: Int) {\n userCalendar(userSlug: $userSlug, year: $year) {\n streak\n totalActiveDays\n submissionCalendar\n activeYears\n monthlyMedals {\n name\n obtainDate\n category\n config {\n icon\n iconGif\n iconGifBackground\n }\n progress\n id\n year\n month\n }\n recentStreak\n }\n}",
        "variables": {"userSlug": name},
        "operationName": "userProfileCalendar"
    }
    response = requests.post(LEETCODE_GRAPHQL_URL, headers=HEADERS, data=json.dumps(data))
    response_json = response.json()

    submission_calendar = json.loads(response_json['data']['userCalendar']['submissionCalendar'])
    return submission_calendar


# 获取最后一次的提交日期、提交次数
def get_last_submission(submission_calendar):
    timestamps = list(submission_calendar.keys())
    last_day_timestamp = int(timestamps[-1])
    last_day_datetime = datetime.fromtimestamp(last_day_timestamp)
    last_day_date = last_day_datetime.strftime('%Y-%m-%d')
    last_day_submissions = submission_calendar[str(last_day_timestamp)]
    return last_day_date, last_day_submissions


def do_monitor():
    config = project_config.load_config()
    users = config['users']
    results = []
    for user in users:
        submission_calendar = get_user_submission_calendar(user)
        last_day_date, last_day_submissions = get_last_submission(submission_calendar)
        results.append((user, last_day_date, last_day_submissions))
    results = sorted(results, key=lambda x: x[1], reverse=True)
    output_string = ''
    output_string += iciba.get_daily_sentence()
    output_string += "\n"
    for name, last_day_date, last_day_submissions in results:
        output_string += f"{name}最后一天({last_day_date})的提交数: {last_day_submissions}\n"

    # 根据配置的不同发送消息
    channel_type = config['channel_type']
    if channel_type == 'telegram':
        asyncio.run(telegram_bot.send(output_string))
    elif channel_type == 'dingding':
        dingding_bot.send(output_string)


def main():
    do_monitor()


if __name__ == '__main__':
    main()
