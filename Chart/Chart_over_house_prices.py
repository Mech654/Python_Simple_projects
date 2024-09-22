import requests
import pandas as pd

# Fetch the webpage content
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
url = 'https://www.propertyinvestmentproject.co.uk/property-statistics/nationwide-average-house-price/'
response = requests.get(url, headers=headers)

# Parse HTML content to get tables (returns a list of DataFrames)
tables = pd.read_html(response.text)

# Assuming 'chart' is the DataFrame you want to work with (select the appropriate index if there are multiple tables)
chart = tables[0]  # Selecting the first table, change the index if needed

# Initialize lists for storing unique 'Year' values and corresponding 'Avg House price (£)' values
ListX = []
ListY = []

# Print every item in the specified column
column_name_X = 'Year'  # Replace with the actual column name
column_name_Y = 'Avg House price (£)'  # Replace with the actual column name

if column_name_X in chart.columns and column_name_Y in chart.columns:
    # Iterate through each item in the column
    for index, item_x in enumerate(chart[column_name_X]):
        item_y = chart[column_name_Y][index]
        if item_x not in ListX:
            ListX.append(item_x)
            ListY.append(item_y)

# Reverse lists if needed (as per your previous attempt)
ListX.reverse()
ListY.reverse()

# Print the lists of unique 'Year' values and 'Avg House price (£)' values
print("ListX (Unique Years):", ListX)
print("ListY (House Prices):", ListY)

