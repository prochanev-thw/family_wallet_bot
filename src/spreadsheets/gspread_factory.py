import gspread
import os
import json


dev_environment = os.getenv('DEVELOPMENT', 'False') == 'True'


def gspread_factory():
    if dev_environment:
        gs = gspread.service_account('gspread_key.json')
    else:
        GSPRED_JSON_KEY_DICT = json.loads(os.environ('GSPRED_JSON_KEY'))
        gs = gspread.service_account_from_dict(GSPRED_JSON_KEY_DICT)
    return gs

def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)
