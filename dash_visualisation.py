# Import necessary libraries
import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load your data
data = pd.read_csv(r'C:\Users\Iele\Desktop\Quantium_task1\sales_result_edit.csv')

# Sort the data by date
data['date'] = pd.to_datetime(data['date'])
data = data.sort_values(by='date')

# Create Dash app
app = dash.Dash(__name__)

# Define layout of the app
app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Visualise'),

    dcc.Graph(
        id='sales-bar-chart',
        figure=px.bar(data, x='date', y='sales', title='Pink Morsel Sales Over Time')
                    .update_layout(xaxis_title='Date', yaxis_title='Sales'),
    ),
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
