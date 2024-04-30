import schedule_job
import config as project_config

if __name__ == '__main__':
    config = project_config.load_config()
    hour = config['hour']
    minute = config['minute']

    print("准备执行定时任务...")
    print("设定的小时：", hour)
    print("设定的分钟：", minute)
    schedule_job.schedule_daily_job(hour, minute)
