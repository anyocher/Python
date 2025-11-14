import pandas as pd

df = pd.read_csv("PYTH_06_04_relatorio_vendas.csv")

reclassificar = df.sort_values(by="Vendedor", ascending=False)
print(reclassificar)

nome_aquivo = "processfiles_reclassificar.csv"
df.to_csv(nome_aquivo , index=False)

# print(df.head()) #teste de leitura do arquivo 

