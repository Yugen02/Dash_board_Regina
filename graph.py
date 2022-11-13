from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import chart_studio
import datetime

username = 'Yugen02'
api_key = 'Vvda56TicCWGrr6OLqd8'

chart_studio.tools.set_credentials_file(username=username,api_key=api_key)

import chart_studio as py
import chart_studio.tools as tls

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
df = pd.read_csv('https://raw.githubusercontent.com/Yugen02/Dash_board_Regina/master/regina_dashboard/02_data_preparation/Casos_Region_Exacta.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/Yugen02/Dash_board_Regina/master/regina_dashboard/02_data_preparation/dataset/BD_COVID19_PRELIMINAR_MARTES_15_DE_JUNIO_2021.csv')
del df2["Unnamed: 0"]

df2['DATE'] = pd.to_datetime(df2['FIS'], errors='coerce')

df2['MES'] = df2['DATE'].dt.month_name()
df2['SEMANA'] = df2['DATE'].dt.isocalendar().week



## LISTA DE DROP DOWN

drop_D = ['TIPO DE PACIENTE','EDAD','GRUPO DE EDAD','SEXO','REGION','DISTRITO','MES','SEMANA']



app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

fig2 = px.scatter(df, x=df['Region'],
                     y=df['Casos'],size="Casos",color="Distrito",hover_name=df["Corregimiento"],
                     size_max=40)

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
        
        html.Div([
            dcc.Dropdown(
                sorted(drop_D),
                'GRUPO DE EDAD',
                id='xaxis-column',
                style={
                'textAlign': 'center',
            }
            )
        ]
        ,style={'width': '45%', 'display': 'inline-block'}
        ),

        html.Div([
            dcc.Dropdown(
                sorted(drop_D),
                'SEXO',
                id='yaxis-column',
                style={
                'textAlign': 'center',
            }
            )
        ]
        ,style={'width': '45%', 'display': 'inline-block', 'padding': '0 20'})
    ], style={
        'padding': '10px 5px'
    }),






    html.Div(children='LAURENTINO CORTIZO COEN PREZIDENTE', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph1'
    )

])



def variables(variable_x, variable_y):
    data_X = []
    data_Y = []
    count = []
    for v_y in pd.unique(variable_y):
        for v_x in pd.unique(variable_x):
            df1 = df2.loc[(variable_x == v_x) & (variable_y == v_y)]
            rows = len(df1.axes[0])
            
            data_X.append(v_x)
            data_Y.append(v_y)
            count.append(rows) 
            # print(df1)
            # print("CASOS {}".format(rows))
    data_variables = pd.DataFrame({'Variable_x': data_X, 'Variable_Y': data_Y,
                            'Casos': count})
    return data_variables
    # print(data_variables)



@app.callback(
    Output('example-graph1', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'))

def update_graph(xaxis_column_n,yaxis_colum_n):

    datos = variables(df2[xaxis_column_n],df2[yaxis_colum_n])     
    # print(variables(xaxis_column_n,yaxis_colum_n))

    # dff = df[df['Region'] == xaxis_column_n]

    fig = px.scatter(datos, x=datos['Variable_x'],
                     y=datos['Casos'],
                     hover_name=datos['Variable_Y'],
                     color=datos['Variable_Y'], 
                     size_max=100,
                     labels = {'x':'x','y':'y','color':yaxis_colum_n,'hover_name':'Corregimiento'}
                     )

    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )

    fig.update_yaxes(title = 'NUMERO DE CASOS')

    fig.update_xaxes(title = xaxis_column_n)

    # fig.update_yaxes(title=[xaxis_column_n]['Casos'])

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)









