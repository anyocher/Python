import pandas as pd

# Dados fornecidos
data = {
    'Item': [1209, 1312, 1529, 1312, 2026, 1759, 1516, 1516, 1312, 1209],
    'Produto': ['Mouse', 'Teclado', 'Gabinete', 'Memoria', 'Gabinete', 'Memoria', 'Mouse', 'HD', 'Mouse', 'Mouse'],
    'Marca': ['R3', 'HP', 'Ship', 'Kingston', 'V12', 'Sandisk', 'Microsoft', 'Adata', 'Microsoft', 'Microsoft'],
    'Quantidade': [2, 3, 1, 2, 1, 1, 1, 2, 3, 1],
    'Preço Uni': [139.9, 39, 156, 250, 220, 99.9, 99.9, 219.9, 99.9, 99.9]
}

# Criação do DataFrame
df = pd.DataFrame(data)

print("-" * 50)

# a) Informe o Total por Venda
df['Total Venda'] = df['Quantidade'] * df['Preço Uni']
print("Total por Venda:\n", df[['Produto', 'Total Venda']])

print("-" * 50)
# b) Informe o Total de Vendas por Item
df_item = df.groupby('Item')['Total Venda'].sum()
print("\nTotal de Vendas por Item:\n", df_item)

print("-" * 50)

# c) Informe qual o nome do Produto mais Vendido
produto_mais_vendido = df.groupby('Produto')['Quantidade'].sum().idxmax()
print("\nProduto mais Vendido:", produto_mais_vendido)

print("-" * 50)

# d) Informe qual o nome do Produto mais Caro
produto_mais_caro = df.loc[df['Preço Uni'].idxmax(), 'Produto']
print("\nProduto mais Caro:", produto_mais_caro)

print("-" * 50)

# e) Informe o Total Geral de Vendas
total_geral_vendas = df['Total Venda'].sum()
print("\nTotal Geral de Vendas:", total_geral_vendas)

print("-" * 50)

# f) Informe as Vendas com o valor menor que 100
vendas_menor_100 = df[df['Total Venda'] < 100]
print("\nVendas com valor menor que 100:\n", vendas_menor_100[['Produto', 'Total Venda']])

print("-" * 50)

# g) Ordene as Vendas da Maior Quantidade Vendida para a Menor
df_sorted = df.sort_values(by='Quantidade', ascending=False)
print("\nVendas Ordenadas pela Maior Quantidade Vendida:\n", df_sorted[['Produto', 'Quantidade', 'Total Venda']])
