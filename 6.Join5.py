import pandas as pd
import xlsxwriter
import xlrd
import openpyxl



# dataframe Name and Age columns
df = pd.DataFrame({'Name': ['Stella Jones', 'Mark Johnson', 'Peter Walker', 'Janet Spears','Ed Peters','Richard O Keefe'],
                   'Sales': [10000, 14000, 22000, 16000,1200,1400],'ID': ['1', '2', '3', '4','5','6']})


df1 = pd.DataFrame({'ID': ['1', '2', '3', '4','5','6'],
                   'Department': ['Sales', 'Sales', 'Finance', 'HR','Sales','Finance']})


df_merge_col = pd.merge(df, df1, on='ID')
print(df_merge_col)