# b-) riar um programa em Python que calcule o raio de uma circunferência.

#import math  # para usar o valor de pi
import math as m 

print("-----Cálculo do Raio da Circunferência-----\n")

# Entrada do usuário
circunferencia = float(input("Digite o valor da circunferência (C): "))

# Cálculo do raio
raio = circunferencia / (2 * m.pi)

# Saída formatada
print(f"O raio da circunferência é: {raio:.2f}")
