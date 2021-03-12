import gspread
import os
import json

from src.settings import Settings


def gspread_factory():
    if Settings.DEV_ENVIRONMENT:
        gs = gspread.service_account('gspread_key.json')
    else:
        GSPRED_JSON_KEY_DICT = json.loads(Settings.GSPRED_JSON_KEY)
        gs = gspread.service_account_from_dict(GSPRED_JSON_KEY_DICT)
    return gs
