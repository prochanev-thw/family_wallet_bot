import random
import requests

from src.spreadsheets import save_into_new_raw
from src.settings import Settings
from src.exceptions import UnknowUserException, InvalidInputException, FamilyWalletException

def extract_user_id(message):
    return message['from']['id']

def parse_text(text):
    try:
        val_1, val_2 = text.split('=')
        val_1, val_2 = int(val_1), val_2.strip()
        if abs(val_1) < 0 or len(val_2) < 1:
             raise InvalidInputException("Неверная сумма или категория")
    except ValueError as exc:
        raise InvalidInputException("Неверный формат ввода. Нужно [{сумма}(целое число с '-' если расход) = {категория}]. Например '-1000 = Курочка'")
    return val_1, val_2

def parse_message(message):
    user_id = extract_user_id(message)
    text = message['text']
    amount, category = parse_text(text)
    try:
        user = Settings.USERS[user_id]
    except KeyError:
        raise UnknownUserException('Неизвестный пользователь...')
    return amount, category, user

def save_transaction(data):
    message = data['message']
    user_id = extract_user_id(message)
    try:
        amount, category, user = parse_message(message)
    except FamilyWalletException as exc:
        send_message(exc, user_id)
    else:
        save_into_new_raw(amount, category, user)
        if Settings.ENABLE_GOOD_PHRASES:
            if Settings.USERS[user_id] == 'Юля':
                phrase = random.choice(Settings.PHRASES)
                if phrase:
                    send_message(phrase, user_id)

def send_message(message, chat_id):

    params = {
        'chat_id': chat_id,
        'text': message
    }

    requests.get(f'{Settings.TELEGRAM_URI}{Settings.TELEGRAM_TOKEN}/sendMessage', params=params)
