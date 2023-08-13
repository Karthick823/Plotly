#import dash
from dash import Dash,Input,Output
from dash import dcc
from dash import html
from dash import dash_table as dt
from dash import Dash, dcc, html, Input, Output


import plotly.express as px


df = px.data.tips()
days = df.day.unique()
app = Dash(__name__)
#app = dash.Dash(__name__)


app.layout = html.Div([
dcc.Dropdown(
id="dropdown",
options=[{"label": x, "value": x} for x in days],
value=days[0],
clearable=False,
),
dcc.Graph(id="bar-chart"),
])


@app.callback(
Output("bar-chart", "figure"),
[Input("dropdown", "value")])

def update_bar_chart(day):
    mask = df["day"] == day
# sourcery skip: return-or-yield-outside-function
    fig = px.bar(df[mask], x="sex", y="total_bill",
    color="smoker", barmode="group")
    return fig


app.run_server(debug=True)