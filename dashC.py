from dash import Dash
from dash import dcc
from dash import html


app = Dash(__name__)




app.layout = html.Div(children=[
html.H1(children='Hello guvi',style={'color':'red'}),
html.H2(children='everyone is budding with plotly '),
html.P("ar is an intense armed conflict between states, governments, societies, or paramilitary groups such as mercenaries, insurgents, and militias."),


html.Div(children='''
Dash: A web application framework for your data.this is datascience
''')




],style={'color':'blue','marginBottom':100,'marginTop':300})


try:
    if __name__ == '__main__':
        app.run_server(debug=True)
except:
    print("this is and exception")
