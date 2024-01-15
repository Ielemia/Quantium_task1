import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load the data
file_path = "C:/Users/Iele/Desktop/Quantium_task1/sales_result_edit.csv"
df = pd.read_csv(file_path)

# Create a Dash web application
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    dcc.RadioItems(
        id='region-radio',
        options=[
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},
            {'label': 'All', 'value': 'all'}
        ],
        value='all',
        labelStyle={'display': 'block'}
    ),
    dcc.Graph(
        id='line-plot',
    )
])

# Define callback to update line plot based on selected region
@app.callback(
    Output('line-plot', 'figure'),
    [Input('region-radio', 'value')]
)
def update_line_plot(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    # Create line plot using Plotly Express
    line_figure = px.line(filtered_df, x='date', y='sales', color='region', title=f'Sales for {selected_region.capitalize()} Region')

    return line_figure

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
