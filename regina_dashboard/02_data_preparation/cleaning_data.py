import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib 

# filepath = 'C:\Users\Efrain\Desktop\regina_dashboard\regina_dashboard\01_data_ingestion\BD COVID-19 PRELIMINAR ( MARTES 15 DE JUNIO 2021).xlsx'


df = pd.read_csv(r'C:\Users\Efrain\Desktop\regina_dashboard\regina_dashboard\01_data_ingestion\Datos_pandas.csv')
print(df)
b = df['RESULTADO/LABORATORIO']
df = df.loc[b == 'DETECTADO']
df2 = df.dropna(subset=['RESULTADO/LABORATORIO'])

df2 = df2.drop(['FE+Q:AFCHA','RESULTADO 2','FECHA RESULTADO 3','RESULTADO 3','FECHA RESULTADO 4','RESULTADO 4','FECHA RESULTADO 5','RESULTADO 5','FECHA RESULTADO 6','OBSERVACION','FRIESGO DE RIESGO','FECHA DE DEFUNCION','UBICACIÓN EN HOSPITAL','HOSPITAL','GRUPO DE EDAD','SE','Unnamed: 0','N'], axis=1)

df2 = df2.dropna()
# ['OBSERVACION','FRIESGO DE RIESGO','UBICACIÓN EN HOSPITAL','HOSPITAL']

# print(df.dtypes)
a = pd.unique(df['REGION'])

print(df2)

df2.to_csv(r'C:\Users\Efrain\Desktop\regina_dashboard\regina_dashboard\02_data_preparation\Data_limpia.csv',index=False)

def casos_region(variable):
    a = 0






# plt.figure(1)
# plt.bar(df['RESULTADO/LABORATORIO'],df['REGION'])
# # plt.xlabel("Weeks")
# # plt.ylabel("Number of Tweets")
# plt.title('Total of Tweets 2020 - 2021')
# # plt.legend()
# plt.show()



# sns.set_theme(style="darkgrid")
# fig, ax = plt.subplots(figsize = (30, 30))
# sns.histplot(data = dataset, x ="RESULTADO 2", y="EDAD")