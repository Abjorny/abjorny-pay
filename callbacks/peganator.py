# -*- coding: utf-8 -*-

from aiogram import Router
from aiogram.utils.keyboard import CallbackData
from aiogram.fsm.state import  State,StatesGroup
from aiogram.fsm.context import  FSMContext
from aiogram.types import CallbackQuery

from utilis.utilis import FormatedText
from keyboards import fabric
from main import Bot
from config import TextsList
import db
import cryptobot
from datetime import datetime,timedelta



router = Router()
db = db.Database('DB.db')

class Pagination(CallbackData, prefix='pag'):
    action: str
    page: int
    last : str
    data : str

async def add_months(date_obj, months):
    month = date_obj.month - 1 + months
    year = date_obj.year + month // 12
    month = month % 12 + 1
    day = min(date_obj.day, [31, 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1])
    return datetime(year, month, day)


@router.callback_query(Pagination.filter())
async def pagination_handler(call: CallbackQuery, callback_data: Pagination,state: FSMContext,bot:Bot):
    user_data = {
        "user_id":call.message.chat.id,
        "username":call.message.chat.username,
        "firstName":call.message.chat.first_name
    }
    action = callback_data.action
    text = ""
    page = 0
    last = ''
    date = []
    if action == "menu":
        text = TextsList('start-text',user_data)
        page = 0
        last ="menu"
        
    elif action == "profile":
        user = db.get_user_userid(call.message.chat.id)
        text = f"*Это ваш профиль:\nUsername : {call.message.chat.username}\nUserid : {call.message.chat.id}\nSubscribe : {"Haven't" if user[2] is None else user[2]}*"
        page = 2
        last = "menu"
    elif action == "buy_subscribe":
        text= "*Выберите метот платежа.*"
        page = 3
        last = "profile"
    elif action == "crypto":
        text= "*Выберите криптовалюту, которой хотите оплатить.*"
        page = 4
        last = "buy_subscribe"
        date = await cryptobot.get_available_currencies()
    elif action == "crypto_accept":
        text="*Пожалуйста оплатите платеж по кнопке ниже, после нажмите 'Я оплатил'*"
        page = 5
        data_st =  await cryptobot.create_payment(callback_data.data,100)
        date = [data_st['payment_url'],data_st['payment_id']]
        last = "crypto"
    elif action == "crypto_ok":
        id_pay =callback_data.data
        status_pay,pay_url = await cryptobot.get_payment_status(id_pay)
        if status_pay == "paid":
            current_date = datetime.now()
            new_date = await add_months(current_date, 1)
            formatted_date = new_date.strftime("%m.%d.%Y")
            db.set_user_timesub(call.message.chat.id,formatted_date)
            text =f"*Оплата прошла успешно!\nУ вас подписка получена до {formatted_date}*"
            page =1
            last = "profile"
        else:
            text = "*Оплата не найдена!\nПожалуйста убедитесь, что вы произвели оплату и повторите попытку нажав на кнопку - 'я оплатил'*"
            page = 5
            last = "profile"
            date =[pay_url,id_pay]
            


    text = FormatedText.formatMarkdownV2(text)
    try:
        mes=  await call.message.edit_text(text,reply_markup=fabric.pagination(page,user_data.get("user_id",1),last,date),parse_mode='MarkdownV2')
        await state.update_data(lastid = mes.message_id)
    except:
        pass



