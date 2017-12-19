import plotly.graph_objs as go


def storia_saldi():
    data = go.Scatter(
        x=[1,2,3],
        y=[4,6,5],
        text=['a', 'b', 'c'],
        mode='lines+markers',
        opacity=0.7,
    )

    layout = dict(
        xaxis={'title': 'Time'},
        yaxis={'title': '€'},
        margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
    )
    return dict(data=[data], layout=layout)


