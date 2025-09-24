# d-)criar um programa que calcule o IMC do usuário baseado no site da UNIMED
print("Calculadora de IMC\n)

# Entrada de dados
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

# Cálculo do IMC = peso/(altura x altura).
imc = peso / (altura ** 2)

# Saída do resultado
print(f"\nSeu IMC é: {imc:.2f}")

# Se for menor de 18,5 será abaixo do peso
if imc < 18.5:
    print("Classificação: Abaixo do peso")
# senão se for menor que 24,9 e maior que 18,4 é peso normal e assim por diante 
elif 18.5 <= imc < 24.9:
    print("Classificação: Peso normal")
elif 25 <= imc < 29.9:
    print("Classificação: Sobrepeso")
elif 30 <= imc < 39.9:
    print("Classificação: Obesidade")
  # se for maior que 39,9 é obesidade grave 
else:
    print("Classificação: Obesidade grave")
