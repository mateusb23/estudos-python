import pandas as pd
import numpy as np

# Criar dados aleatórios para Massa Corporal (kg) e Altura (cm)
np.random.seed(42)  # Para garantir reproducibilidade dos dados
dados = {
    'Massa Corporal (kg)': np.random.uniform(50, 100, 30),
    'Altura (cm)': np.random.uniform(150, 200, 30)
}

# Criar DataFrame
df = pd.DataFrame(dados)

# Salvar o DataFrame como um arquivo Excel (.xlsx)
df.to_excel('./datasets/peso-altura.xlsx', index=False)
