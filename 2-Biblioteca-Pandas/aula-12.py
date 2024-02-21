### TRATAMENTO DE DADOS AUSENTES DO DATAFRAME

import pandas as pd
import numpy as np

dados = np.array([[1,      2, np.nan],
                  [4, np.nan, np.nan],
                  [7,      8,      9]])

df = pd.DataFrame(dados, columns='A B C'.split())

print(f'{df} \n')

## Método isnull() 
## esse método vai retornar uma espécie de máscara, com True quando o valor for nulo e False quando o valor for diferente de nulo.
print(f'{df.isnull()} \n')

# Verificando se tem valores nulos na coluna A:
print(f'{df["A"].isnull()} \n')
# Verificando se tem valores nulos na coluna B:
print(f'{df["B"].isnull()} \n')

# Saber quantos valores nulos temos em nosso DataFrame:
print(f'Quantidade de valores nulos em cada coluna do DataFrame: \n{df.isnull().sum()} \n')

## Método dropna()
## ele sozinho vai eleiminar/remover a linha que tenha algum valor nulo. Basta que algum coluna tenha um valor nulo, que a linha toda será removida.
print(f'{df.dropna()} \n')

# usando o método dropna() para excluir a coluna onde está o valor nulo. No exemplo abaixo iremos excluir a coluna 1(coluna A), caso ela tenha algum valor nulo.
print(f'{df.dropna(axis=1)} \n')

## Método fillna()
## ele sozinho vai preencher os locais nulos que existirem no DataFrame.

# Preenchendo como zero(0) os valores nulos na coluna B do DataFrame, caso existam:
print(f'f{df["B"].fillna(0)} \n')

# Atualizando a coluna B com os valores nulos preenchidos com zero:
df["B"] = df["B"].fillna(0)
print(f'Valores atualizados da coluna B: \n{df["B"]} \n')

# Preenchendo todos valores nulos do DataFrame com zero(0):
print(f'{df.fillna(0)} \n')

df["B"][1] = np.nan

# Preenchendo com o valor anterior na coluna onde está nulo.
print(f'{df.fillna(method="ffill")} \n')

# Preenchendo com o valor posterior na coluna onde está nulo.
print(f'{df.fillna(method="bfill")} \n')


## APLICANDO ESSE CONHECIMENTO NOS DADOS DO TITANIC:
df = pd.read_csv("./datasets/titanic_train.csv")
print(f'Tabela de dados do Titanic: \n{df}\n')

# Vendo quais são nulos em nosso DataFrame do Titanic:
print(f'Vendo quais são nulos em nosso DataFrame do Titanic: \n{df.isnull()} \n')

# Saber quantos valores nulos temos em nosso DataFrame do Titanic:
print(f'Quantidade de valores nulos em cada coluna do DataFrame do Titanic: \n{df.isnull().sum()} \n')

# OBS: conforme podemos ver no retorno do comando da linha 63, a coluna Cabin (Cabine) tem 687 valores nulos.
#      ou seja, 77% dos valores dessa coluna são nulos. Dessa forma, temos essa coluna como sendo irrelevante
#      para as nossas análises. A partir disso, o aconselhado é removê-la do DataFrame.
df.drop('Cabin', axis=1, inplace=True)
print(f'{df.isnull().sum()} \n')

# quantificando cada um dos elementos distintos da Series(coluna) Embarked:
print(f'Quantificando cada um dos elementos distintos da Series(coluna) Embarked: \n{df["Embarked"].value_counts()} \n')

# Preenchendo os valores nulos da coluna Embarked com o valor que mais aparece na coluna em si e atualizar o DataFrame também com o inplace=True:
df["Embarked"].fillna("S", inplace=True)
print(f'Preenchendo os valores nulos da coluna Embarked com o valor que mais aparece na coluna em si: \n{df} \n')
print(f'{df.isnull().sum()} \n')

# OBS: conforme podemos notar, a Coluna Age (idade) ainda tem 177 valores nulos, aproximadamente 20% dos valores. A partir disso, a decisão
#      mais aconselhada seria adicionar nos locais com valores nulos justamente o valor da média da coluna Age.
print(f'Média da coluna Age: {df["Age"].mean()} \n')
media_idade = df["Age"].mean()
df["Age"].fillna(media_idade, inplace=True)
print(f'Preenchendo os valores nulos da coluna Age com o valor da média da coluna em si: \n{df} \n')
print(f'{df.isnull().sum()} \n')
