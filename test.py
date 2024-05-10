import asyncio

from telegram import Bot
import config as project_config

config = project_config.load_config()
telegram_bot_token = config['telegram_bot_token']
print(telegram_bot_token)
bot = Bot(token=telegram_bot_token)


async def main():
    """Sends a message to a Telegram chat."""
    chat_id = 5082065337
    text = '你好，世界！'

    await bot.send_message(chat_id=chat_id, text=text, connect_timeout=30)


if __name__ == '__main__':
    asyncio.run(main())
