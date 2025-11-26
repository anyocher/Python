import pandas as pd

# URL do arquivo do professor
url = "https://raw.githubusercontent.com/JansenLeite/Python/main/PYTH_07_01_Inventario.csv"
def carregar_dados(url):
    return pd.read_csv(url, sep=";")

def calcular_totais(df):
    df["PurchasePriceTotal"] = df["PurchasePrice"] * df["StockQuantity"]
    df["SalePriceTotal"] = df["SalePrice"] * df["StockQuantity"]
    return df

def salvar_arquivos(df, prefixo="inventario"):
    df.to_csv(f"{prefixo}.csv", index=False)
    df.to_excel(f"{prefixo}.xlsx", index=False)

def gerar_relatorio_fornecedores(df):
    df_fornecedor = df.groupby("Supplier").sum(numeric_only=True).reset_index()
    df_fornecedor = df_fornecedor.sort_values("Supplier")
    return df_fornecedor

def filtrar_acima60(df):
    return df[df["StockQuantity"] > 60]

def main(url):
    df = carregar_dados(url)

    df = calcular_totais(df)
    salvar_arquivos(df, prefixo="inventario_totais")

    df_fornecedor = gerar_relatorio_fornecedores(df)
    salvar_arquivos(df_fornecedor, prefixo="inventario_fornecedores")

    df_acima60 = filtrar_acima60(df)
    salvar_arquivos(df_acima60, prefixo="inventario_acima60")

    print("Arquivos gerados...")

main(url) # rodar o programa com url fornecida