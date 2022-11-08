from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
df = pd.read_csv(r'C:\Users\Efrain\Desktop\regina_dashboard\regina_dashboard\02_data_preparation\Casos_Region_Exacta.csv')

app = Dash(__name__)
fig2 = px.scatter(df, x=df['Region'],
                     y=df['Casos'],size="Casos",color="Distrito",hover_name=df["Corregimiento"],
                     size_max=40)
app.layout = html.Div([

        
    html.Div([
        dcc.Dropdown(
            sorted(df['Region'].unique()),
            'BOCAS DEL TORO',
            id='xaxis-column'
        )
    ]
    ,style={'width': '45%', 'display': 'inline-block'}
    ),


    dcc.Graph(
        id='example-graph1'
    ),

    dcc.Graph(
        id='example-graph2',
        figure=fig2
    )

])



@app.callback(
    Output('example-graph1', 'figure'),
    Input('xaxis-column', 'value'))

def update_graph(xaxis_column_n):
                 
    dff = df[df['Region'] == xaxis_column_n]

    fig = px.scatter(x=df[df['Region'] == xaxis_column_n]['Distrito'],
                     y=dff['Casos'],
                     size=dff['Casos'],
                     color=dff['Distrito'],
                     hover_name= dff['Corregimiento'],
                     size_max=35,
                     labels = {'x':'Distrito','y':'Casos','color':'Distrito','hover_name':'Corregimiento','size':'Casos'}
                     )

    fig.update_traces(text='Distrito', selector=dict(type='scatter'))

    fig.update_yaxes(title='Numero de Casos')

    fig.update_xaxes(title=xaxis_column_n)

    # fig.update_yaxes(title=[xaxis_column_n]['Casos'])

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)