import logging
from aiogram import Bot, Dispatcher, types, html  
from dotenv import load_dotenv
import os
from aiogram.filters import CommandStart
import asyncio
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import sys
from aiogram.types import Message

load_dotenv()
# TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# print(TELEGRAM_BOT_TOKEN)

# configure logging
logging.basicConfig(level=logging.INFO)

# initialize bot and dispatcher
# bot = Bot(token = TELEGRAM_BOT_TOKEN)
# dp = Dispatcher(bot)


dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


# @dp.message_
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())



    # 06:30: 00