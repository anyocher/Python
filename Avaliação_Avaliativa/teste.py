# Projeto COTAFRETE - Sistema de Cotação de Frete e Calculadora
# Desenvolvido em Python

import os

# Função para limpar a tela (compatível com Windows e Unix)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Tabela de Aeroportos e Distâncias (Origem: Guarulhos-SP)
tabela_aeroportos = {
    "Viracopos": 102,
    "Congonhas-SP": 98,
    "Campo de Marte-SP": 112,
    "Pinto Martins-CE": 2922,
    "Eduardo Gomes-AM": 6294
}

# Credenciais de login (hardcoded para simplicidade)
usuario_correto = "admin"
senha_correta = "123"

# Tela Inicial [RNF001]
def tela_inicial():
    limpar_tela()
    print("=" * 50)
    print("         BEM-VINDO AO COTAFRETE")
    print("    Sistema de Cotação de Frete e Calculadora")
    print("=" * 50)
    input("Pressione Enter para continuar...")

# Tela de Login [RNF002]
def tela_login():
    limpar_tela()
    print("TELA DE LOGIN")
    print("-" * 20)
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    
    if usuario == usuario_correto and senha == senha_correta:
        print("Login bem-sucedido!")
        input("Pressione Enter para continuar...")
        return True
    else:
        print("Erro: Usuário ou senha incorretos.")
        input("Pressione Enter para tentar novamente...")
        return False

# Menu Principal [RNF003]
def menu_principal():
    while True:
        limpar_tela()
        print("MENU PRINCIPAL")
        
        print("-" * 20)
        print("1. Cotação de Frete")
        print("2. Calculadora")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            menu_cotacao_frete()
        elif opcao == "2":
            menu_calculadora()
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")

# Menu Cotação de Frete
def menu_cotacao_frete():
    limpar_tela()
    print("COTAÇÃO DE FRETE")
    print("-" * 20)
    
    # Solicitar Aeroporto de Destino
    print("Aeroportos disponíveis (Origem: Guarulhos-SP):")
    for aeroporto, distancia in tabela_aeroportos.items():
        print(f"- {aeroporto}: {distancia} KM")
    
    aeroporto_destino = input("Digite o Aeroporto de Destino: ").strip()
    if aeroporto_destino not in tabela_aeroportos:
        print("Aeroporto inválido.")
        input("Pressione Enter para voltar...")
        return
    
    distancia = tabela_aeroportos[aeroporto_destino]
    
    # Solicitar Embalagem
    embalagem = input("Digite a Embalagem (Caixa Papelão ou Container): ").strip().lower()
    if embalagem not in ["caixa papelão", "container"]:
        print("Embalagem inválida.")
        input("Pressione Enter para voltar...")
        return
    
   
    try:
        altura = float(input("Digite a Altura: "))
        largura = float(input("Digite a Largura: "))
        profundidade = float(input("Digite a Profundidade: "))
        peso = float(input("Digite o Peso (em Kg): "))
        total_itens = int(input("Digite o Total de Itens: "))
    except ValueError:
        print("Valores inválidos. Use números.")
        input("Pressione Enter para voltar...")
        return
    
    # Cálculo do custo
    if embalagem == "caixa papelão":
        # Y = Altura (Mt), X = Largura (Mt), Z = Profundidade (Mt), W = Peso (Kg), F = 0.26
        y, x, z, w, f = altura, largura, profundidade, peso, 0.26
        volume = y * x * z * w
        custo = (volume * (1 + f)) * (1 + (distancia * 9.8))
    elif embalagem == "container":
        # Y = Altura (cm), X = Largura (cm), Z = Profundidade (cm), W = Peso (Kg), F = 0.37
        y, x, z, w, f = altura, largura, profundidade, peso, 0.37
        volume = y * x * z * w
        custo = (volume * (1 + f)) * (1 + (distancia * 9.8))
    
    custo_total = custo * total_itens
    
    print(f"\nCusto estimado do frete: R$ {custo_total:.2f}")
    input("Pressione Enter para voltar ao menu...")

# Menu Calculadora
def menu_calculadora():
    limpar_tela()
    print("CALCULADORA")
    print("-" * 20)
    print("Operações disponíveis:")
    print("1. Soma (Adição)")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Porcentagem")
    print("6. Voltar")
    
    while True:
        opcao = input("Escolha uma operação: ")
        
        if opcao in ["1", "2", "3", "4", "5"]:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                if opcao == "1":
                    resultado = num1 + num2
                    print(f"Resultado: {num1} + {num2} = {resultado}")
                elif opcao == "2":
                    resultado = num1 - num2
                    print(f"Resultado: {num1} - {num2} = {resultado}")
                elif opcao == "3":
                    resultado = num1 * num2
                    print(f"Resultado: {num1} * {num2} = {resultado}")
                elif opcao == "4":
                    if num2 != 0:
                        resultado = num1 / num2
                        print(f"Resultado: {num1} / {num2} = {resultado}")
                    else:
                        print("Erro: Divisão por zero.")
                elif opcao == "5":
                    resultado = (num1 * num2) / 100
                    print(f"Resultado: {num1}% de {num2} = {resultado}")
                
                input("Pressione Enter para continuar...")
            except ValueError:
                print("Valores inválidos. Use números.")
                input("Pressione Enter para continuar...")
        elif opcao == "6":
            break
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")


def main():
    tela_inicial()
    while not tela_login():
        pass  # Loop até login bem-sucedido
    menu_principal()


if __name__ == "__main__":
    main()
