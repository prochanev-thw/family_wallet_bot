from src.handler import handler

event = """{
    "update_id": 812772640,
    "message": {
        "message_id": 619343,
        "from": {
            "id": 506520483,
            "is_bot": false,
            "first_name": "\u042e\u043b\u0438\u044f",
            "last_name": "\u041f\u0440\u043e\u0447\u0430\u043d",
            "username": "Julia_Prochan",
            "language_code": "ru"
        },
        "chat": {
            "id": 506520483,
            "first_name": "\u042e\u043b\u0438\u044f",
            "last_name": "\u041f\u0440\u043e\u0447\u0430\u043d",
            "username": "Julia_Prochan",
            "type": "private"
        },
        "date": 1615526697,
        "text": "- = б"
    }
}"""

handler(event, {'context': 'empty'})