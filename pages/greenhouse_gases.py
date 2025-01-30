import dash
from dash import html, dcc, callback, Input, Output
import plotly.graph_objs as go

from data.data import get_dataset

dash.register_page(__name__, path='/greenhouse-gases', name='Gazy cieplarniane')

@callback(
    Output('graph-greenhouse', 'figure'),
    [Input('country-dropdown', 'value'), Input('year-slider', 'value')]
)
def update_graph(selected_country, year_range):
    df = get_dataset()
    filtered_df = df[
        (df['year'] >= year_range[0]) & 
        (df['year'] <= year_range[1]) &
        (df['country'] == selected_country)
    ]
    return {
        'data': [{
            'x': filtered_df['year'],
            'y': filtered_df[gas],
            'type': 'scatter',
            'name': gas
            } for gas in ['total_ghg', 'co2', 'methane', 'nitrous_oxide']
        ],
    }

@callback(
    Output('graph-greenhouse-2', 'figure'),
    [Input('year-dropdown', 'value')]
)
def update_graph2(selected_year):
    df = get_dataset()
    latest_data = df[(df['year'] == selected_year) & (df['country'] == 'World')]
    gas_columns = ['co2', 'methane', 'nitrous_oxide']
    ghg_emissions = latest_data[gas_columns].sum()
    return {
        'data': [
            go.Pie(labels=gas_columns, values=ghg_emissions, 
                   hoverinfo='label+percent', textinfo='value', 
                   marker=dict(colors=['#4285f4', '#ea4335', '#fbbc05']))
        ],
    }

@callback(
    Output('graph-greenhouse-3', 'figure'),
    [Input('year-dropdown', 'value'), Input('sort-dropdown', 'value')]
)
def update_graph3(selected_year, sort_by):
    df = get_dataset()
    latest_data = df[df['year'] == selected_year]
    top_countries = latest_data[~latest_data['country'].isin([
        'World', 'Asia', 'Europe', 'Africa', 'North America', 'South America', 'Oceania', 'Non-OECD (GCP)', 'High-income countries'
        ])].sort_values(sort_by, ascending=False).head(20)
    
    return {
        'data': [{
            'x': top_countries['country'],
            'y': top_countries[i],
            'type': 'bar',
            'name': i
        }for i in ['methane', 'nitrous_oxide']],
    }

layout = html.Div([
    # Graph 1 - Greenhouse Gases
    html.Div([
        html.H1("📈 Gazy cieplarniane w czasie", className="text-3xl"),
        # Select Filters
        html.Div([
            html.Div([
                html.Label("Wybierz państwo:"),
                dcc.Dropdown(
                    id='country-dropdown',
                    options=[{'label': c, 'value': c} for c in sorted(get_dataset()['country'].unique())],
                    value='World'
                ),
            ], className="flex-1"),
            html.Div([
                html.Label("Wybierz zakres lat:", style={'marginTop': '20px'}),
                dcc.RangeSlider(
                    id='year-slider',
                    min=get_dataset()['year'].min(),
                    max=get_dataset()['year'].max(),
                    value=[1900, 2023],
                    marks={i: str(i) for i in range(int(get_dataset()['year'].min()), int(get_dataset()['year'].max()+1), 10)},
                    step=1
                )
            ], className="flex-1")
        ], className="p-2 flex flex-col md:flex-row justify-between"),
        # Graph view
        html.Div([
            dcc.Graph(id='graph-greenhouse', className="w-full h-full"),
        ])
    ],className="p-5 m-2 bg-white rounded-3xl shadow-lg"),
    # Share of Greenhouse Gases
    html.Div([
        html.H1("🌳 Udział gazów cieplarnianych", className="text-3xl"),
        html.Div([
            html.Label("Wybierz rok:"),
            dcc.Dropdown(
                id='year-dropdown',
                options=[{'label': c, 'value': c} for c in sorted(get_dataset()['year'].unique())],
                value=2023
            ),
        ], className="flex-1"),
        html.Div([
            dcc.Graph(id="graph-greenhouse-2", className="w-full h-full", )
        ])
    ],className="p-5 m-2 mt-8 bg-white rounded-3xl shadow-lg"),
    # Top Emitting Countries
    html.Div([
        html.H1("🌍 Top państw pod względem emisji CO2", className="text-3xl"),
        html.Div([
            html.Div([
                html.Label("Wybierz rok:"),
                dcc.Dropdown(
                    id='year-dropdown',
                    options=[{'label': c, 'value': c} for c in sorted(get_dataset()['year'].unique())],
                    value=2023
                ),
            ], className="flex-1"),
            html.Div([
                html.Label("Sortuj po:"),
                dcc.Dropdown(
                    id='sort-dropdown',
                    options=[{'label': c, 'value': c} for c in ['methane', 'nitrous_oxide', 'co2']],
                    value='methane'
                ),
            ], className="flex-1"),
        ],className="p-2 flex flex-col md:flex-row justify-between space-x-2"),
        html.Div([
            dcc.Graph(id="graph-greenhouse-3", className="w-full h-full", )
        ])
    ], className="p-5 m-2 mt-8 bg-white rounded-3xl shadow-lg")
])