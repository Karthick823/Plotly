#import dash
from dash import Dash,Input,Output
from dash import dcc
from dash import html
from dash import dash_table as dt
from dash import Dash, dcc, html, Input, Output


import plotly.express as px


import plotly.express as px


df = px.data.iris()


#app = dash.Dash(__name__)
app = Dash(__name__)


app.layout = html.Div([
dcc.Graph(id="scatter-plot"),
html.P("Petal Width:"),
dcc.RangeSlider(
id='range-slider',
min=0, max=2.5, step=0.1,
marks={0: '0', 2.5: '2.5'},
value=[0.5, 2]
),
])


@app.callback(
Output("scatter-plot", "figure"),
[Input("range-slider", "value")])
def update_bar_chart(slider_range):
    low, high = slider_range
    mask = (df['petal_width'] > low) & (df['petal_width'] < high)
    return px.scatter(
        df[mask],
        x="sepal_width",
        y="sepal_length",
        color="species",
        size='petal_length',
        hover_data=['petal_width'],
    )


app.run_server(debug=True)
