import gspread
import os
from google.oauth2.service_account import Credentials

scopes=[
    'https://www.googleapis.com/auth/spreadsheets',
]

credentials = Credentials.from_service_account_file('credentials.json', scopes=scopes)
client=gspread.authorize(credentials)

sheet_id=os.environ.get('SHEET_ID')

workbook=client.open_by_key(sheet_id)

values_list=workbook.sheet1.get_all_values()
print(values_list[0])

worksheet_list=workbook.worksheets()
print(worksheet_list)

worksheet=map(lambda x: x.title, worksheet_list)
print(list(worksheet))

worksheet=workbook.get_worksheet(0)
print(worksheet.get_all_values())

worksheet=workbook.get_worksheet(0)
worksheet.update_title('First Sheet')

worksheet=workbook.get_worksheet(0)
worksheet.append_row(['Hello', 'World'])

worksheet=workbook.get_worksheet(0)
worksheet.insert_row(['Hello', 'World'], 1)

worksheet=workbook.get_worksheet(0)
worksheet.update('A1', [['Hello', 'World']])

worksheet=workbook.get_worksheet(0)
worksheet.update('A1:B1', [['Hello', 'World']])

worksheet=workbook.get_worksheet(0)
worksheet.update_cell(3, 3, 'Hello')

worksheet=workbook.get_worksheet(0)
cell_value=worksheet.acell('A1').value
print(cell_value)

worksheet=workbook.get_worksheet(0)
worksheet.format('A1:B1', {
    "backgroundColor": {
        "red": 1.0,
        "green": 0.0,
        "blue": 0.0
    }
})

# worksheet=workbook.get_worksheet(0)
# worksheet.delete_row(1)
#
# worksheet=workbook.get_worksheet(0)
# worksheet.clear()
