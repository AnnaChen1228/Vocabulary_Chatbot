from openpyxl import Workbook
import sentence

def excel_sentence(user_file,mistake_word):
    wb = Workbook()
    ws = wb.active
    ws.append(['單字','意思','例句'])
    sentence.get_sentence(mistake_word)
    for row in mistake_word:
        ws.append(row)
    wb.save(user_file)

def excel(user_file,mistake_word):
    wb = Workbook()
    ws = wb.active
    ws.append(['單字','意思'])
    for row in mistake_word:
        ws.append(row)
    wb.save(user_file)