import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



## TIPO DE PACIENTE, EDAD, TIPOS_EDAD, SEXO, FIS, REGION, DISTRITO, CORREGIMIENTO, INSTALACION, RESULTADO/LABORATORIO
df = pd.read_csv('https://raw.githubusercontent.com/Yugen02/Dash_board_Regina/master/regina_dashboard/02_data_preparation/dataset/BD_COVID19_PRELIMINAR_MARTES_15_DE_JUNIO_2021.csv')
df['year'] = pd.DatetimeIndex(df['FIS']).year

print(df.head(30))

def variables(variable_x, variable_y):
    data_X = []
    data_Y = []
    count = []
    for v_y in pd.unique(variable_y):
        for v_x in pd.unique(variable_x):
            df1 = df.loc[(variable_x == v_x) & (variable_y == v_y)]
            rows = len(df1.axes[0])

            data_X.append(v_x)
            data_Y.append(v_y)
            count.append(rows) 
            # print(df1)
            # print("CASOS {}".format(rows))
    data_variables = pd.DataFrame({'Variable_x': data_X, 'Variable_Y': data_Y,
                            'Casos': count})
    return data_variables


print(variables(df['GRUPO DE EDAD'],df['SEXO']))

regiones = pd.unique(df['CORREGIMIENTO'])

count = []
D_reg = []
D_dis = []

for prov in regiones:
    df1 = df.loc[df['CORREGIMIENTO'] == prov]
    data_DISTRITO = df1.iloc[0,6]
    data_REGION = df1.iloc[0,5]

    D_reg.append(data_REGION)
    D_dis.append(data_DISTRITO)
    rows = len(df1.axes[0]) 
    count.append(rows)

# print(regiones)
# print(count)

data_regiones = pd.DataFrame({'Region': D_reg, 'Distrito':D_dis, 'Corregimiento': regiones,
                            'Casos': count})

print(data_regiones)

# data_regiones.to_csv(r'C:\Users\Efrain\Desktop\regina_dashboard\regina_dashboard\02_data_preparation\Casos_Region_Exacta.csv',index=False)
