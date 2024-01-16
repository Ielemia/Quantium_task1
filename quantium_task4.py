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
    html.Header(
        id='header',
        style={'color': 'white', 'background-color': 'lightblue'}
    ),
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='region-dropdown',
                options=[
                    {'label': 'Please select dates to compare sales', 'value': ''},
                ] + [
                    {'label': region, 'value': region} for region in df['region'].unique()
                ],
                value='',
                multi=False,
                style={'color': 'black', 'background-color': 'lightgrey', 'label': {'color': 'black', 'background-color': 'lightgrey', 'font-weight': 'bold', 'font-size': '1.2em', 'padding': '0 10px'}}
            )
        ], style={'width': '50%', 'display': 'inline-block'}),
        html.Div([
            dcc.Graph(
                id='line-plot',
                style={'background-color': 'lightgrey'}
            )
        ], style={'width': '50%', 'display': 'inline-block'})
    ], style={'background-color': 'lightgrey'})
], style={'background-color': 'lightgrey'})

# Define callback to update line plot based on selected region
@app.callback(
    Output('line-plot', 'figure'),
    [Input('region-dropdown', 'value')]
)
def update_line_plot(selected_region):
    if not selected_region:
        return {}
    
    filtered_df = df[df['region'] == selected_region]
    
    # Create line plot using Plotly Express
    line_figure = px.line(filtered_df, x='date', y='sales', title=f'Sales for {selected_region}')
    
    return line_figure

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)