import dash
from dash import html

from data.data import get_test_data

dash.register_page(__name__, path='/', name='Home')

layout = html.Div([
    html.H1('Home Page'),
    html.P(get_test_data().shape)
])