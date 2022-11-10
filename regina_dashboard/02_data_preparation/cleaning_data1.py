import numpy as np
import pandas as pd


filepath = 'C:/Users/Edward/OneDrive - Universidad Tecnológica de Panamá/Projects/regina_dashboard/01_data_ingestion/BD COVID-19 PRELIMINAR ( MARTES 15 DE JUNIO 2021).xlsx'


dataset = pd.read_excel(io = filepath)
print(dataset.head())
to_drop = ['N', 'RESULTADO 2','RESULTADO 3', 'RESULTADO 4', 'RESULTADO 5','FECHA RESULTADO 3', 'FECHA RESULTADO 4', 'FECHA RESULTADO 5', 'FECHA RESULTADO 6',
           'UBICACIÓN EN HOSPITAL', 'HOSPITAL','OBSERVACION', 'FE+Q:AFCHA', 'FECHA DE DEFUNCION', 'FRIESGO DE RIESGO']

dataset.drop(to_drop, inplace=True, axis=1)
dataset = dataset.dropna()

print(dataset.head())
dataset['RESULTADO/LABORATORIO'] = 'POSITIVO'
dataset['GRUPO DE EDAD'].unique()
dataset['GRUPO DE EDAD'] = dataset['GRUPO DE EDAD'].str.replace('< 20 AÑOS', '< 20')
dataset['GRUPO DE EDAD'] = dataset['GRUPO DE EDAD'].str.replace('80 Y MAS', '> 80')
dataset['GRUPO DE EDAD'] = dataset['GRUPO DE EDAD'].str.replace('A', '-')
dataset['GRUPO DE EDAD'].unique()

dataset.to_csv('dataset/BD_COVID19_PRELIMINAR_MARTES_15_DE_JUNIO_2021.csv')

