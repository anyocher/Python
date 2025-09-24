#c) Crie uma calculadora com as 4 operações matemáticas (Multiplicação, Soma,
Subtração e Divisão);
print("=== Calculadora Básica ===")

# Entrada de dados
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("\nEscolha a operação:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

opcao = input("Digite o número da operação: ")

# Processamento
if opcao == "1":
    resultado = n1 + n2
    print(f"\nResultado: {n1} + {n2} = {resultado}")
elif opcao == "2":
    resultado = n1 - n2
    print(f"\nResultado: {n1} - {n2} = {resultado}")
elif opcao == "3":
    resultado = n1 * n2
    print(f"\nResultado: {n1} * {n2} = {resultado}")
elif opcao == "4":
    if n2 != 0:
        resultado = n1 / n2
        print(f"\nResultado: {n1} / {n2} = {resultado}")
    else:
        print("\nErro: Divisão por zero não é permitida!")
else:
    print("\nOpção inválida!")
