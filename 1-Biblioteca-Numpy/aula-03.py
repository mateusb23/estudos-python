### INDEXAÇÃO E CORTES DE ARRAYS
import numpy as np

a = np.arange(10, 21)
print(a)
print(f'Primeiro elemento do Array a --> {a[0]}\n')
print(f'Último elemento do Array a --> {a[-1]}\n')

# Criando um array bidimensional de números aleatórios:
b = np.random.rand(5, 5)
print(f'Array bidimensional 5x5 com valores aleatórios: \n{b}\n')
# Acessando uma linha inteira do Array bidimensional que criamos anteriormente:
print(f'Primeira linha do Array bidimensional b --> \n{b[0]}\n')
# Acessando um elemento de acordo com a sua localização (linha, coluna) no Array que criamos:
print(f'Segundo elemento da primeira linha do Array bidimensional b --> \n{b[0, 1]}\n')
# OU
print(f'Segundo elemento da primeira linha do Array bidimensional b --> \n{b[0][1]}\n')
# Alterando o valor de um elemento do Array bidimensional b, que criamos anteriormente:
b[0, 1] = 10
print(f'Após alteração do segundo elemento da primera linha, mostre o Array bidimensional b --> \n{b}\n')

## Slices de Arrays unidimensionais:
# imprimindo o Array unidimensional a:
print(f'Array unidimensional a --> \n{a}\n')
# Exemplo de slice em Array unidimensional:
print(f'Slice do Array a contendo o intervalo do elemento 2 ao 4 --> \n{a[2:5]}\n')
# Outro exemplo de slice em Array unidimensional:
print(f'Slice do Array a contendo intervalo do elemento 0 ao 4 --> \n{a[:5]}\n')
# Outro exemplo de slice em Array unidimensional:
print(f'Slice do Array a contendo intervalo do elemento 3 ao -1(último) --> \n{a[3:]}\n')

## Slices de Arrays bidimensionais:
# imprimindo o Array bidimensional b:
print(f'Array bidimensional  --> \n{b}\n')
# Slice contendo as duas primeiras linhas do Array bidimensional b:
print(f'Slice contendo as duas primeiras linhas do Array bidimensional b \n{b[0:2]}\n')
# Slice contendo as terceiras colunas das duas primeiras linhas do Array bidimensional b:
print(f'contendo as terceiras colunas das duas primeiras linhas do Array bidimensional b --> \n{b[0:2, 2]}\n')

# Pulando elementos de uma Array com intervalos diferentes de 1: 
print(f'Array unidimensional a --> \n{a}\n')
print(f'Faixa de valores do elemento 2 ao 8 no Array A --> \n{a[2:9]}\n')
print(f'Pulando de 2 em 2 elementos no Array a --> \n{a[2:9:2]}\n')
print(f'Pulando de -1 em -1 elementos no Array a --> \n{a[8:2:-1]}\n')

