import pandas as pd

# Provide the path to your CSV file
file_path = r'C:\Users\Iele\Desktop\Quantium_task1\daily_sales_data_0.csv'

# Load data into a DataFrame
df = pd.read_csv(file_path, header=0)

#display the data frame
print(df)