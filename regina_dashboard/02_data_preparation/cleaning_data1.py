import numpy as np
import pandas as pd


filepath = 'C:/Users/Edward/OneDrive/OneDrive - Universidad Tecnológica de Panamá/Projects/regina_dashboard/data_ingestion/BD COVID-19 PRELIMINAR ( MARTES 15 DE JUNIO 2021).xlsx'


"""
delete some columns from main dataset that it's doesn't matter
"""

dataset = pd.read_excel(io = filepath)  # main dataset
print(dataset.head())
to_drop = ['N', 'RESULTADO 2','RESULTADO 3', 'RESULTADO 4', 'RESULTADO 5','FECHA RESULTADO 3', 'FECHA RESULTADO 4', 'FECHA RESULTADO 5', 'FECHA RESULTADO 6',
           'UBICACIÓN EN HOSPITAL', 'HOSPITAL','OBSERVACION', 'FE+Q:AFCHA', 'FECHA DE DEFUNCION', 'FRIESGO DE RIESGO']

dataset.drop(to_drop, inplace=True, axis=1)
dataset = dataset.dropna()

"""
change the type of format to represents the age group
"""

print(dataset.head())
dataset['RESULTADO/LABORATORIO'] = 'POSITIVO'
dataset['GRUPO DE EDAD'].unique()
dataset['GRUPO DE EDAD'] = dataset['GRUPO DE EDAD'].str.replace('< 20 AÑOS', '0 - 19')
dataset['GRUPO DE EDAD'] = dataset['GRUPO DE EDAD'].str.replace('80 Y MAS', '80 - 107')
dataset['GRUPO DE EDAD'] = dataset['GRUPO DE EDAD'].str.replace('A', '-')
dataset['GRUPO DE EDAD'].unique()

"""
transform the ages to same time references in years
"""

for i, (age, age_type) in enumerate(zip(dataset['EDAD'], dataset['TIPOS_EDAD'])):
    if age_type == 'MESES':
        dataset['EDAD'][i] = age/12
    
    elif age_type == 'DIAS':
        dataset['EDAD'][i] = age/365


dataset.to_csv('dataset/BD_COVID19_PRELIMINAR_MARTES_15_DE_JUNIO_2021.csv', index = False)

