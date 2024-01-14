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

# Read each CSV file into a separate DataFrame
df1 = pd.read_csv(r'C:\Users\Iele\Desktop\Quantium_task1\daily_sales_data_0.csv')
df2 = pd.read_csv(r'C:\Users\Iele\Desktop\Quantium_task1\daily_sales_data_1.csv')
df3 = pd.read_csv(r'C:\Users\Iele\Desktop\Quantium_task1\daily_sales_data_2.csv')

# Concatenate the DataFrames into a single DataFrame
combined_df = pd.concat([df1, df2, df3], ignore_index=True)

# Check if the 'product' column is present in the DataFrame
if 'product' in combined_df.columns:
    # Task 1: Filter rows where the 'product' is 'pink morsel'
    filtered_data = combined_df[combined_df['product'].str.strip().str.lower() == 'pink morsel']

    # Task 2: Create a new column 'sales' by multiplying 'quantity' and cleaned 'price'
    if not filtered_data.empty:
        # Remove the space at the end of 'price' values and convert to float
        filtered_data['price'] = filtered_data['price'].str.rstrip().apply(lambda x: float(x.replace('$', '')))

        # Calculate 'sales' as integer
        filtered_data['sales'] = (filtered_data['quantity'] * filtered_data['price']).astype(int)

        # Task 3: Select relevant columns ('sales', 'date', 'region') for the output file
        output_data = filtered_data[['sales', 'date', 'region']]

        # Display the resulting DataFrame
        print(output_data)

        # Export the filtered data to a CSV file on the desktop
        output_data.to_csv(r'C:\Users\Iele\Desktop\Quantium_task1\sales_result_edit.csv', index=False)


