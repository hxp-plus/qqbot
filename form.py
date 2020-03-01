import openpyxl
import re

book_name = 'A李萍22名单（胡喜平）.xlsx'
sheet_name = 'Sheet3'
datafile = 'data.txt'
offset_date = 8
offset_student_number = 3

def read_xlsx(path, sheet_name):
    workbook = openpyxl.load_workbook(path)
    sheet = workbook[sheet_name]
    return workbook,sheet

def write_xlsx(student_number, date, book_name, sheet_name, offset_student_number, offset_date):
    workbook,sheet = read_xlsx(book_name, sheet_name)
    for i in range(1,50):
        if sheet.cell(row=i, column=offset_student_number).value == student_number :
            for j in range(offset_date, offset_date + 3):
                if sheet.cell(row=i, column=j).value == None:
                    sheet.cell(row=i, column=j).value = date
                    workbook.save(book_name)
                    print(student_number, '\t', date)

def read_data_and_write(datafile, book_name, sheet_name, offset_student_number, offset_date):
    fo = open(datafile, 'r+')
    while True:
        line = fo.readline()
        if not line:
            break
        if re.search(r'U\d{9}', line) and re.search(r'\d{4}/\d{1,2}/\d{1,2}', line):
            student_number=re.search(r'U\d{9}', line).group(0)
            date=re.search(r'\d{4}/\d{1,2}/\d{1,2}', line).group(0)
            write_xlsx(student_number, date, book_name, sheet_name, offset_student_number, offset_date)

read_data_and_write(datafile, book_name, sheet_name, offset_student_number, offset_date)
