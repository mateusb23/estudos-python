### INTRODUÇÃO AO PANDAS E SERIES
import numpy as np
import pandas as pd

## Series --> é uma linha ou uma coluna do DataFrame(tabela). Embora possa parecer que esse objeto
# é idêntico a um Numpy Array, ele possui atributos, os quais vamos estudar agora.

# Criando uma Series:
steps = pd.Series([4216, 3867, 7934, 4180, 5344])
print(f' {steps} \n')
print(f'Tipo da Series steps: {type(steps)} \n')

print(f'Valores da Series steps --> \n {steps.values} \n')

print(f'Índices da Series steps --> \n {steps.index} \n') # vai nos retornar uma notação informando que foi criado um range de 0 a 5 pulando de 1 em 1.

# Substituindo os índices da Series steps por dias da semana:
steps = pd.Series(data=[4216, 3867, 7934, 4180, 5344], index=['seg','ter','qua','qui','sex'])
print(f'{steps} \n')

print(f'Índices da Series steps (Após a alteração nos índices) --> \n {steps.index} \n')

print(f' Retornando o menor valor da Series steps --> {steps.min()} \n')
print(f' Retornando o maior valor da Series steps --> {steps.max()} \n')
print(f' Retornando a média dos valores da Series steps --> {steps.mean()} \n')
print(f' Retornando a soma dos valores da Series steps --> {steps.sum()} \n')

# Mostrando conjunto de cálculos feitos com base na Series steps:
print(f' Retornando um conjunto de vários cálculos acerca da Series steps ---> {steps.describe()} \n')

# Multiplicando os valores da Series steps por 2:
print(f' Multiplicando os valores da Series steps por 2 --> \n{steps * 2} \n')

# Aplicando as funções da Biblioteca Numpy dentro da series:
print(f' Mostrando a raiz quadrada de cada um dos valores da Series steps --> \n{np.sqrt(steps)} \n')
