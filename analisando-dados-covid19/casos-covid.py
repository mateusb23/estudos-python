### CASOS CONFIRMADOS DE COVID-19

import pandas as pd
from urllib.request import urlretrieve
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
print(f'{urlretrieve(url, './datasets/global_cases_covid19.csv')}\n')

# Criando o DataFrame:
df_covid = pd.read_csv('./datasets/global_cases_covid19.csv')

# Imprimindo "todo" o DataFrame df_covid:
print(f'{df_covid}\n')
print(f'{type(df_covid)}\n')

# Imprimindo apenas as cinco primeiras linhas do DataFrame df_covid:
print(f'{df_covid.head()}\n')

# Acessando colunas do DataFrame df_covid. Essas colunas são retornadas em series, que são muito semelhantes a Arrays.:
print(f' {df_covid['Lat']} \n')

# Método drop() para excluir determinados conteúdos do nosso DataFrame df_covid:
# --> Excluindo as colunas Lat e Long do nosso DataFrame df_covid:
# print(f'{df_covid.drop(['Lat', 'Long'], axis=1)}')  # o parâmetro axis é a linha, onde 0 seria referente à linhas e 1 referente à colunas.
# OBS: Quando solicitarmos para imprimir novamente o DataFrame com print(df_covid), isso vai nos retornar o DataFrame original, sem a
# alteração da remoção das duas colunas que fizemos na linha 25. Porém, para contornar isso, podemos atribuir o conteúdo que já criamos,
# com o parâmetro inplace=True . Isso vai garantir que o DataFrame será modificado e atualizado de acordo com essa alteração, de fato.
df_covid.drop(['Lat', 'Long'], axis=1, inplace=True)

print(f'{df_covid} \n')

# Agrupando dados do DataFrame, criando DataSets:
df_country = df_covid.groupby('Country/Region').sum()
print(f' {df_country} \n')

# Acessando linhas do DataFrame df_country.
print(f' {df_country.loc['Brazil']} \n')

# Criando novas variáveis chamadas date e cases, que vão armazenar as datas e casos da linha Brazil:
date = df_country.loc['Brazil'].index
cases = df_country.loc['Brazil'].values

print(f' {date} \n')
print(f' {cases} \n')

## Plotando um gráfico de colunas com a biblioteca MatPlotlib:
# plt.figure(figsize=(14,8))
# plt.bar(date, cases)
# plt.show()

# Criando uma series só para o Brasil, ou seja, vamos pegar os dados referentes a apenas uma linha do DataFrame em questão:
s_brazil = df_country.loc['Brazil']
print(f' {s_brazil} \n')

# Mostrando o s_brazil era maior que zero. Ou seja, nessa vizualização queremos apenas os dias no Brasil que não estejam com casos iguais a zero. 
print(f' {s_brazil[s_brazil > 0]} \n')

# Mostrando os índices da series Brazil que chamamos por s_brazil
print(f' {s_brazil.index} \n')

# Mostrando os valores diferentes de zero na series s_brazil de uma forma diferente:
print(f' {s_brazil.values} \n')

## Plotando casos e datas no Brasil com a biblioteca Matplotlib:
tam = len(s_brazil)
plt.figure(figsize=(14,8))
plt.xticks(rotation=60)
plt.bar(s_brazil.index[tam-40:tam], s_brazil.values[tam-40:tam])
plt.title('Total de casos confirmados de COVID-19, nos últimos 40 dias no Brasil')
plt.show()





