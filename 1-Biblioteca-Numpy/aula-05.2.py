## MÉTODOS DO OBJETO Array E MÁSCARAS

import numpy as np

array = np.random.randn(10)
print(f'{array}\n')

matrix = np.random.randn(3, 3)
print(f'{matrix}\n')

# Função ndim para sabermos a quantidade de dimensões do Array ou Matrix:
print(f'Quantidade de dimensões do array --> {array.ndim}')
print(f'Quantidade de dimensões da matrix --> {matrix.ndim}\n')

# Função shape para sabermos o shape de uma Array ou Matrix:
print(f'Shape do array --> {array.shape}')
print(f'Shape da matrix --> {matrix.shape}\n')

# Função que mostra o tipo de dado contigo dentro daquele Array ou Matrix:
print(f'Tipo de dados do array --> {array.dtype}')
print(f'Tipo de dados da matrix --> {matrix.dtype}\n')

# Método astype() para alterar o tipo de dado de determinado Array ou Matrix:
print(f'{array}\n')
print(f'Tipo de dados do array --> {array.dtype}')
print(f'... [[ Alterando o TIPO DE DADO do Array array acima ]] --> \n{array.astype('int')}\n')
print(f'{matrix}\n')
print(f'Tipo de dados da matrix --> {matrix.dtype}')
print(f'... [[ Alterando o TIPO DE DADO do Matrix matrix acima ]] --> \n{matrix.astype('int')}\n')
print(f'... [[ Alterando o TIPO DE DADO do Matrix matrix acima ]] --> \n{matrix.astype('bool')}\n')

# Métodos min() e max() que retornam os valores mínimo e máximo em meu Array ou Matrix:
print(f'Valor mínimo dentro do array --> {array.min()}\n')
print(f'Valor máximo dentro do array --> {array.max()}\n')

# Métoddos argmin() e argmax() que nos permite saber a posição do valor mínimo e valor máximo presentes no Array ou Matrix:
print(f'Valor mínimo dentro do array --> {array.argmin()}\n')
print(f'Valor máximo dentro do array --> {array.argmax()}\n')

# Método sort() de ordenação do Array ou Matrix:
print(f'Array --> {array}\n')
print(f'ORDENANDO O ARRAY acima ... \n')
array.sort()
print(f'Array ordenado --> \n{array}\n')

# Função T que calcula a transposta de uma matrix:
print(f'Matrix --> \n{matrix}\n')
print(f'Transposta da da Matrix matrix --> \n{matrix.T}\n')


## MÁSCARAS:
a = np.array([1, 2, 3, 4])

# vamos pegar apenas os elementos 2 e 4 da lista a acima:
# Criando a máscara a[[False, True, False, True]]
print(f'Elementos 2 e 4 da lista a --> \n{a[[False, True, False, True]]}\n')

print(f'Mostre a máscara com os valores maiores ou iguas a três do Array a: \n{a >= 3}\n')

# Utilizando a própria máscara do array como índice desse mesmo array:
print(f'Mostre os valores maiores ou iguais a 3 presentes no Array a --> \n{a[a >= 3]}\n')

# Retorne os elementos pares dentro do Array a:
print(f'Os elementos pares dentro do Array a --> \n{a[a % 2 == 0]}\n')


