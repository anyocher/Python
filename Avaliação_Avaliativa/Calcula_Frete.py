def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Calcular Custo de Frete")
        print("2. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            calcular_custo_frete()
        elif opcao == "2":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
def calcular_custo_frete():
    print("\n=== Cálculo de Custo de Frete ===")
    print("Origem fixa: Aeroporto de Viracopos")

    # Tabela de aeroportos e distâncias
    aeroportos = {
        1: ("Congonhas-SP", 102),
        2: ("Guarulhos-SP", 112),
        3: ("Campo de Marte-SP", 98),
        4: ("Pinto Martins-CE", 2922),
        5: ("Eduardo Gomes-AM", 6294)
    }

    # Mostrar lista de aeroportos
    print("\nAeroportos disponíveis para destino:")
    for codigo, (nome, km) in aeroportos.items():
        print(f"{codigo}. {nome} ({km} KM)")

    # Escolha do aeroporto de destino
    try:
        escolha = int(input("\nEscolha o número do aeroporto de destino: "))
        if escolha not in aeroportos:
            print("❌ Erro: Opção inválida.")
            return
        destino, distancia = aeroportos[escolha]
    except ValueError:
        print("❌ Erro: Entrada inválida. Digite apenas números.")
        return

    # Escolha do tipo de embalagem
    print("\nTipos de Embalagem:")
    print("1. Caixa Papelão (medidas em METROS)")
    print("2. Container (medidas em CENTÍMETROS)")
    try:
        tipo_embalagem = int(input("Escolha o tipo de embalagem (1 ou 2): "))
        if tipo_embalagem == 1:
            embalagem = "Caixa Papelão"
            fator = 0.26
        elif tipo_embalagem == 2:
            embalagem = "Container"
            fator = 0.37
        else:
            print("❌ Erro: Tipo de embalagem inválido.")
            return
    except ValueError:
        print("❌ Erro: Entrada inválida. Digite 1 ou 2.")
        return

    # Coleta das medidas
    print(f"\nInforme as medidas da embalagem em {'METROS' if tipo_embalagem == 1 else 'CENTÍMETROS'}:")

    try:
        largura = float(input("Largura: "))
        altura = float(input("Altura: "))
        profundidade = float(input("Profundidade: "))
        peso = float(input("Peso (em KG): "))
    except ValueError:
        print("❌ Erro: Digite apenas números válidos.")
        return

    # Conversão para metros se for container
    if tipo_embalagem == 2:
        largura /= 100
        altura /= 100
        profundidade /= 100

    # Aplicação da fórmula:
    # FÓRMULA = ((Y * X * Z * W) * (1 + F)) * (1 + (D * 9.8))
    try:
        custo_frete = ((largura * altura * profundidade * peso) * (1 + fator)) * (1 + (distancia * 9.8))
        print(f"\n✅ Custo do frete para {destino}: R$ {custo_frete:.2f}")
    except Exception as e:
        print(f"❌ Erro no cálculo do frete: {e}")
