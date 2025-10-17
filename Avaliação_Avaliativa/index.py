# Welcome personalizado (RNF001)
def show_welcome():
    banner = [
        "******************************************",
        "*                                        *",
        "*              C O T A F R E T E         *",
        "*                                        *",
        "******************************************"
    ]
    for line in banner:
        print(line)
    print("Bem vindo ao sistema de cotação de frete!")
    input("Pressione Enter para continuar...")

# Tela de Login (RNF002) - exige usuário/senha alfanuméricos
def login():
    valid_user = "admin"
    valid_password = "1234"
    
    while True:
        username = input("Digite o usuário (letras e números): ").strip()
        password = input("Digite a senha (letras e números): ").strip()
        
        if not (username.isalnum() and password.isalnum()):
            print("Erro: usuário e senha devem conter apenas letras e números. Tente novamente.")
            continue
        
        if username == valid_user and password == valid_password:
            print("Login realizado com sucesso!")
            main_menu()
            break
        else:
            print("Erro: Usuário ou senha incorretos. Tente novamente.")

# Calculadora (RNF005)
def calculadora():
    print("\n--- Calculadora ---")
    print("1. Somatória")
    print("2. Divisão")
    print("3. Subtração")
    print("4. Adição")
    print("5. Porcentagem")
    print("6. Voltar ao Menu Principal")
    
    while True:
        operacao = input("Escolha uma operação: ").strip()
        if operacao == "1":
            nums = input("Digite os números separados por espaço: ").split()
            try:
                resultado = sum(map(float, nums))
                print(f"Resultado da Somatória: {resultado}")
            except ValueError:
                print("Entrada inválida.")
        elif operacao == "2":
            try:
                a = float(input("Primeiro número: "))
                b = float(input("Segundo número: "))
                resultado = a / b
                print(f"Resultado da Divisão: {resultado}")
            except ValueError:
                print("Entrada inválida.")
            except ZeroDivisionError:
                print("Erro: divisão por zero.")
        elif operacao == "3":
            try:
                a = float(input("Primeiro número: "))
                b = float(input("Segundo número: "))
                print(f"Resultado da Subtração: {a - b}")
            except ValueError:
                print("Entrada inválida.")
        elif operacao == "4":
            try:
                a = float(input("Primeiro número: "))
                b = float(input("Segundo número: "))
                print(f"Resultado da Adição: {a + b}")
            except ValueError:
                print("Entrada inválida.")
        elif operacao == "5":
            try:
                valor = float(input("Valor: "))
                perc = float(input("Porcentagem (%): "))
                print(f"Resultado da Porcentagem: {(valor * perc) / 100}")
            except ValueError:
                print("Entrada inválida.")
        elif operacao == "6":
            break
        else:
            print("Opção inválida.")

# Menu Cotação de Frete (RNF004) - aceita seleção por número ou nome, inclui Total de Itens
def menu_cotacao_frete():
    print("\n--- Menu Cotação de Frete ---")
    aeroportos = [
        ("Congonhas-SP", 102),
        ("Guarulhos-SP", 112),
        ("Campo de Marte-SP", 98),
        ("Pinto Martins-CE", 2922),
        ("Eduardo Gomes-AM", 6294)
    ]
    for i, (nome, dist) in enumerate(aeroportos, start=1):
        print(f"{i}. {nome} - {dist} KM")
    
    sel = input("Escolha o Aeroporto de Destino (número ou nome): ").strip()
    destino = None
    distancia = None
    # tenta por número
    if sel.isdigit():
        idx = int(sel) - 1
        if 0 <= idx < len(aeroportos):
            destino, distancia = aeroportos[idx]
    else:
        for nome, dist in aeroportos:
            if sel.lower() == nome.lower():
                destino, distancia = nome, dist
                break
    if destino is None:
        print("Erro: Aeroporto de destino inválido.")
        return
    
    embalagem = input("Tipo de embalagem (Caixa Papelão / Container): ").strip().lower()
    if embalagem not in ["caixa papelão", "caixa papelao", "container"]:
        print("Erro: Tipo de embalagem inválido.")
        return
    
    try:
        # para caixa papelão -> metros; para container -> centímetros (converteremos)
        altura = float(input("Altura: "))
        largura = float(input("Largura: "))
        profundidade = float(input("Profundidade: "))
        peso = float(input("Peso (Kg): "))
        total_itens = int(input("Total de Itens: "))
    except ValueError:
        print("Erro: entrada numérica inválida.")
        return
    
    if embalagem in ["container"]:
        # recebido em cm conforme RNF; converter para metros para fórmula manter coerência
        altura_m = altura / 100.0
        largura_m = largura / 100.0
        profundidade_m = profundidade / 100.0
        fator = 0.37
    else:
        altura_m = altura
        largura_m = largura
        profundidade_m = profundidade
        fator = 0.26
    
    # Fórmula conforme especificada; aplica por item e multiplica pelo total de itens
    custo_por_item = ((largura_m * altura_m * profundidade_m * peso) * (1 + fator)) * (1 + (distancia * 9.8))
    custo_total = custo_por_item * max(1, total_itens)
    
    print(f"\nDestino: {destino} ({distancia} KM)")
    print(f"Embalagem: {'Container' if embalagem.startswith('container') else 'Caixa Papelão'}")
    print(f"Custo por item: R$ {custo_por_item:.2f}")
    print(f"Total de itens: {total_itens}")
    print(f"Custo total: R$ {custo_total:.2f}")

# Menu Principal (RNF003)
def main_menu():
    print("\n--- Menu Principal ---")
    print("1. Opção 1")
    print("2. Opção 2")
    print("3. Calculadora")
    print("4. Menu Cotação de Frete")
    print("5. Sair")
    
    while True:
        choice = input("Escolha uma opção: ").strip()
        if choice == "1":
            print("Você escolheu a Opção 1.")
        elif choice == "2":
            print("Você escolheu a Opção 2.")
        elif choice == "3":
            calculadora()
        elif choice == "4":
            menu_cotacao_frete()
        elif choice == "5":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chamada inicial
if __name__ == "__main__":
    show_welcome()
    login()
