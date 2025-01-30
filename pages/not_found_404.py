import dash
from dash import html, dcc

dash.register_page(
    __name__,
    path="/404",
    title="404 - Page Not Found",
    description="404 error - page not found",
)

layout = html.Div([
    html.Div([
        html.H1("404 - Page Not Found", className="text-4xl font-bold text-red-600 mb-4"),
        html.P("The page you're looking for doesn't exist.", className="text-gray-600 mb-4"),
        dcc.Link(
            "Go back to Home",
            href="/",
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        )
    ], className="flex flex-col items-center justify-center min-h-screen")
], className="bg-gray-100")