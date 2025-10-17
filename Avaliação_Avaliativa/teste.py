# Tela de Login
def login():
    valid_user = "admin"
    valid_password = "1234"
    
    while True:
        username = input("Digite o usuário (letras e números): ")
        password = input("Digite a senha (letras e números): ")
        
        if username == valid_user and password == valid_password:
            print("Login realizado com sucesso!")
            main_menu()
            break
        else:
            print("Erro: Usuário ou senha incorretos. Tente novamente.")
# Função para Calculadora
def calculadora():
    print("\n--- Calculadora ---")
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


# Função para Menu Cotação de Frete
def menu_cotacao_frete():
    print("\n--- Menu Cotação de Frete ---")
    aeroportos = {
        "Congonhas-SP": 102,
        "Guarulhos-SP": 112,
        "Campo de Marte-SP": 98,
        "Pinto Martins-CE": 2922,
        "Eduardo Gomes-AM": 6294
    }
    
    print("Aeroportos disponíveis:")
    for aeroporto in aeroportos:
        print(f"- {aeroporto}")
    
    destino = input("Digite o Aeroporto de Destino: ")
    if destino not in aeroportos:
        print("Erro: Aeroporto de destino inválido.")
        return
    
    embalagem = input("Digite o tipo de embalagem (Caixa Papelão ou Container): ").strip().lower()
    if embalagem not in ["caixa papelão", "container"]:
        print("Erro: Tipo de embalagem inválido.")
        return
    
    try:
        altura = float(input("Digite a Altura (em metros para Caixa Papelão ou em cm para Container): "))
        largura = float(input("Digite a Largura (em metros para Caixa Papelão ou em cm para Container): "))
        profundidade = float(input("Digite a Profundidade (em metros para Caixa Papelão ou em cm para Container): "))
        peso = float(input("Digite o Peso (em Kg): "))
        total_itens = int(input("Digite o Total de Itens: "))
    except ValueError:
        print("Erro: Entrada inválida. Certifique-se de digitar números válidos.")
        return
    
    distancia = aeroportos[destino]
    if embalagem == "caixa papelão":
        fator_custo = 0.26
    elif embalagem == "container":
        fator_custo = 0.37
        altura /= 100
        largura /= 100
        profundidade /= 100
    
    custo_frete = ((altura * largura * profundidade * peso) * (1 + fator_custo)) * (1 + (distancia * 9.8))
    print(f"Custo do Frete: R$ {custo_frete:.2f}")


def main_menu():
    print("\n--- Menu Principal ---")
    print("1. Calculadora")
    print("2. Menu Cotação de Frete")
    print("3. Sair")
    
    while True:
        choice = input("Escolha uma opção: ")
        if choice == "1":
            calculadora()
        elif choice == "2":
            menu_cotacao_frete()
        elif choice == "3":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    print("----------------COTAFRETE----------------")
    print("Bem vindo ao sistema de cotação de frete!")
    login()
