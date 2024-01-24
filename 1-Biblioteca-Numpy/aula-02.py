import numpy as np

## Exemplo de array bidimensinal:
b = np.array([[0,1,2], [3,4,5]])
print(b)

# Como ver a quantidade de dimensões de um array com o método ndim:
print(b.ndim)

# Como saber quantas linhas e colunas um array com o método shape:
print(b.shape) # 2 linhas e 3 colunas

# como saber o tamanho de um array com a função len():
print(len(b))  # irá imprimir o número 2 na tela, pois está dizendo que tem duas linhas.

# Função arange() --> permite que você crie um array com um tamanho que você desejar de forma automática:
c = np.arange(0, 100, 2)
print(f'\n{c}\n')

c2 = np.arange(0, 10, 0.1)
print(f'{c2}\n')

c3 = np.arange(10)
print(f'{c3}\n')

c4 = np.arange(10, 20)
print(f'{c4}\n')

# Função lindspace() --> assim como a função arange(), podemos criar arrays com tamanhos prédefinados. A
# diferença é que aqui na função lindspace() nós dizemos quantos elementos queremos em determinado intervalo.
d = np.linspace(1, 10, 13)
print(f'{d}\n')

d2 = np.linspace(1, 10, 13, endpoint=False)
print(f'{d2}\n')

# Função ones() --> ela cria arrays de 1:
e = np.ones((5, 5))
print(f'{e}\n')