

from aiogram.utils.keyboard import InlineKeyboardBuilder

def pagination(page: int=0,id: int=1,last:str='',elem: list=None):
    
    from callbacks.peganator import Pagination
    build = InlineKeyboardBuilder()

    if page == 0:

        build.button(
            text = "Профиль",
            callback_data=Pagination(action="profile", page=page, last=last, data='')
        )
        build.adjust(1)
    elif page == 1:
        build.button(
            text="◀назад",
            callback_data=Pagination(action=last, page=page, last=last, data='')
        )
        build.adjust(1) 
    elif page == 2:
        build.button(
            text="Купить подписку",
            callback_data=Pagination(action="buy_subscribe", page=page, last=last, data='')
        )
        build.button(
            text="◀назад",
            callback_data=Pagination(action=last, page=page, last=last, data='')
        )
        build.adjust(1) 
    elif page == 3:
        build.button(
            text="Криптовалюта",
            callback_data=Pagination(action="crypto", page=page, last=last, data='')
        )
        build.button(
            text="◀назад",
            callback_data=Pagination(action=last, page=page, last=last, data='')
        )
        build.adjust(1) 
    elif page == 4:
        for el in elem:
            build.button(
            text=el,
            callback_data=Pagination(action="crypto_accept", page=page, last=last, data=el)
            )
        build.button(
            text="◀назад",
            callback_data=Pagination(action=last, page=page, last=last, data='')
        )
        build.adjust(3) 
    elif page == 5:
        build.button(
            text="Оплатить",
            url = f"{elem[0]}"
        )
        build.button(
            text="Я оплатил",
            callback_data=Pagination(action="crypto_ok", page=page, last=last, data=f'{elem[1]}')
        )
        build.button(
            text="◀назад",
            callback_data=Pagination(action=last, page=page, last=last, data='')
        )
        build.adjust(1) 
    return build.as_markup(resize_keyboard=True)