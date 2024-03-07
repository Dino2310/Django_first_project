# pip install -U aiogram
# pip install environs


import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import other_handlers, user_hendlers

async def main():
    config : Config = load_config()

    bot = Bot(token= config.tg_bot.token)
    dp = Dispatcher()


    dp.include_router(user_hendlers.router)
    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates= True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())