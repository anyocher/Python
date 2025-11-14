import pandas as pd

df = pd.read_csv("PYTH_07_01_Inventario.csv",  sep= ";")  

reclassificar = df.sort_values(by="PurchasePrice",  ascending=False)

df.to_csv("inventario_totais.csv", index=False)

nome_aquivo = "inventario_totais.csv"
df.to_csv(nome_aquivo , index=False)

df = pd.read_csv("inventario_totais.csv")

# Agrupar por fornecedor
df_fornecedores = df.groupby("Supplier", as_index=True).sum()

df_fornecedores = df_fornecedores.sort_index()

df_fornecedores.to_csv("inventario_fornecedores.csv", encoding="utf-8")
df_fornecedores.to_excel("inventario_fornecedores.xlsx")
