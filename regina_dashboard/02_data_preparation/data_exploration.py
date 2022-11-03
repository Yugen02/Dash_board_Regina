import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filepath = 'C:/Users/Edward/OneDrive - Universidad Tecnológica de Panamá/Projects/regina_dashboard/01_data_ingestion/BD COVID-19 PRELIMINAR ( MARTES 15 DE JUNIO 2021).xlsx'


dataset = pd.read_excel(io = filepath)
sns.set_theme(style="darkgrid")
fig, ax = plt.subplots(figsize = (30, 30))
sns.histplot(data = dataset, x ="RESULTADO 2", y="EDAD")
