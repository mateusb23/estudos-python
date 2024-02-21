import numpy as np
import pandas as pd

np.random.seed(42)

dados = {
    'Massa corporal (kg)': np.random.randint(51, 160, 20),
    'Altura (cm)': np.random.randint(160, 202, 20),
    'Idade': np.random.randint(1, 103, 20),
    'COVID-19': np.random.choice(['SIM', 'NÃO'], size=20)
}

df = pd.DataFrame(dados)

df.to_csv('./datasets/pesquisa-covid.csv', index=False)
