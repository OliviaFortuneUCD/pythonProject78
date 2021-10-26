import pandas as pd
import xlsxwriter
import xlrd
import openpyxl



# dataframe Name and Age columns
df = pd.DataFrame({'Name': ['Stella Jones', 'Mark Johnson', 'Peter Walker', 'Janet Spears','Ed Peters','Richard O Keefe'],
                   'Sales': [10000, 14000, 22000, 16000,1200,1400],'ID': ['1', '2', '3', '4','5','6']})


df1 = pd.DataFrame({'Division': ['Cork', 'Cork', 'Dublin', 'Waterford','Dublin','Dublin'],
                   'Commission': [16, 15, 32, 10,16,42], 'ID': ['1', '2', '3', '4','5','6']})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('Oursales2021.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Salesname', index=False)

# Convert the dataframe to an XlsxWriter Excel object.
df1.to_excel(writer, sheet_name='Profit', index=False)

# Close the Pandas Excel writer and output the Excel file.
writer.save()