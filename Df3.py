# Import pandas package
import pandas as pd

# Define a dictionary containing employee data
data = {'Name': ['Stella', 'Peter', 'Mark', 'Taylor'],
        'Age': [27, 24, 22, 32],
        'Address': ['London', 'Paris', 'Dublin', 'Cork'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# select two columns
print(df[['Name', 'Qualification']])
#print one
print(df[['Name']])
