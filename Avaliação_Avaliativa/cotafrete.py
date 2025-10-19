def tela_inicial():
print("======================")
print("|                    |")
print("|      Cotafrete     |")
print("|                    |")
print("======================\n")
input("\nPressione ENTER para continuar...")

def tela_login():
    usuario_cadastrado = "admin"
    senha_cadastrada = "1234"

    while True:
        print("\nTela Login")
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario == usuario_cadastrado and senha == senha_cadastrada:
            print("\nLogin realizado com sucesso!")
            return True
        else:
            print("\n❌ Usuário ou senha incorretos. Tente novamente.")

def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Cotação de Frete")
        print("2 - Calculadora")
        print("3 - Voltar para o Login")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_cotacao_frete()
        elif opcao == "2":
            menu_calculadora()
        elif opcao == "3":
            print("\nVoltando para a tela de login...")
            break
        else:
            print("\nOpção inválida, tente novamente.")

def menu_cotacao_frete():
    aeroportos = {
        "1": ("Congonhas-SP", 102),
        "2": ("Guarulhos-SP", 112),
        "3": ("Campo de Marte-SP", 98),
        "4": ("Pinto Martins-CE", 2922),
        "5": ("Eduardo Gomes-AM", 6924)
    }

    print("\n=== COTAÇÃO DE FRETE ===")
    print("Aeroporto de Origem: Viracopos-SP")
    print("Escolha o aeroporto de destino:")

    for codigo, (nome, distancia) in aeroportos.items():
        print(f"{codigo} - {nome} ({distancia} km)")

    escolha = input("Digite o número do aeroporto: ")

    if escolha not in aeroportos:
        print("❌ Opção inválida.")
        return

    destino, distancia = aeroportos[escolha]
    print(f"\nDestino escolhido: {destino} - {distancia} km")

    tipo_embalagem = input("Tipo de embalagem (Caixa ou Container): ").strip().lower()
    altura = float(input("Altura: "))
    largura = float(input("Largura: "))
    profundidade = float(input("Profundidade: "))
    peso = float(input("Peso total (kg): "))

    if tipo_embalagem == "caixa":
        fator = 0.26
    elif tipo_embalagem == "container":
        fator = 0.37
    else:
        print(" Tipo de embalagem inválido.")
        return

    custo = ((largura * altura * profundidade * peso) * (1 + fator)) * (1 + (distancia * 9.8))
    print("\n Custo estimado do frete: R$ {:.2f}".format(custo))

    continuar = input("\nDeseja fazer outra cotação? (s/n): ").lower()
    if continuar == "s":
        menu_cotacao_frete()
    else:
        print("\nVoltando ao menu principal...")

def menu_calculadora():
    while True:
        print("\n=== CALCULADORA ===")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Porcentagem")
        print("6 - Voltar ao Menu Principal")

        opcao = input("Escolha a operação: ")

        if opcao == "6":
            break

        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            resultado = n1 + n2
            print(f"Resultado: {resultado}")
        elif opcao == "2":
            resultado = n1 - n2
            print(f"Resultado: {resultado}")
        elif opcao == "3":
            resultado = n1 * n2
            print(f"Resultado: {resultado}")
        elif opcao == "4":
            if n2 == 0:
                print(" Erro: divisão por zero!")
            else:
                resultado = n1 / n2
                print(f"Resultado: {resultado}")
        elif opcao == "5":
            resultado = (n1 * n2) / 100
            print(f"{n2}% de {n1} = {resultado}")
        else:
            print(" Opção inválida.")

        continuar = input("\nDeseja fazer outro cálculo? (s/n): ").lower()
        if continuar != "s":
            break

def main():
    tela_inicial()
    if tela_login():
        menu_principal()
