import pandas as pd
import matplotlib.pyplot as plt

# Leitura dos dados (arquivo CSV criado anteriormente)
try:
    df = pd.read_csv("vendas_exemplo.csv")
    print(" Arquivo carregado com sucesso!\n")
except FileNotFoundError:
    print("Erro: O arquivo 'vendas_exemplo.csv' não foi encontrado.\n")
    exit()

# Exibir primeiras linhas
print(" Dados iniciais:\n", df.head(), "\n")

# a) Total por Venda
df['Total_Venda'] = df['Quantidade'] * df['Valor_Unitario']
print(" a) Total por Venda:")
print(df[['Venda', 'Produto', 'Quantidade', 'Valor_Unitario', 'Total_Venda']], "\n")

# b) Total de Vendas por Item
total_por_item = df.groupby('Produto')['Total_Venda'].sum().sort_values(ascending=False)
print(" b) Total de Vendas por Item:")
print(total_por_item, "\n")

# c) Produto mais Vendido (por quantidade)
mais_vendido = df.groupby('Produto')['Quantidade'].sum().idxmax()
qtd_mais_vendida = df.groupby('Produto')['Quantidade'].sum().max()
print(f" c) Produto mais Vendido: {mais_vendido} ({qtd_mais_vendida} unidades)\n")

# d) Produto mais Caro (maior valor unitário)
produto_mais_caro = df.loc[df['Valor_Unitario'].idxmax()]
print(f" d) Produto mais Caro: {produto_mais_caro['Produto']} - R$ {produto_mais_caro['Valor_Unitario']:.2f}\n")

# e) Total Geral de Vendas
total_geral = df['Total_Venda'].sum()
print(f"e) Total Geral de Vendas: R$ {total_geral:.2f}\n")

# f) Vendas com valor menor que R$100
vendas_menor_100 = df[df['Total_Venda'] < 100]
print(" f) Vendas com valor menor que R$100:")
if vendas_menor_100.empty:
    print("Nenhuma venda com valor menor que R$100.\n")
else:
    print(vendas_menor_100[['Venda', 'Produto', 'Total_Venda']], "\n")

# g) Ordenar da maior quantidade vendida para menor
ordenado = df.sort_values(by='Quantidade', ascending=False)
print(" g) Vendas ordenadas da maior para a menor quantidade:\n", ordenado, "\n")


#  Gráfico: Total de vendas por produto
plt.figure(figsize=(10, 6))
plt.bar(total_por_item.index, total_por_item.values, color='#63E7D5', edgecolor='#051127')
plt.title('Total de Vendas por Produto', fontsize=14, color='#17213E', weight='bold')
plt.xlabel('Produto', fontsize=12)
plt.ylabel('Total de Vendas (R$)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.xticks(rotation=45)
plt.tight_layout()

# Mostrar o gráfico
plt.show()

print("ANÁLISE CONCLUÍDA COM SUCESSO ")
