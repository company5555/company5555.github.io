import pandas as pd

# Load the dataset
file_path = 'Dataset2.xlsx'  # Replace with your file path
df = pd.ExcelFile(file_path).parse('Sheet1')


# Check the structure of the dataset
print(df.columns)
print(df.shape)

# If there are extra columns, drop them
df = df.iloc[:, :3]  # Keep only the first 3 columns

# Rename columns
df.columns = ['Educational Attainment', 'Median Weekly Earnings ($)', 'Unemployment Rate (%)']

# Clean and prepare the dataset
df = df[2:]  # Drop unnecessary rows
df.reset_index(drop=True, inplace=True)

# Convert relevant columns to numeric for calculations
df['Median Weekly Earnings ($)'] = pd.to_numeric(df['Median Weekly Earnings ($)'], errors='coerce')
df['Unemployment Rate (%)'] = pd.to_numeric(df['Unemployment Rate (%)'], errors='coerce')

# Map educational attainment to 4 categories
def map_educational_attainment(value):
    if value in [
        "No formal educational credential",
        "Postsecondary nondegree award",
        "Some college, no degree",
        "High school diploma or equivalent",
        "High school diploma",
        "Associate's degree",
    ]:
        return "High school diploma or less"
    elif value in ["Bachelor's degree", "Associate's degree"]:
        return "Bachelor's degree"
    elif value == "Master's degree":
        return "Master's degree"
    elif value == "Doctoral degree" or value == "Professional degree":
        return "Doctoral or professional degree"
    else:
        return "Unknown"

df['Educational Group'] = df['Educational Attainment'].map(map_educational_attainment)

# Group by the new educational groups and calculate averages
result = df.groupby('Educational Group').agg({
    'Median Weekly Earnings ($)': 'mean',
    'Unemployment Rate (%)': 'mean'
}).reset_index()

# Convert weekly earnings to annual earnings (52 weeks per year)
result['Median Weekly Earnings ($)'] = result['Median Weekly Earnings ($)'] * 50

# Round to 2 decimal places
result['Median Weekly Earnings ($)'] = result['Median Weekly Earnings ($)'].round(2)
result['Unemployment Rate (%)'] = result['Unemployment Rate (%)'].round(2)

# Reorder the groups as specified: 1, 3, 0, 2
result = result.reindex([1, 3, 0, 2]).reset_index(drop=True)

# Rename columns to match the required headers
result.columns = [
    "Educational attainment",
    "Median usual annual earnings ($)",  # Updated header
    "Unemployment rate (%)"
]

# Save the final result to "Sheet2" in an Excel file
output_file = 'Updated_Educational_Annual_Data_Sheet2.xlsx'  # Replace with your desired file path
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    result.to_excel(writer, index=False, sheet_name='Sheet2')

print(f"The updated version has been saved to {output_file}")