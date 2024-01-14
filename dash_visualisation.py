# Import necessary libraries
import dash
from dash import dcc, html
#import dash_core_components as dcc
#import dash_html_components as html
import pandas as pd
import plotly.express as px

# Load your data (replace 'your_data.csv' with the actual file path)
df1 = pd.read_csv(r'C:\Users\Iele\Desktop\Quantium_task1\daily_sales_data_0.csv')
df2 = pd.read_csv(r'C:\Users\Iele\Desktop\Quantium_task1\daily_sales_data_1.csv')
df3 = pd.read_csv(r'C:\Users\Iele\Desktop\Quantium_task1\daily_sales_data_2.csv')

# Concatenate or merge your dataframes to create a single dataframe
data = pd.concat([df1, df2, df3], ignore_index=True)

# Sort the data by date
data['date'] = pd.to_datetime(data['date'])
data = data.sort_values(by='date')

# Filter the data for Pink Morsel
#pink_morsel_data = data[data['item'] == 'pink morsel']
pink_morsel_data = data[data['product'] == 'pink morsel']
# Create Dash app
app = dash.Dash(__name__)

# Define layout of the app
app.layout = html.Div(children=[
    html.H1(children='Sales Data Visualizer'),

    dcc.Graph(
        id='sales-line-chart',
        figure=px.line(pink_morsel_data, x='date', y='quantity', title='Pink Morsel Sales Over Time')
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
