# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

df1 = pd.read_csv(r'C:\Users\Efrain\Desktop\regina_dashboard\regina_dashboard\02_data_preparation\casos_CORREGIMIENTO.csv')
df2 = pd.read_csv(r'C:\Users\Efrain\Desktop\regina_dashboard\regina_dashboard\02_data_preparation\casos_DISTRITO.csv')
df3 = pd.read_csv(r'C:\Users\Efrain\Desktop\regina_dashboard\regina_dashboard\02_data_preparation\casos_region.csv')

fig1 = px.bar(df1, x="Regiones", y="Casos")
fig2 = px.bar(df2, x="Regiones", y="Casos")
fig3 = px.bar(df3, x="Regiones", y="Casos")

app.layout = html.Div([

    html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig1
    )
]),

    html.Div(children=[
    dcc.Graph(
        id='example-graph1',
        figure=fig2
    )
]),

    html.Div(children=[
    dcc.Graph(
        id='example-graph2',
        figure=fig3
    )
]),

])

if __name__ == '__main__':
    app.run_server(debug=True)
