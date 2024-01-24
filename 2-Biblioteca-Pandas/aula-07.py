### SERIES: Indexação, Operações e Máscaras:

import numpy as np
import pandas as pd

## Series:
d = {'Python': 10, 'Java': 8, 'Matlab': 7, 'Scilab': 3,'JavaScript': 9, 'C++': 4, 'Go': 7, 'Rust': 2}

series = pd.Series(d)

print(f' {series} \n')

## Indexação:
#s = pd.Series(data=np.random.randint(1, 5, 10), index=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
s = pd.Series(data=np.random.randint(1, 5, 10), index='A B C D E F G H I J'.split())
print(f'{s} \n')

# OBS: Veremos exemplos que comprovam que os valores de uma Series podem ser acessados de mais de uma forma.
# VEJAMOS OS EXEMPLOS ABAIXO.
# utilizamos o índice igual a zero, ao invés de utilizarmos a letra A, que abilitamos como o verdadeiro índice da primeira posição...
print(f' {s[0]} \n')
print(f' {s['A']} \n')

# utilizando Series com slices:
print(f'{s[2:4]} \n')
print(f'{s['C':'D']} \n')
print(f'{series['Python':'JavaScript']} \n')

## Operações com Series:
s1 = pd.Series(data=np.random.randint(1, 100, 4), index='Facebook Instagram Youtube Whatsapp'.split())
s2 = pd.Series(data=np.random.randint(1, 100, 4), index='Telegram Instagram Youtube Whatsapp'.split())

print(f'{s1} \n')
print(f'{s2} \n')

print(f'{s1 + s2} \n')

## Máscaras em Series:
print(f'{s} \n')
print(f'Mostre as linhas que tenham valores maiores que 2 --> \n{s[s > 2]} \n')
print(f'Mostre os valores maiores que 2 --> \n{s[s > 2].values} \n')
print(f'Mostre os índices onde os valores são maiores que 2 --> \n{s[s > 2].index} \n')




