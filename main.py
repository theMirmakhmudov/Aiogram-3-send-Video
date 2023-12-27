import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from config import Token
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile

TOKEN = Token
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message(Command("video"))
async def cmd_video(message: Message) -> None:
    file_ids = []

    with open("#nocomment.mp4", "rb") as video_from_buffer:
        result = await message.answer_video(
            BufferedInputFile(
                video_from_buffer.read(),
                filename="#nocomment.mp4"
            ))

        file_ids.append(result.video[-1].file_id)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
