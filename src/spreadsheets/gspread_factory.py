import gspread
import os
import base64
import json
import logging

from src.settings import Settings

logger = logging.getLogger(__name__)

def gspread_factory():
    if Settings.DEV_ENVIRONMENT:
        gs = gspread.service_account('gspread_key.json')
    else:
        GSPRED_JSON_KEY_DICT = json.loads(base64.b64decode(Settings.GSPREAD_B64_KEY).decode())
        gs = gspread.service_account_from_dict(GSPRED_JSON_KEY_DICT)

    logger.info('Gspread have connected')
    return gs
