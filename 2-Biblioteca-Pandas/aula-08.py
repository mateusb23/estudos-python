### DataFrame: Criação e Indexação
# Basicamente, um DataFrame pode ser perfeitamente comparado a uma tabela do Excel, uma tabela do banco de dados OracleDB etc.

import pandas as pd
import numpy as np

dados = np.array([[72, 180, 26], [80, 170, 19], [60, 165, 15], [90, 187, 58]])
print(f'{dados} \n')

dataframe_1 = pd.DataFrame(data=dados, columns=['Peso', 'Altura', 'Idade'])
print(f'{dataframe_1} \n')

dataframe_2 = pd.DataFrame(data=dados, index=['A','B','C','D'], columns=['Peso', 'Altura', 'Idade'])
print(f'{dataframe_2} \n')

## Indexação em DataFrame:

## Retornando determinada(s) coluna(Series):
print(f'Mostre a coluna(Series) de Altura --> \n{dataframe_1['Altura']} \n')
print(f'Tipo da Coluna Altura do DataFrame dataframe_1: {type(dataframe_1['Altura'])} \n')

# Retornando apenas os valores de determinada coluna(Series):
print(f'Mostre os valores da coluna(Series) de Altura --> \n{dataframe_1['Altura'].values} \n')
print(f'Tipo dos valores de cada linha da coluna Altura do DataFrame dataframe_1: {type(dataframe_1['Altura'].values)} \n')

# Retornando apenas os valores de determinada coluna(Series):
print(f'Mostre os índices da coluna(Series) de Altura --> \n{dataframe_1['Altura'].index} \n')
print(f'Tipo dos índices de cada linha da coluna Altura do DataFrame dataframe_1: {type(dataframe_1['Altura'].index)} \n')

# Retornando duas ou mais colunas(Series) ao mesmo tempo:
print(f'Mostre as colunas Peso e Idade --> \n{dataframe_1[['Peso', 'Idade']]} \n')

## Retornando determinada(s) linhas:
print(f'Mostre a linha 1 do DataFrame dataframe_1 --> \n{dataframe_1.loc[1]} \n')
print(f'Tipo da linha 1 do DataFrame dataframe_1: {type(dataframe_1.loc[1])} \n')

print(f'Mostre a linha 1 do DataFrame dataframe_1 --> \n{dataframe_1.loc[1:3]} \n')

# Retornando determinados índices de Series:
print(f'{dataframe_1} \n')
print(f'Mostre o segundo elemento da linha 1 --> \n{dataframe_1['Altura'][1]} \n')
print(f'Mostre o segundo elemento da linha 1 --> \n{dataframe_1.loc[1][1]} \n')
print(f'Mostre o segundo elemento da linha 1 --> \n{dataframe_1.iloc[1,1]} \n')

