### Analisando e Filtrando Dados

import pandas as pd
import numpy as np

dataframe_1 = pd.read_csv("./datasets/titanic_train.csv")
print(f'Mostre as 5 primeiras linhas do DataFrame sobre o Titanic --> \n{dataframe_1.head()} \n')

# Retornando uma lista contendo o nome de cada uma das colunas:
print(f'Retorne o nome de todas as colunas do DataFrame sobre o Titanic: \n{dataframe_1.columns} \n')

# Retornando a quantidade de índices que existe no DataFrame em questão:
print(f'Retorne quantidade de índices do DataFrame sobre o Titanic: \n{dataframe_1.index} \n')

## Método unique()
print(f'Retorne os valores únicos referentes à coluna de idades(age) no DataFrame sobre o Titanic ---> \n{dataframe_1['Age'].unique()} \n')

## Método value_counts()
# Retornando a quantidade de elementos referentes aos valores únicos.
print(f'Retornando a quantidade de pessoas do sexo masculino e feminino --> \n{dataframe_1['Sex'].value_counts()} \n')
print(f'Retornando a quantidade de pessoas para cada idade --> \n{dataframe_1['Age'].value_counts()} \n')

# Retornando a média de idade dos Passageiros do Titanic:
print(f'Retornando a média de idade dos Passageiros do Titanic --> \n{dataframe_1['Age'].mean()} \n')

## Como eliminar linhas duplicadas, retornando um novo DataFrame sem essas linhas duplicadas, caso realmente existam no tal:
# Verificar se existem linhas duplicadas em determinado DataFrame:
print(f'Retorne a quantidade de linhas duplicadas no DataFrame sobre o Titanic --> \n{dataframe_1.duplicated().sum()} \n')

# Eliminando as linhas duplicadas do DataFrame em questão, caso existam:
print(f'Eliminando DataFrame com linhas duplicadas e retornando um novo e corrigido ---> \n{dataframe_1.drop_duplicates()} \n')

### FILTRAGEM DE DADOS(MÁSCARAS):
print(f'Compare as idades maiores e menores que 25 anos do DataFrame sobre o Titanic --> \n{dataframe_1['Age'] > 25} \n')
print(f'Mostre apenas as linhas onde as idades são maiores que 25 anos do DataFrame sobre o Titanic --> \n{dataframe_1[dataframe_1['Age'] > 25]} \n')
print(f'Mostre apenas as linhas onde as idades são maiores que a média de idades do DataFrame sobre o Titanic --> \n{dataframe_1[dataframe_1['Age'] > dataframe_1['Age'].mean()]} \n')
print(f'Mostre apenas os dados sobre passageiros do sexo feminino ---> \n{dataframe_1[dataframe_1['Sex'] == 'female']} \n')
## Essa Filtragem de dados através das máscaras é muito útil, uma vez que conseguimos até atribuir essa filtragem a uma variável qualquer,
## que passará a ser considerado outro DataFrame. Exemplo:
dataframe_1_men = dataframe_1[dataframe_1['Sex'] == 'male']
print(f'Mostre apenas os dados sobre passageiros do sexo masculino ---> \n{dataframe_1_men} \n')

