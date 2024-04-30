import schedule
import time
import monitor
from datetime import datetime, timedelta, timezone


def job() -> None:
    print("开始执行定时任务执行时间：", datetime.now())
    monitor.do_monitor()


def schedule_daily_job(hour: int, minute: int) -> None:
    # 获取当前时间并转换为东八区时间
    now = datetime.now(timezone(timedelta(hours=8)))
    # 计算今天的执行时间
    today = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    # 如果当前时间已经超过了设定的时间，就将执行时间移动到第二天
    if now > today:
        today += timedelta(days=1)

    # 每天的指定时间执行任务
    schedule.every().day.at(today.strftime("%H:%M")).do(job)

    # 开始调度任务
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    schedule_daily_job(14, 44)
