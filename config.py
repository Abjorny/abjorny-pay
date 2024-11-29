from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API_KEY = os.getenv("API_KEY")

tarifs = {
    1: ['Месяц 1$', 1],
    3: ['3 месяца 3$', 3],
    9: ['Год 9$', 12],
}

def TextsList (key:str,values = {}) -> str:
    texts = {
        "start-text":f"*Привет, {values.get('username','')}!\nЭто бот для рассылки эксклюзивного контента по криптовалюте, чтобы начать получать посты, купите подписку в профиле.*",
    }
    if key in texts:
        return texts[key]
    else:
        raise KeyError(f"Key '{key}' not found in texts.")