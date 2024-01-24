## MOSTRANDO OPERAÇÕES COM ARRAYS DA BIBLIOTECA NUMPY

import numpy as np

# vai garantir que as sequências aleatórias de números gerados sempre sejam as mesmas, a cada execução do script.
np.random.seed(32)

a1 = np.ones(10)

print(a1)
print(a1 * 10)
print(a1 / 2)
print(a1 + 2)
print((a1+3)**2)

a2 = np.random.randint(1, 20, 8)

print(a2)

a3 = np.random.randint(1, 100, 8)

print(f'{a3}\n')

## vejamos com é a soma entre os Arrays a2 e a3:
# OBS: ISSO SÓ TORNA-SE POSSÍVEL POR a2 E a3 TEREM A MESMA NATUREZA E TAMANHO, SENDO ARRAYS 
# DE 8 ELEMENTOS E UNIDIMENSIONAIS. SE FOSSE UMA SOMA ENTRE OS ARRAYS a1 e a2, DARIA UM ERRO
# NA TELA, POIS SÃO ARRAYS DE NATUREZAS E TAMANHOS DIFERENTES.
print(f'{a2 + a3}\n')

## MULTIPLICAÇÃO ENTRE MATRIZES:
# OBS: é importante ressaltarmos que só é possível multiplicarmos matrizes, quando o número
# colunas da primeira matriz seja igual ao número de linhas da segunda.
# A matriz resultante será uma que tenha o número de linhas da primeira e o número de 
# colunas da segunda.
# Exemplo de matrizes: (3 x 2) x (2 x 3) = (3 x 3)

m1 = np.random.randint(1, 10, (3, 2))
print(f'{m1}\n')

m2 = np.random.randint(1, 10, (2, 3))
print(f'{m2}\n')

# É ASSIM QUE MULTIPLICAMOS MATRIZES NO PYTHON:
print(f'{m1.dot(m2)}\n')


## COMPARAÇÕES:
a4 = np.array([1, 2, 2, 1])
a5 = np.array([3, 2, 3, 1])

# Essa forma de comparação vai comparar cada um dos elementos e imprimir uma matriz
# dizendo se cada um dos índices é igual ou não ao da outra matriz.
print(f'Comparação entre cada elemento dos Arrays a4 e a5 --> \n{a4 == a5}\n')

print(f'Comparação completa entre os Arrays a4 e a5 --> \n{np.array_equal(a4, a5)}\n')

# Funções trigonométricas:
print(f'Seno de cada um dos índices do Array a4 --> \n{np.sin(a4)}')

# Função de soma em Arrays:
print(f'Soma de todos os valores do Array a5 --> \n{np.sum(a5)}\n')

# Função da média em Arrays:
print(f'Média de todos os valores do Array a5 --> \n{np.mean(a5)}\n')

# Função da variância em Arrays:
print(f'Variância de todos os valores do Array a5 --> \n{np.var(a5)}\n')

# Função do desvio padrão em Arrays:
print(f'Desvio padrão de todos os valores do Array a5 --> \n{np.std(a5)}\n')
