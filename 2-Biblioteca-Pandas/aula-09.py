### Lendo e salvando Datasets com Pandas (CSV, XLSX e HTML)
# OBS: Pode ser importante instalar os pacotes xlrd e openpyxl.

import pandas as pd
import numpy as np

## PARA ARQUIVOS .csv
dataframe_1 = pd.read_csv("./datasets/titanic_train.csv")

print(dataframe_1)

print(f'Mostre apenas as 15 primeiras linhas do DataFrame titanic_train.csv ---> \n{dataframe_1.head(15)} \n')
print(f'Mostre apenas as 10 últimas linhas do DataFrame titanic_train.csv ---> \n{dataframe_1.tail(10)} \n')

print(f'Mostre informações estatísticas sobre o DataFrame titanic_train.csv ---> \n{dataframe_1.describe()} \n')

## PARA ARQUIVOS .xlsx
dataframe_2 = pd.read_excel("./datasets/peso-altura.xlsx")

print(f'Me mostre as 8 primeiras linhas do DataFrame peso-altura.xslx ---> \n{dataframe_2.head(8)} \n')

print(f'O Shape do DataFrame peso-altura.xslx : {dataframe_2.shape} \n')

# COMO CONVERTER um aquivo .xslx para .csv:
print('----- CONVERTENDO PLANILHA PRA O FORMATO .csv  ... \n')
dataframe_2.to_csv("./datasets/peso-altura.csv")

# COMO CONVERTER um arquivo .csv para .xslx:
#print('----- CONVERTENDO PLANILHA PRA O FORMATO .xslx  ... \n')
#dataframe_1.to_excel("./datasets/titanic_train.xslx")

## PARA ARQUIVOS IMPORTADOS DA Web:
dataframe_3 = pd.read_html("https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/")
print(dataframe_3)
print('------------------------------------------------------------------------------------------------------------------------------------------- \n')
print(f'{dataframe_3[0]} \n')
print(f'{len(dataframe_3)} \n')