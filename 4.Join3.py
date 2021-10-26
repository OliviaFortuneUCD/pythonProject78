import pandas as pd
import xlsxwriter
import xlrd
import openpyxl


reader = pd.read_excel(r'Oursales2021.xlsx',sheet_name='Salesname')

reader1 = pd.read_excel(r'Oursales2021.xlsx',sheet_name='Profit')


df_merge_col = pd.merge(reader, reader1, on='ID')

print(df_merge_col)