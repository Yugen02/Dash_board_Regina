import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df2 = pd.read_csv('https://raw.githubusercontent.com/Yugen02/Dash_board_Regina/Efrain/regina_dashboard/02_data_preparation/dataset/BD_COVID19_PRELIMINAR_MARTES_15_DE_JUNIO_2021.csv')


def locations(variable_x, variable_y, dataframe):
    data_X = []
    data_Y = []
    count = []
    for v_y in pd.unique(variable_y):
        for v_x in pd.unique(variable_x):
            df1 = dataframe.loc[(variable_x == v_x) & (variable_y == v_y)]
            rows = len(df1.axes[0])

            data_X.append(v_x)
            data_Y.append(v_y)
            count.append(rows) 
            # print(df1)
            # print("CASOS {}".format(rows))
    data_variables = pd.DataFrame({'REGION': data_X, 'Variable_Y': data_Y,
                            'Casos': count, 'Lat':lat, 'Lon':lon})
    return data_variables

# locations(df2['REGION'],df2['SEXO'],df2)


df = pd.read_csv('C:\Users\Efrain\Desktop\Dash_board_Regina\region_location.csv')

locations(df2['REGION'],df2['SEXO'],df2)
