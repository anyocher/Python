import pandas as pd
import os
def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

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


def total_por_venda():
    print("\nTotal por Venda:\n", df[['Produto', 'Total Venda']])

def total_vendas_por_item():
    df_item = df.groupby('Item')['Total Venda'].sum()
    print("\nTotal de Vendas por Item:\n", df_item)

def produto_mais_vendido():
    produto = df.groupby('Produto')['Quantidade'].sum().idxmax()
    print("\nProduto mais Vendido:", produto)

def produto_mais_caro():
    produto = df.loc[df['Preço Uni'].idxmax(), 'Produto']
    print("\nProduto mais Caro:", produto)

def total_geral_vendas():
    total = df['Total Venda'].sum()
    print("\nTotal Geral de Vendas:", total)

def vendas_menor_100():
    vendas = df[df['Total Venda'] < 100]
    print("\nVendas com valor menor que 100:\n", vendas[['Produto', 'Total Venda']])

def ordenar_por_quantidade():
    ordenado = df.sort_values(by='Quantidade', ascending=False)
    print("\nVendas Ordenadas pela Maior Quantidade Vendida:\n", ordenado[['Produto', 'Quantidade', 'Total Venda']])

opcoes = {
    'a': ("Total por Venda", total_por_venda),
    'b': ("Total de Vendas por Item", total_vendas_por_item),
    'c': ("Produto mais Vendido", produto_mais_vendido),
    'd': ("Produto mais Caro", produto_mais_caro),
    'e': ("Total Geral de Vendas", total_geral_vendas),
    'f': ("Vendas com valor menor que 100", vendas_menor_100),
    'g': ("Ordenar por Quantidade Vendida", ordenar_por_quantidade),
}

def mostrar_menu():
    print("\n" + "-" * 50)
    print("Escolha uma opção:")
    for key, (descricao, _) in opcoes.items():
        print(f" {key}) {descricao}")
    print(" s) Sair")
    print("-" * 50)

while True:
    mostrar_menu()
    escolha = input("Digite a opção desejada: ").lower().strip()

    if escolha == 's':
        print("\nPrograma Finalizado...")
        break
    elif escolha in opcoes:
        print("-" * 50)
        opcoes[escolha][1]()  
        print("-" * 50)
    else:
        print("\n Opção inválida! Tente novamente.")

