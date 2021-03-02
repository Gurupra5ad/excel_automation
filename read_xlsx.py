from openpyxl import load_workbook

book = load_workbook('main.xlsx')
sheet = book.active

for row in sheet:
    for cell in row:
        print(cell.value)