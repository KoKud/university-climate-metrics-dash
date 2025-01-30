import dash
from dash import Dash, html, page_container, page_registry, dcc
import pandas as pd

external_scripts = [
    {"src": 'https://cdn.tailwindcss.com'},
]

app = Dash(
    __name__, 
    external_scripts=external_scripts,
    use_pages=True
)
server = app.server

app.layout = html.Div([
    # Navigation
    html.Div([
        html.Nav([
            html.Div([
                html.Div([
                    # Static title
                    html.Div("Projekt Wizualizacja Danych", className="lg:text-3xl text-2xl mr-20 md:mx-0 mx-auto"),
                    # Links in separate div
                    html.Div([
                        dcc.Link(
                            f"{page['name']}", 
                            href=page["relative_path"],
                            className="hover:text-blue-800 px-4"
                        ) for page in dash.page_registry.values()
                        if page["module"] != "pages.not_found_404"
                    ], className="flex md:flex-row md:my-0 my-4 flex-col items-center text-gray-600 uppercase justify-between lg:justify-end lg:space-x-20")
                ], className="flex md:flex-row flex-col justify-between")
            ])
        ], className="container mx-auto p-6")
    ]),
    # Page content
    html.Div(page_container, className="container mx-auto p-6 min-h-[50vh]"),
    # Footer
    html.Footer([
        html.Div([
            html.Div([
                html.Div([
                    html.Div("Projekt Wizualizacja Danych", className="text-2xl mb-4"),
                    html.Div([
                        dcc.Link(
                            f"{page['name']}", 
                            href=page["relative_path"],
                            className="hover:text-blue-800 px-4"
                        ) for page in dash.page_registry.values()
                        if page["module"] != "pages.not_found_404"
                    ], className="flex flex-col md:flex-row  items-center md:space-x-10 md:space-y-0 space-y-3 text-gray-300")
                ])
            ], className="flex flex-col text-center md:text-left"),
            html.Div([
                html.Div([
                    dcc.Link([html.Img(src="/assets/images/icon-github.svg") ], 
                             className="ficon", href="#"),
                    dcc.Link([html.Img(src="/assets/images/icon-facebook.svg") ], 
                             className="ficon", href="#"),
                    dcc.Link([html.Img(src="/assets/images/icon-instagram.svg") ], 
                             className="ficon", href="#"),
                    dcc.Link([html.Img(src="/assets/images/icon-twitter.svg") ], 
                             className="ficon", href="#")
                ], className="flex flex-row space-x-3 mx-auto md:mx-0"),
                html.Div([
                    "© 2025 Konrad Kudlak. All Rights Reserved"
                ], className="text-gray-300")
            ], className="flex flex-col space-y-5 mx-auto md:mx-0  mt-3")
        ], className="container max-w-7xl p-10 mx-auto flex flex-col md:flex-row justify-between")
    ], className="bg-gray-900 text-white")
])

if __name__ == "__main__":
    app.run_server(debug=True)