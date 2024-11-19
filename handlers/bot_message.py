from keyboards import  fabric
from aiogram import  Router,F
from aiogram.filters import Command
from aiogram.types import Message
import db
from utilis.utilis import FormatedText
from config import TextsList
import datetime
db = db.Database('DB.db')

router = Router()



@router.message(Command('start'))
async def send_welcome(message : Message):
    text = TextsList('start-text',
        {
            "username":message.from_user.username
        }
    )
    text = FormatedText.formatMarkdownV2(text)
    db.add_user(message.from_user.id)
    await message.answer(
        text =text,
        reply_markup=fabric.pagination(0,message.from_user.id,'menu'),
        parse_mode='MarkdownV2'

    )
@router.message(F.text & (F.text.lower() != ""))
async def send_welcome(message : Message):
    if str(message.chat.id)[0] == "-":
        users = db.get_users_with_timesub()
        for user in users:
            try:
                date_pay = user[2]
                date_format = '%m.%d.%Y'  
                parsed_date = datetime.datetime.strptime(date_pay, date_format)
                current_date = datetime.datetime.now()
                if parsed_date >= current_date:
                    await message.forward(chat_id=user[1])
                elif parsed_date < current_date:
                    db.set_user_timesub(user[1],None)
            except:
                pass