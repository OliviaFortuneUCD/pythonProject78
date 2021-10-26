import pandas as pd
import xlsxwriter
import xlrd
import openpyxl


reader = pd.read_excel(r'Oursales2021.xlsx',sheet_name='Salesname')
#print(reader)
reader1 = pd.read_excel(r'Oursales2021.xlsx',sheet_name='Profit')
#print(reader1)

df_row = pd.concat([reader, reader1])

print(df_row)