from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, Message, BotCommand
from environs import Env

def test(a):
    print(a)
    return "Ответ"

env = Env()
env.read_env()

bot = Bot(token=env("BOT_TOKEN"))
dp = Dispatcher()

async def set_main_menu(bot:Bot):
    main_menu_commands = [
        BotCommand(command = '/start', description = "Просто команда"),
        BotCommand(command='/help', description= 'Справка по работе')
    ]
    await bot.set_my_commands(main_menu_commands)

@dp.message(CommandStart())
async def st(message :Message):
    await message.answer(text=test(message.text))


dp.startup.register(set_main_menu)
dp.run_polling(bot)
