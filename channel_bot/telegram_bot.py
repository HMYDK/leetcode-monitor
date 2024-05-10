import telegram
import config as project_config

config = project_config.load_config()
telegram_bot_token = config['telegram_config']['bot_token']
bot = telegram.Bot(token=telegram_bot_token)
chat_id = config['telegram_config']['chat_id']


async def send(msg: str):
    # print(telegram_bot_token)
    # print(chat_id)
    try:
        await bot.send_message(chat_id=chat_id, text=msg)
    except telegram.error.TelegramError as e:
        print(f"Error sending message: {e}")
