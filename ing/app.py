import dash
import dash_core_components as dcc
import dash_html_components as html

import plot

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(
        id='Saldo',
        figure=plot.storia_saldi()
    )
])

if __name__ == '__main__':
    app.run_server()
