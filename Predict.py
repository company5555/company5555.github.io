import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load the dataset
file_path = 'Prediction_DataSet.xlsx'
df = pd.read_excel(file_path, sheet_name='Raw_Data')

# Function to forecast salaries for all sectors and save results to an Excel file
def forecast_all_sectors(output_file):
    results = []
    years = np.array([int(col) for col in df.columns[1:]])  # Convert year columns to integers
    future_years = np.arange(years.min(), 2034)  # Years up to 2033

    for _, row in df.iterrows():
        sector_name = row['Sectors']
        salaries = row[1:].values

        # Prepare data for linear regression
        X = years.reshape(-1, 1)  # Independent variable (years)
        y = salaries  # Dependent variable (salaries)

        # Train the linear regression model
        model = LinearRegression()
        model.fit(X, y)

        # Predict salaries for years up to 2033
        future_salaries = model.predict(future_years.reshape(-1, 1))

        # Append results to the list
        for year, salary in zip(future_years, future_salaries):
            results.append({"Sector": sector_name, "Year": year, "Predicted_Salary": round(salary, 2)})

    # Create a DataFrame from the results
    results_df = pd.DataFrame(results)

    # Save the results to an Excel file
    results_df.to_excel(output_file, index=False)
    print(f"Predicted salaries have been saved to {output_file}")

# Example usage
output_file = 'Sector_Salary_Forecast.xlsx'  # Replace with desired output path
forecast_all_sectors(output_file)
