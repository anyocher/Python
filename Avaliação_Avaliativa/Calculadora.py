def calculadora():
    print("\nCalculadora")
    print("1. Soma")
    print("2. Divisão")
    print("3. Subtração")
    print("4. Adição")
    print("5. Porcentagem")
    print("6. Voltar ao Menu Principal")
    
    while True:
        operacao = input("Escolha uma operação: ")
        if operacao == "1":
            numeros = input("Digite os números separados por espaço: ").split()
            resultado = sum(map(float, numeros))
            print(f"Resultado da Soma: {resultado}")
        elif operacao == "2":
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = num1 / num2
                print(f"Resultado da Divisão: {resultado}")
            except ZeroDivisionError:
                print("Erro: Divisão por zero não é permitida.")
        elif operacao == "3":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 - num2
            print(f"Resultado da Subtração: {resultado}")
        elif operacao == "4":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 + num2
            print(f"Resultado da Adição: {resultado}")
        elif operacao == "5":
            valor = float(input("Digite o valor: "))
            porcentagem = float(input("Digite a porcentagem: "))
            resultado = (valor * porcentagem) / 100
            print(f"Resultado da Porcentagem: {resultado}")
        elif operacao == "6":
            print("Voltando ao Menu Principal...")
            break
        else:
            print("Opção inválida. Tente novamente.")