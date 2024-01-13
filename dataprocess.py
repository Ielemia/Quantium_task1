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

import pandas as pd

df1 = pd.read_csv(r'C:\Users\Iele\Desktop\Quantium_task1\daily_sales_data_0.csv')
df2 = pd.read_csv(r'C:\Users\Iele\Desktop\Quantium_task1\daily_sales_data_1.csv')  
df3 = pd.read_csv(r'C:\Users\Iele\Desktop\Quantium_task1\daily_sales_data_2.csv')

combined_df = pd.concat([df1, df2, df3])



print(combined_df)






