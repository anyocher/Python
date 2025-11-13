import pandas as pd

# Criar dados fictícios de vendas
dados = {
    'Venda': [1, 2, 3, 4, 5, 6, 7, 8],
    'Produto': ['Mouse', 'Teclado', 'Monitor', 'Mouse', 'Teclado', 'Cadeira', 'Notebook', 'Headset'],
    'Quantidade': [2, 3, 1, 5, 2, 1, 4, 2],
    'Valor_Unitario': [50, 150, 700, 50, 150, 500, 3000, 200]
}

# Criar DataFrame
df = pd.DataFrame(dados)

# Salvar como CSV
caminho_csv = "/mnt/data/vendas_exemplo.csv"
df.to_csv(caminho_csv, index=False)

caminho_csv
