# Calculadora com loop while

while True:
    print("\n=== Calculadora Básica ===")

    # Entrada de dados
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    # Menu de operações
    print("\nEscolha a operação:")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("0 - Sair")

    opcao = input("Digite o número da operação: ")

    # Condição de parada
    if opcao == "0":
        print("Encerrando a calculadora. Até mais!")
        break # quebra o ciclo 

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
        print("\nOpção inválida! Tente novamente.")
