

def Calcular_imc():
    print("--------------Calculadora de IMC--------------\n")

    # Entrada de dados
    nome = input("Diga seu nome: ")
    # idade = input("Diga sua idade: ")  # Pode ser usado se quiser
    try:
        peso = float(input("Digite seu peso (em kg): "))
        altura = float(input("Digite sua altura (ex: 1.70): "))
    except ValueError:
        print("Você digitou um valor inválido. Tente novamente.\n")
        return  # Sai da função sem continuar

    # Cálculo do IMC
    imc = peso / (altura ** 2)

    # Saída do resultado
    print(f"\nResultados do(a) {nome}")
    print(f"Seu IMC é: {imc:.2f}")

    # Classificação do IMC conforme tabela da UNIMED
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


# Loop principal
while True:
    Calcular_imc()

    continuar = input("\nDeseja realizar outro cálculo de IMC? (s/n): ")
    if continuar != 's':
        print("Encerrando o programa. Obrigado!")
        break

