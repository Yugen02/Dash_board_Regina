from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import chart_studio

username = 'Yugen02'
api_key = 'Vvda56TicCWGrr6OLqd8'

chart_studio.tools.set_credentials_file(username=username,api_key=api_key)

import chart_studio as py
import chart_studio.tools as tls

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
df = pd.read_csv('https://raw.githubusercontent.com/Yugen02/Dash_board_Regina/master/regina_dashboard/02_data_preparation/Casos_Region_Exacta.csv')

app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

fig2 = px.scatter(df, x=df['Region'],
                     y=df['Casos'],size="Casos",color="Distrito",hover_name=df["Corregimiento"],
                     size_max=40)

py.plotly(fig2,filename = 'prueba',auto_open = True)


fig2.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
    )

fig2.update_yaxes(title='NUMERO DE CASOS')

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[

        html.H1(
        children='ANALISIS DEL NUMERO DE CASOS DE SARS-COVID19 POSITIVOS EN PANAMÁ',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),



        
    html.Div([
        dcc.Dropdown(
            sorted(df['Region'].unique()),
            'BOCAS DEL TORO',
            id='xaxis-column',
            style={
            'textAlign': 'center',
        }
        )
    ]
    ,style={'width': '45%', 'display': 'inline-block'}
    ),

    html.Div(children='LAURENTINO CORTIZO COEN PREZIDENTE', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

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

    fig = px.scatter(x=dff['Distrito'],
                     y=dff['Casos'],
                     size=dff['Casos'],
                     color=dff['Distrito'],
                     hover_name= dff['Corregimiento'],
                     size_max=35,
                     labels = {'x':'Distrito','y':'Casos','color':'Distrito','hover_name':'Corregimiento','size':'Casos'}
                     )

    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )

    fig.update_yaxes(title='NUMERO DE CASOS')

    fig.update_xaxes(title=xaxis_column_n)

    # fig.update_yaxes(title=[xaxis_column_n]['Casos'])

    return fig



if __name__ == '__main__':
    app.run_server(debug=True)