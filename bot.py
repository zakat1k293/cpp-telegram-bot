from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import aiohttp
import asyncio

TOKEN = "ВАШ_ТОКЕН_ОТ_BOTFATHER"  # <-- замени на свой токен

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def get_waifu_url():
    url = "https://api.waifu.pics/sfw/waifu"  # безопасные аниме тянки
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                return data.get("url")
            else:
                return None

@dp.message(Command("тян"))
async def send_anime_girl(message: types.Message):
    photo_url = await get_waifu_url()
    if photo_url:
        await message.answer_photo(photo_url, caption="Вот твоя аниме тянка 💖")
    else:
        await message.answer("Не получилось загрузить тянку, попробуй позже 😔")

async def main():
    try:
        print("Бот стартует...")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
