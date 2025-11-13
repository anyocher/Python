import matplotlib.pyplot as plt


categorias = ['Mouse', 'Teclado', 'Gabinete', 'Memoria','HD']
valores = [139.9, 39, 156, 250, 219.9]


# plt.plot(categorias, valores, marker='o', linestyle='-', color='pink')
plt.title('Gráfico de barras Vendas')
plt.bar(categorias, valores, color= 'purple')
plt.xlabel('Itens', color= 'purple')
plt.ylabel('Valores', color= 'purple')
# plt.grid(True)
plt.show()
