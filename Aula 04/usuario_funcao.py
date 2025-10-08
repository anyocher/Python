# a) Criar um programa em Python onde o usuário irá digitar seu nome completo, idade e peso. Usando 3 funções, sendo elas de inclusão de dados, mostrar dados e por fim a saida de dados
def incluir_dados():
    nome = input("Digite seu nome completo: ")
    idade = int(input("Digite sua idade: "))
    peso = float(input("Digite seu peso (em kg): "))

    dados_usuario = {
    "nome": nome,
    "idade": idade,
    "peso": peso
    }
    return dados_usuario

def exibir_dados(dados):
    print(f"Nome: {dados['nome']}")
    print(f"Idade: {dados['idade']} anos")
    print(f"Peso: {dados['peso']} kg")

def exibir_saida(dados):
    exibir_dados(dados) 

if __name__ == "__main__":
    dados_digitados = incluir_dados()
    exibir_saida(dados_digitados)
    