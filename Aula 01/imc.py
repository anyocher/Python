# d-)criar um programa que calcule o IMC do usuário baseado no site da UNIMED
print("Calculadora de IMC")

# Entrada de dados
nome = input("Diga seu nome:")
idade = input("Diga sua idade: ")
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (ex: 1.50): "))

# Cálculo do IMC = peso/(altura x altura).
imc = peso / altura ** 2

# Saída do resultado
print("Seu Resultado é: ")
print(f"\nSeu IMC é: {imc:.2f}")

#if idade >= 19 and idade < 61: 
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


#
def Calcular_imc():
    
    print("--------------Caclculadora de IMC--------------\n")

# Entrada de dados
nome = input("Diga seu nome:")
#idade = input("Diga sua idade: ")
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (ex: 1.50): "))
imc = peso / altura ** 2

print("Resultados do(a)", nome)
print(f"\nSeu IMC é: {imc:.2f}")
#if idade >= 19 and idade < 61: 
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Classificação: Peso normal")
elif 25 <= imc < 29.9:
    print("Classificação: Sobrepeso")
elif 30 <= imc < 39.9:
    print("Classificação: Obesidade") 
else:
    print("Classificação: Obesidade grave")


    while True :

        Calcular_imc()

        print("Deseja realizar outro calculo de IMC?")



