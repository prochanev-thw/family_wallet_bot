from src.spreadsheets.gspread_factory import gspread_factory


def save_into_new_raw(amount, category, user):
    sh = gspread_factory().open('family-wallet').worksheet("sheet1")
    save_row(sh, amount, category, user)

def save_row(sh, amount, category, user):
    active_row = next_available_row(sh)
    sh.batch_update([{
        'range': f'A{active_row}:C{active_row}',
        'values': [[user, category, amount]],
    }])

def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)
