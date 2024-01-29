### CRIANDO E REMOVENDO COLUNAS DO DataFrame

import numpy as np
import pandas as pd
from random import choice

dataframe = pd.read_excel("./datasets/peso-altura.xlsx")

print(f"-- Primeiras cinco linhas do DataFrame em questão: \n{dataframe.head()} \n")

print(f"-- Mostre o Shape(linhas, colunas) desse DataFrame: \n{dataframe.shape} \n")

## Gerando um Array com 30 idades descritas por números inteiros entre 17 e 40:
idade = np.random.randint(17, 40, 30)
print(f"\n {idade} \n")

# jogando o Array idade para dentro do DataFrame que está com os dados de peso e altura.
# quando colocamos entre aspas simples o nome 'Idade', estamos dizendo que este Array que
# estamos jogando para dentro do DataFrame será uma coluna do mesmo, e com o nome Idade.
dataframe['Idade'] = idade
print(f"--> Mostrando como ficou o DataFrame, após a inclusão do Array idade no tal: [5 PRIMEIRAS LINHAS DO DATAFRAME] \n{dataframe.head()} \n")

## Gerando um Array com 30 sexo descritas por strings que variam entre M ou F:
# Será utilizada a função choice([]) que vai basicamente pegar os valores do Array que
# colocarmos entre seus parênteses e vai escolher aleatorimente entre eles. 
sexo = [choice(['M', 'F']) for i in range(30)]
print(f"\n {sexo} \n")

# jogando o Array sexo para dentro do DataFrame que está com os dados de peso e altura e idade.
dataframe['Sexo'] = sexo
print(f"--> Mostrando como ficou o DataFrame, após a inclusão do Array sexo no tal: \n{dataframe} \n")

## Como deletar uma coluna do DataFrame:
# Excluindo a coluna 'Altura (cm)' da amostragem:
print(f"--> DataFrame peso, idade e sexo: \n{dataframe.drop('Altura (cm)', axis=1)} \n")

# Atualizando o DataFrame, após a remoção da coluna 'Altura (cm)':
# dataframe = dataframe.drop('Altura (cm)', axis=1)
# OU ------------------------
# simplesmente podemos utilizar o parâmetro inplace=True. Esse parâmetro diz que o python
# já pode pegar essa atualização e jogá-la automaticamente dentro do DataFrame atualizado, sem
# que seja necessário atribuirmo novamente à variável dataframe. Exemplo:
dataframe.drop('Altura (cm)', axis=1, inplace=True)

print(f"Mostrando como ficou DataFrame: \n{dataframe} \n")