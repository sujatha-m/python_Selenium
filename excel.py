"""
pip install xlrd==1.2.0   # pip uninstall xlrd
pip list
"""

import xlrd

# path = (r"C:\Users\sujat\OneDrive\Desktop\data.xlsx")
path = (r"C:\Users\sujat\Downloads\testData.xlsx")
workbook_obj = xlrd.open_workbook(path)
print(workbook_obj)

# create an instance of worksheet
worksheet_obj = workbook_obj.sheet_by_name("testdata")
print(worksheet_obj)
#
# get the content of all the rows   ---- generator object
rows = worksheet_obj.get_rows()
print(rows)

# traversing through the generator object
for row in rows:
    print(row)

rows = worksheet_obj.get_rows()
print(rows)

# getting values from cell objects
for row in rows:
    print(row[0].value, row[1].value)

rows = worksheet_obj.get_rows()
header = next(rows)   # to skip 1 iteration
print(header)   # [text:'name', text:'profession']

# create a dictionary
d = {row[0].value: row[1].value for row in rows}
print(d)