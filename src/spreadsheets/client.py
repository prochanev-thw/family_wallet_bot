from src.spreadsheets.gspread_factory import gspread_factory, next_available_row

gs = gspread_factory()

sh = gs.open('family-wallet').worksheet("sheet1")
sh.update_cell(next_available_row(sh), 1, 'Bingo!')
sh.update_cell(next_available_row(sh), 1, 'Bingo!')
sh.update_cell(next_available_row(sh), 1, 'Bingo!')
sh.update_cell(next_available_row(sh), 1, 'Bingo!')
sh.update_cell(next_available_row(sh), 1, 'Bingo!')
sh.update_cell(next_available_row(sh), 1, 'Bingo!')
sh.update_cell(next_available_row(sh), 1, 'Bingo!')
sh.update_cell(next_available_row(sh), 1, 'Bingo!')
sh.update_cell(next_available_row(sh), 1, 'Bingo!')