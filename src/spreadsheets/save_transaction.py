from datetime import datetime
from src.spreadsheets.gspread_factory import gspread_factory

now = datetime.now().strftime('%d.%m.%Y %H:%M:%S.%f')

def save_into_new_raw(amount, category, user):
    sh = gspread_factory().open('family-wallet').worksheet("sheet1")
    save_row(sh, amount, category, user)

def save_row(sh, amount, category, user):
    active_row = next_available_row(sh)
    sh.batch_update([{
        'range': f'A{active_row}:D{active_row}',
        'values': [[user, category, amount, now]],
    }])

def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)
