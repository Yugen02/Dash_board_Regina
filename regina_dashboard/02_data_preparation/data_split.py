import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


## TIPO DE PACIENTE, EDAD, TIPOS_EDAD, SEXO, FIS, REGION, DISTRITO, CORREGIMIENTO, INSTALACION, RESULTADO/LABORATORIO
df = pd.read_csv(r'C:\Users\Efrain\Desktop\regina_dashboard\regina_dashboard\02_data_preparation\Data_limpia.csv')
df['year'] = pd.DatetimeIndex(df['FIS']).year

print(df.head(30))




regiones = pd.unique(df['CORREGIMIENTO'])

count = []
D_reg = []
D_dis = []

for prov in regiones:
    lugar = df['CORREGIMIENTO']
    df1 = df.loc[lugar == prov]
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
