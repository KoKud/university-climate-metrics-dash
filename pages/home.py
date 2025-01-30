import dash
from dash import html, dcc

from data.data import get_dataset
from components.Card import Card

dash.register_page(__name__, path='/', name='Home')

layout = html.Div([
    html.Div([
        html.Div([
            html.H1('Projekt zaliczeniowy z przedmiotu "Wizuazlizacja danych"', className='text-3xl'),
            html.P('Autor: Konrad Kudlak', className='text-xl text-gray-600'),
            html.P('Rok: 2025', className='text-xl text-gray-600'),
            html.P('Kierunek: Informatyka', className='text-xl text-gray-600'),
        ], className="flex-1 p-8 border-2 border-gray-200 rounded-3xl shadow-lg"),
        html.Div([
            html.H1('Opis projektu', className='text-2xl'),
            html.P('Projekt ma na celu przedstawienie wizualizacji danych związanych z emisją CO2 oraz emisją gazów cieplarnianych.', className='text-xl text-gray-600'),
            html.P('Dane zostały pobrane z serwisu internetowego "Our World in Data".', className='text-xl text-gray-600'),
            dcc.Link('Link do danych', href='https://github.com/owid/co2-data/blob/master/owid-co2-data.csv', className='text-xl text-blue-600'),
        ], className="flex-1 border-r-2 border-gray-200 rounded-3xl p-8")
    ], className='flex flex-col md:flex-row m-5 gap-5 items-center'),
    html.Div([
        html.H1('Informacje na temat zbioru danych', className='text-2xl mt-10'),
        html.Div([
            Card("Liczba wierszy", get_dataset().shape[0], "sky-600"),
            Card("Liczba kolumn", get_dataset().shape[1], "rose-600"),
        ], className='flex items-center gap-4 w-4xl'),
        html.Div([
            Card("Liczba państw", get_dataset()['country'].nunique(), "green-600"),
            Card("Liczba lat", get_dataset()['year'].nunique(), "amber-600"),
            Card("Liczba sektorów", 6, "blue-600"),
        ], className='flex items-center gap-4')
    ], className='flex flex-col m-10 gap-5 items-center'),

    html.Div([
        html.Div([
            html.H1('Technologie', className='text-2xl'),
            html.P('Projekt został stworzony przy użyciu następujących technologii:', className='text-xl text-gray-600'),
            html.Div([
                html.Ul([
                    html.Li('Python'),
                    html.Li('Pandas'),
                    html.Li('Plotly'),
                    html.Li('Dash'),
                    html.Li('Tailwind CSS'),
                ], className='text-md text-gray-600 flex gap-6'),
            ], className="flex justify-center"),
        ], className='flex flex-col w-1/2 items-center py-10 px-5 border-l-2 border-t-2 border-gray-200 rounded-l-3xl shadow-[0_-15px_15px_-15px_rgba(0,0,220,0.3),_-15px_0_15px_-15px_rgba(0,0,150,0.3)]'),
        html.Div([
            html.P('Projekt składa się z 4 stron:', className='text-xl text-gray-600'),
            html.Ul([
                html.Li('Strona główna - zawiera informacje o autorze oraz opis projektu.'),
                html.Li('Trendy - zawiera wizualizacje danych związanych z emisją CO2.'),
                html.Li('Gazy cieplarniane - zawiera wizualizacje danych związanych z emisją gazów cieplarnianych.')
            ]),
        ])
    ], className='flex flex-col md:flex-row m-5 gap-5 justify-between mt-20 items-center'),
    
    

    

    

])