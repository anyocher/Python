import pandas as pd

# Dados fornecidos
dados = {
    'Item': [1209, 1312, 1529, 1312, 2026, 1759, 1516, 1516, 1312, 1209],
    'Produto': ['Mouse', 'Teclado', 'Gabinete', 'Memoria', 'Gabinete', 'Memoria', 'Mouse', 'HD', 'Mouse', 'Mouse'],
    'Marca': ['R3', 'HP', 'Ship', 'Kingston', 'V12', 'Sandisk', 'Microsoft', 'Adata', 'Microsoft', 'Microsoft'],
    'Quantidade': [2, 3, 1, 2, 1, 3, 1, 2, 3, 1],
    'Preço Uni': [139.9, 39, 156, 250, 220, 99.9, 99.9, 219.9, 99.9, 99.9]
}

# Criação do DataFrame
df = pd.DataFrame(dados)
df['Total Venda'] = df['Quantidade'] * df['Preço Uni']



def valorfinal():
    