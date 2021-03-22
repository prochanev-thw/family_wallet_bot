import os
from dotenv import load_dotenv


dev_environment = os.getenv('DEVELOPMENT', 'False') == 'True'

if dev_environment:
    load_dotenv()

class Settings:
    DEV_ENVIRONMENT = dev_environment
    TELEGRAM_TOKEN  = os.getenv('TELEGRAM_TOKEN')
    GSPREAD_B64_KEY = os.getenv('GSPREAD_B64_KEY')

    USERS = {506520483: 'Женя', 370226546: 'Юля'}
    TELEGRAM_URI = 'https://api.telegram.org/bot'
    ENABLE_GOOD_PHRASES = True
    PHRASES = [
        'Умничка, так держать!',
        'Ты супер, детка!',
        'Юля, ты мое солнышко!',
        'Червяк! :)',
        'Уууеее, молдчинка!',
        'Ты бесподобна!',
        'Я не могу поверить в то, что я встретил такую очаровательную девушку как ты!',
        'Обожаю тебя, мой котеночек :)',
        'Все учтено!',
        'Супер!'
    ]