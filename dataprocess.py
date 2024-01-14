#import pandas as pd

# Provide the path for the three CSV file

#file_path = r'C:\Users\Iele\Desktop\Quantium_task1\daily_sales_data_0.csv'

# Load data into a DataFrame
#df = pd.read_csv(file_path, header=0)

#display the data frame
#print(df)

#import pandas as pd

# Specify the paths for the three CSV files
#file1_path = r'C:\Users\Iele\Desktop\Quantium_task1\daily_sales_data_0.csv'
#file2_path = r'C:\Users\Iele\Desktop\Quantium_task1\daily_sales_data_1.csv'
#file3_path = r'C:\Users\Iele\Desktop\Quantium_task1\daily_sales_data_2.csv'

# Load the data from the three CSV files into three separate dataframes
#df1 = pd.read_csv(file1_path, header=0)
#df2 = pd.read_csv(file2_path, header = 0)
#df3 = pd.read_csv(file3_path, header =0)

# Concatenate the three dataframes vertically
#final_df = pd.concat([df1, df2, df3], axis=0)


#final_df = pd.concat([df1, df2, df3], ignore_index=True)

# Display the final dataframe
#print(final_df) 

#import pandas as pd

#df1 = pd.read_csv(r'C:\Users\Iele\Desktop\Quantium_task1\daily_sales_data_0.csv')
#df2 = pd.read_csv(r'C:\Users\Iele\Desktop\Quantium_task1\daily_sales_data_1.csv')  
#df3 = pd.read_csv(r'C:\Users\Iele\Desktop\Quantium_task1\daily_sales_data_2.csv')

#combined_df = pd.concat([df1, df2, df3])



#print(combined_df)

#import pandas as pd

#df1 = pd.read_csv(r'C:\Users\Iele\Desktop\Quantium_task1\daily_sales_data_0.csv')
#df2 = pd.read_csv(r'C:\Users\Iele\Desktop\Quantium_task1\daily_sales_data_1.csv')
#df3 = pd.read_csv(r'C:\Users\Iele\Desktop\Quantium_task1\daily_sales_data_2.csv')

#combined_df = pd.concat([df1, df2, df3])

#combined_df['sales'] = combined_df['quantity'] * combined_df['price'] 

#combined_df.to_csv(r'C:\Users\Iele\Desktop\combined_sales.csv', index=False)
#import pandas as pd

#df1 = pd.read_csv(r'C:\Users\Iele\Desktop\Quantium_task1\daily_sales_data_0.csv')
#df2 = pd.read_csv(r'C:\Users\Iele\Desktop\Quantium_task1\daily_sales_data_1.csv')
#df3 = pd.read_csv(r'C:\Users\Iele\Desktop\Quantium_task1\daily_sales_data_2.csv')

#combined_df = pd.concat([df1, df2, df3])

#combined_df['sales'] = combined_df['quantity'] * combined_df['price']
#print(combined_df)


# Leave date and region as is


import pandas as pd

# Assuming your data is stored in CSV files named 'daily_sales_data_0.csv', 'daily_sales_data_1.csv', and 'daily_sales_data_2.csv'
file_paths = [
    r'C:\Users\Iele\Desktop\Quantium_task1\daily_sales_data_0.csv',
    r'C:\Users\Iele\Desktop\Quantium_task1\daily_sales_data_1.csv',
    r'C:\Users\Iele\Desktop\Quantium_task1\daily_sales_data_2.csv'
]

# Read each CSV file into a separate DataFrame
dfs = [pd.read_csv(file_path) for file_path in file_paths]

# Concatenate the DataFrames into a single DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# Task 1: Filter rows where the 'product' is 'pink morsel'
if 'product' in combined_df.columns:
    # Use str.lower() to make the comparison case-insensitive
    # Use str.strip() to remove leading and trailing whitespaces
    filtered_data = combined_df[combined_df['product'].str.strip().str.lower() == 'pink morsel']

    # Task 2: Create a new column 'sales' by multiplying 'quantity' and 'price'
    if not filtered_data.empty:
        filtered_data['sales'] = filtered_data['quantity'] * filtered_data['price']

        # Display the resulting DataFrame
        print(filtered_data)
    else:
        print("No rows found with 'pink morsel' in the 'product' column.")
else:
    print("Column 'product' not found in the DataFrame.")


# Export filtered data to CSV
desktop_path = r'C:\Users\Iele\Desktop' 
csv_file = 'filtered_data.csv'

full_path = desktop_path + '\\' + csv_file

filtered_data.to_csv(full_path, index=False)

print('Filtered data exported to CSV: {}'.format(full_path))





