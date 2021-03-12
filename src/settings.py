import os
from dotenv import load_dotenv


load_dotenv()

dev_environment = os.getenv('DEVELOPMENT', 'False') == 'True'

class Settings:
    USERS = {506520483: 'Женя', 370226546: 'Юля'}
    DEV_ENVIRONMENT = dev_environment
    GSPRED_JSON_KEY = os.getenv('GSPRED_JSON_KEY')
    TELEGRAM_URI = 'https://api.telegram.org/bot'
    TELEGRAM_TOKEN  = os.getenv('TELEGRAM_TOKEN')
