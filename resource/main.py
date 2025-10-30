# import logging
# from aiogram import Bot, Dispatcher, types, html  
# from dotenv import load_dotenv
# import os
# from aiogram.filters import CommandStart
# import asyncio
# from aiogram.client.default import DefaultBotProperties
# from aiogram.enums import ParseMode
# import sys
# from aiogram.types import Message
# import openai




# load_dotenv()
# TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# openai.api_key = os.getenv("OPENAI_API_KEY")
# TOKEN = TELEGRAM_BOT_TOKEN


# class Reference:
#     """
#         The class to store previously response from the openai API
#     """
#     def __init__(self) -> None:
#         self.reference = ""

# reference = Reference()
# model_name = "gpt-3.5-turbo"


# # Initialize bot and dispatcher
# dp = Dispatcher() 

# @dp.message(CommandStart())
# async def command_start_handler(message: Message) -> None:
#     """
#     This handler receives messages with `/start` command
#     """
#     await message.answer(f"Hello\n I am Tele Bot!\Created by Livingston. How can i assist you")





# async def main() -> None:
#     # Initialize Bot instance with default bot properties which will be passed to all API calls
#     bot = Bot(token=TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

#     # And the run events dispatching
#     await dp.start_polling(bot)





# @dp.message()
# async def chatgpt(message: types.Message):
#     """
#             A handler to process the user's input and generate a response using ChatGPT API.
#     """
#     print(f">>> User input: {message.text}")
#     response = openai.ChatCompletion.create(
#     model= model_name,
#     messages=[
#         {
#             "role": "system", "content": reference.response
#         },

#         {"role": "user", "content": message.text}
#         ]
#     )


#     reference.response = response.choices[0].message.content
#     print(f">>> ChatGPT response: {reference.response}")
#     await bot.send_message(chat_id = message.chat.id, text= reference.response)


# if __name__ == "__main__":
#     asyncio.run(main())




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
from openai import OpenAI





load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TOKEN = TELEGRAM_BOT_TOKEN
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class Reference:
    """
        The class to store previously response from the openai API
    """
    def __init__(self) -> None:
        self.response = ""

reference = Reference()
model_name = "gpt-3.5-turbo"


# Initialize bot and dispatcher
dp = Dispatcher() 

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello\n I am Tele Bot!\Created by Livingston. How can i assist you")





async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)





@dp.message()
async def chatgpt(message: types.Message):
    """
            A handler to process the user's input and generate a response using ChatGPT API.
    """
    print(f">>> User input: {message.text}")
    response = client.chat.completions.create(model= model_name,
    messages=[
        {
            "role": "system", "content": reference.response
        },
    
        {"role": "user", "content": message.text}
        ])


    reference.response = response.choices[0].message.content
    print(f">>> ChatGPT response: {reference.response}")
    await bot.send_message(chat_id = message.chat.id, text= reference.response)


if __name__ == "__main__":
    asyncio.run(main())



