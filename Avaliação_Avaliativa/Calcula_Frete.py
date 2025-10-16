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