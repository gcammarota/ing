import dash
import dash_core_components as dcc
import dash_html_components as html

from . import plot


def run():
    app = dash.Dash()
    app.layout = html.Div([
        dcc.Graph(
            id='Saldo',
            figure=plot.storia_saldi()
        )
    ])

    app.run_server()
