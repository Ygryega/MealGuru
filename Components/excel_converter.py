import pandas as pd

# Read the Excel file
df = pd.read_excel('Components/Reglas.xlsx', engine='openpyxl')

# Convert to JSON
json_data = df.to_json(orient='records', indent=4)

# Save the JSON data to a file
with open('Components/reglas_output.json', 'w') as f:
    f.write(json_data)

print("Excel file converted to JSON successfully!")