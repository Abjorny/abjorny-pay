token = "7607390972:AAGqHKWvU3zBP_YwN-9bGEdNvTrbnKu1pj4"

def TextsList (key:str,values = {}) -> str:
    texts = {
        "start-text":f"*Привет, {values.get('username','')}!\nЭто бот для рассылки эксклюзивного контента по криптовалюте, чтобы начать получать посты, купите подписку в профиле.*",
    }
    if key in texts:
        return texts[key]
    else:
        raise KeyError(f"Key '{key}' not found in texts.")