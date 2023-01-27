import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


## TIPO DE PACIENTE, EDAD, TIPOS_EDAD, SEXO, FIS, REGION, DISTRITO, CORREGIMIENTO, INSTALACION, RESULTADO/LABORATORIO
df = pd.read_csv(r'C:\Users\Efrain\Desktop\regina_dashboard\regina_dashboard\02_data_preparation\Data_limpia.csv')
print(df.head(30))

regiones = pd.unique(df['CORREGIMIENTO'])

count = []
for prov in regiones:
    b = df['CORREGIMIENTO']
    df1 = df.loc[b == prov]
    rows = len(df1.axes[0]) 
    count.append(rows)

print(regiones)
print(count)

data_regiones = pd.DataFrame({'Regiones': regiones,
                            'Casos': count})

print(data_regiones)

data_regiones.to_csv(r'C:\Users\Efrain\Desktop\regina_dashboard\regina_dashboard\02_data_preparation\casos_CORREGIMIENTO.csv',index=False)
# print(df1.count())

