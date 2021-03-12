import requests

import src.spreadsheets as sh
from src.settings import Settings
from src.exceptions import UnknowUserException, InvalidInputException, FamilyWalletException

def extract_user_id(message):
    return message['from']['id']

def parse_text(text):
    try:
        val_1, val_2 = text.split('=')
    except ValueError as exc:
        raise InvalidInputException("Неверный формат ввода. Нужно [сумма(целое число с '-' если расход) - категория]")
    return int(val_1.strip()), val_2.strip()

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
        sh.save_into_new_raw(amount, category, user)

def send_message(message, chat_id):

    params = {
        'chat_id': chat_id,
        'text': message
    }

    requests.get(f'{Settings.TELEGRAM_URI}{Settings.TELEGRAM_TOKEN}/sendMessage', params=params)
