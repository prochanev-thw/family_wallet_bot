from datetime import datetime
from src.spreadsheets.gspread_factory import gspread_factory

import logging


logger = logging.getLogger(__name__)

now = datetime.now(tz='Asia/Yekaterinburg').strftime('%d.%m.%Y %H:%M:%S.%f')

def save_into_new_raw(amount, category, user):
    sh = gspread_factory().open('family-wallet').worksheet("sheet1")
    save_row(sh, amount, category, user)

def save_row(sh, amount, category, user):
    active_row = next_available_row(sh)

    logger.info(
        'A%(active_row)s:D%(active_row)s with values %(user)s, %(category)s, %(amount)s, %(now)s', 
        {'active_row': active_row,
         'user': user,
         'category': category,
         'amount': amount,
         'now': now,
        })

    sh.batch_update([{
        'range': f'A{active_row}:D{active_row}',
        'values': [[user, category, amount, now]],
    }])

def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)
