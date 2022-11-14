from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import chart_studio
import datetime

df2 = pd.read_csv('https://raw.githubusercontent.com/Yugen02/Dash_board_Regina/Efrain/regina_dashboard/02_data_preparation/dataset/BD_COVID19_PRELIMINAR_MARTES_15_DE_JUNIO_2021.csv')

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
    data_variables = pd.DataFrame({'x': data_X, 'y': data_Y,
                            'Casos': count})
    data_variables = data_variables.sort_values(by=['x'])
    return data_variables
    # print(data_variables)


datos = variables(df2['REGION'],df2['SEXO'])


lat = [9.4165,9.4165, 8.3971129,8.3971129,8.4604873,8.4604873,9.3553005,9.3553005,8.2158991,8.2158991,9.057822904338451,9.057822904338451,7.8432774,7.8432774,7.8773471,7.8773471,8.999729497842978,8.999729497842978,8.48621,8.48621,9.0329592,9.0329592,9.078862,9.078862,8.9898564,8.9898564,9.0551061,9.0551061,8.2414131,8.2414131]
lon= [-82.5207,-82.5207,-82.3223443,-82.3223443,-80.4305652,-80.4305652,-79.8974085,-79.8974085,-78.0172551,-78.0172551,-77.89447750948364,-77.89447750948364,-80.7587705,-80.7587705,-80.4290617,-80.4290617,-79.51171356618619,-79.51171356618619,-81.73081,-81.73081,-79.4710178,-79.4710178,-79.4719702,-79.4719702,-79.6793267,-79.6793267,-79.4933063,-79.4933063,8.2414131,8.2414131]

datos.insert(3, "Longitud", lon, True)
datos.insert(4, "Latitud", lat, True)
# print(datos)

px.set_mapbox_access_token('pk.eyJ1IjoieXVnZW4wMiIsImEiOiJjbGFnMHJiY3AwdWlrM25vOXRwMG1uaHA1In0.6nnPpOKyl5QsmfGBNcb75Q')

fig = px.scatter_mapbox(datos,
                        lon = datos['Longitud'],
                        lat = datos['Latitud'],
                        zoom = 5,
                        hover_name=datos['y'],
                        color = datos['x'],
                        size = datos['Casos'],
                        size_max=75
                        )



fig.show()