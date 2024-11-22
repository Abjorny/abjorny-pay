# -*- coding: utf-8 -*-
import logging
import asyncio
from aiogram import Bot, Dispatcher
from callbacks import peganator
from handlers import bot_message
import config

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TELEGRAM_BOT_TOKEN)

async def main():

    dp = Dispatcher()
    dp.include_routers(
    bot_message.router,
        peganator.router,
    )
    
    await  dp.start_polling(bot)
    
if __name__=='__main__':
    asyncio.run(main())