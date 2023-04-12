print('salees!')
a = 0
b = 4
c = (a+1.5) * b
print(c)
print('using Thonny')

x = 7.5
def square_x(x):
    x *= x
    print(x)

print(x)


""" unrelated, excel sheets copy paste

import openpyxl

# Load Input1.xlsx workbook and Sheet1
wb_input1 = openpyxl.load_workbook('Input1.xlsx')
ws_input1 = wb_input1['Sheet1']

# Load Input2.xlsx workbook and Sheet2
wb_input2 = openpyxl.load_workbook('Input2.xlsx')
ws_input2 = wb_input2['Sheet2']

# Load Output.xlsx workbook and Output1 worksheet
wb_output1 = openpyxl.load_workbook('Output.xlsx')
ws_output1 = wb_output1['Output1']

# Load Output.xlsx workbook and Output2 worksheet
wb_output2 = openpyxl.load_workbook('Output.xlsx')
ws_output2 = wb_output2['Output2']

# Copy data from Sheet1 in Input1.xlsx to Output1.xlsx
for row in ws_input1.iter_rows(values_only=True):
    ws_output1.append(row)

# Copy data from Sheet2 in Input2.xlsx to Output2.xlsx
for row in ws_input2.iter_rows(values_only=True):
    ws_output2.append(row)

# Save changes to Output1.xlsx and Output2.xlsx
wb_output1.save('Output.xlsx')
wb_output2.save('Output.xlsx')

# Close all workbooks
wb_input1.close()
wb_input2.close()
wb_output1.close()
wb_output2.close()