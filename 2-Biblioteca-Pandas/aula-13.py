### AGRUPANDO DADOS DE UM DataFrame

import pandas as pd
import numpy as np

df = pd.read_csv('./datasets/pesquisa-covid.csv')

print(f'{df.head()}')