def incluir_dados():
    while True:
        try:
            nome = input("Digite seu nome completo: ")
            idade = int(input("Digite sua idade: "))
            peso = float(input("Digite seu peso (em kg): "))

            if idade <= 0 or peso <= 0:
                raise ValueError("Idade e peso devem ser números positivos.")
            
            dados_usuario = {
                "nome": nome,
                "idade": idade,
                "peso": peso
            }
            return dados_usuario
        except ValueError as e:
            print(f"Erro de entrada: {e}. Tente novamente.")

def exibir_dados(dados):
    print(f"Nome: {dados['nome']}")
    print(f"Idade: {dados['idade']} anos")
    print(f"Peso: {dados['peso']} kg")

def exibir_saida(dados):
    exibir_dados(dados)

if __name__ == "__main__":
    continuar = "s"
    while continuar.lower() == "s":
        dados_digitados = incluir_dados()   
        exibir_saida(dados_digitados)
        continuar = input("Deseja continuar? (s/n): ").strip()
    
    print("Obrigado por usar o programa!")
