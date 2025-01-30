from dash import html

def Card(cardTitle, cardData, dataColor):
    return html.Div([
            html.P(cardTitle, className='text-lg text-semibold text-gray-600'),
            html.P(cardData, className=f'text-5xl font-bold text-{dataColor}'),
        ], className='flex flex-col w-48 h-32 bg-white rounded-xl shadow-lg items-center justify-evenly')