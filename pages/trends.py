import dash
from dash import html, dcc, callback, Input, Output
import plotly.graph_objs as go

from data.data import get_dataset

dash.register_page(__name__, path='/trends-co2', name='Trendy CO2')

# Graph 1 - CO2
@callback(
    Output('graph-co2', 'figure'),
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
            'y': filtered_df['co2'],
            'type': 'scatter',
            'name': selected_country
            }
        ],
    }

def get_graph_temp():
    df = get_dataset()
    filtered_df = df[
        (df['year'] >= 1850) & 
        (df['year'] <= 2023) &
        (df['country'] == 'World')
    ]
    return {
        'data': [{
            'x': filtered_df['year'],
            'y': filtered_df['temperature_change_from_co2'],
            'type': 'scatter',
            'name': 'Temperature'
            }
        ],
    }

# Graph 2 - CO2 per sektor
possible_sectors = ['cement_co2', 'coal_co2', 'gas_co2', 'oil_co2', 'flaring_co2', 'other_industry_co2']
@callback(
    Output('graph-co2-2', 'figure'),
    [Input('country2-down', 'value')]
)
def update_graph2(country):
    return {
        'data': [{
            'x': get_dataset()['year'],
            'y': get_dataset()[get_dataset()["country"]==country][sec],
            'type': 'scatter',
            'name': sec
        }for sec in possible_sectors],
    }

# Graph 3 - Top państ
@callback(
    Output('graph-co2-3', 'figure'),
    [Input('year3-dropdown', 'value')]
)
def update_graph3(selected_year):
    df = get_dataset()
    latest_data = df[df['year'] == selected_year]
    top_countries = latest_data[~latest_data['country'].isin([
        'World', 'Asia', 'Europe', 'Africa', 'North America', 'South America', 'Oceania', 'Non-OECD (GCP)', 'High-income countries'
        ])].sort_values('co2', ascending=False).head(20)
    
    return {
        'data': [{
            'x': top_countries['country'],
            'y': top_countries['co2'],
            'type': 'bar',
            'name': 'CO2 Emission'
        }],
        'layout': {
            'title': 'Top Countries by CO2 Emission',
            'xaxis': {'title': 'Country'},
            'yaxis': {'title': 'CO2 Emission'}
        }
    }

# Graph 4 - CO2 per sektor
@callback(
    Output('graph-sector-2', 'figure'),
    [Input('year3-down', 'value')]
)
def update_graph2(selected_year):
    df = get_dataset()
    sector_columns = ['cement_co2', 'coal_co2', 'oil_co2', 'gas_co2', 'flaring_co2', 'land_use_change_co2']
    latest_data = df[(df['year'] == selected_year) & (df['country'] == 'World')]
    sector_emissions = latest_data[sector_columns].sum()
    return {
        'data': [
            go.Pie(labels=sector_columns, values=sector_emissions, 
                   hoverinfo='label+percent', textinfo='value', 
                   marker=dict(colors=['#4285f4', '#ea4335', '#fbbc05', '#34a853', '#ff6d00', '#aa66cc']))
        ],
    }

layout = html.Div([
    html.Div([
        html.H1("Emisja CO2 🧪", className="text-5xl"),
    ], className="flex justify-center my-10"),
    # Temperature Change Graph
    html.Div([
        html.H1("🌡️ Zmiana temperatury w czasie", className="text-3xl"),
        # Graph view
        html.Div([
            dcc.Graph(figure=get_graph_temp(), className="w-full h-full"),
        ])
    ],className="p-5 m-2 bg-white rounded-3xl shadow-lg"),

    # CO2 Emission Graph
    html.Div([
        html.H1("💨 Trend w poziomie CO2", className="text-3xl"),
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
                    value=[2000, 2023],
                    marks={i: str(i) for i in range(int(get_dataset()['year'].min()), int(get_dataset()['year'].max()+1), 10)},
                    step=1
                )
            ], className="flex-1")
        ], className="p-2 flex flex-col md:flex-row justify-between"),
        # Graph view
        html.Div([
            dcc.Graph(id='graph-co2', className="w-full h-full"),
        ])
    ],className="p-5 m-2 bg-white rounded-3xl shadow-lg"),

    # Top Countries by CO2 Emission
    html.Div([
        html.H1("🌍 Top państw pod względem emisji CO2", className="text-3xl"),
        html.Div([
            html.Label("Wybierz rok:"),
            dcc.Dropdown(
                id='year3-dropdown',
                options=[{'label': c, 'value': c} for c in sorted(get_dataset()['year'].unique())],
                value=2023
            ),
        ], className="flex-1"),
        html.Div([
            dcc.Graph(id="graph-co2-3", className="w-full h-full", )
        ])
    ],className="p-5 m-2 mt-8 bg-white rounded-3xl shadow-lg"),
    html.Div([
        html.H1("🗺️ Emisja CO2 per sektor", className="text-5xl"),
    ], className="flex justify-center my-20"),
    # Udział sektorów w emisji CO2
    html.Div([
        html.H1("⚖️ Udział sektorów w emisji CO2", className="text-3xl"),
        html.Div([
            html.Label("Wybierz rok:"),
            dcc.Dropdown(
                id='year3-down',
                options=[{'label': c, 'value': c} for c in sorted(get_dataset()['year'].unique())],
                value=2023
            ),
        ], className="flex-1"),
        html.Div([
            dcc.Graph(id="graph-sector-2", className="w-full h-full")
        ])
    ],className="p-5 m-2 bg-white rounded-3xl shadow-lg"),

    # Emisja CO2 per sektor
    html.Div([
        html.H1("🎥 Emisja CO2 per sektor w czasie", className="text-3xl"),
        dcc.Dropdown(
                    id='country2-down',
                    options=[{'label': c, 'value': c} for c in sorted(get_dataset()['country'].unique())],
                    value='World'
                ),
        html.Div([
            dcc.Graph(id="graph-co2-2", className="w-full h-full")
        ])
    ],className="p-5 m-2 mt-8 bg-white rounded-3xl shadow-lg"),
])