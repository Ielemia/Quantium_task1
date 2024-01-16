import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Load data
df = pd.read_csv("C:/Users/Iele/Desktop/Quantium_task1/sales_result_edit.csv") 

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div(style={'backgroundColor': '#f4f4f4', 'padding': '20px'}, children=[

    html.H1("Soul Food Sales Dashboard", id='header', style={'color': '#333', 'textAlign': 'center', 'fontFamily': 'Arial, sans-serif'}),
    
    html.Div([
        dcc.RadioItems(
            id='region-radio', 
            options=[{'label': r, 'value': r} for r in df['region'].unique()],
            value='Region',
            inline=True,  # Display radio buttons horizontally
            style={'margin': '20px 0', 'textAlign': 'center'}
        ),
    ]),
    
    dcc.Graph(id="sales-graph"),
])

@app.callback(
    Output("sales-graph", "figure"), 
    [Input("region-radio", "value")]
)

def update_chart(region):

    filtered_df = df[df['region'] == region]

    fig = px.line(filtered_df, x='date', y='sales')

    fig.update_traces(hovertemplate='$%{y:.2f}<extra></extra>')

    fig.update_xaxes(title_text='Date')

    fig.update_yaxes(title_text='Revenue', tickprefix='$')

    fig.update_layout(
        title_text=f'Sales in {region}',
        legend_title='Metrics',
        legend=dict(
            orientation="h",
            y=1.2,
            x=0.3,
            xanchor="right"
        ),
        paper_bgcolor='#fff',  # Background color of the plot
        plot_bgcolor='#f4f4f4',  # Background color of the chart area
    )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
