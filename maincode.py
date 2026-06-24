import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "8742676991:AAEtgyTXniDS3ScVg7S70YzfgfHxoSCNTb0"
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(msg: types.Message):
    await msg.answer("Hello! Its my first telegram bot!")
   
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())