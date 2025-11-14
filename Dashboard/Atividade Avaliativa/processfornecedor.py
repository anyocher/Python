import pandas as pd

df = pd.read_csv("PYTH_07_01_Inventario.csv",  sep= ";")  


# Agrupar por fornecedor
df_fornecedores = df.groupby("Forecedor", as_index=True).sum()

df_fornecedores = df_fornecedores.sort_index()

df_fornecedores.to_csv("inventario_fornecedores.csv")