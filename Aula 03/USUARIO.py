# a) Criar um programa em Python onde o usuário irá digitar seu nome completo, idade e peso e ao final deverá mostrar todos os dados de forma personalizada;
# Entrada de dados
start_programa = True 
start_campos = True
campo = 1

while start_programa:
    while start_campos:

        match campo:
            case 1:
                try:
                    nome = str(input("Digite seu nome completo: "))
                    campo += 1
                except:
                    print("Nome inválido...")
            case 2:  
                try:
                    idade = int(input("Digite sua idade em anos: "))
                    campo += 1
                except:
                    print("Idade inválida...") 
                    
            case 3:
                try:
                    peso = float(input("Digite seu peso em Kg: ").replace (",", "."))
                    start_campos = False
                except:
                    print("Peso inválido...")
    else:
    # Saída personalizada

        print("-----------------------------------------------")
        print("Nome:", nome)

        print("Idade:", idade, "anos")

        print("Peso:", peso, "Kgs")

        fim_programa = True
        while fim_programa:
            print("Deseja finalizar o programa?\n")
            try:
                confirma = str(input("DIGITE S (Sim, finalizar) OU N (Não, finalizar)"))
                if confirma == "S" or confirma == "S":
                 fim_programa = False   
                 start_programa = False
                elif confirma == "N" or confirma == "N":
                    fim_programa = False
                    start_campos = True
                    campos = 1
                else:
                    print("Valor inválido...")
                             
            except:
                print("Campo inválido...")


       # break

else:
    print("\n PROGRAMA CONCLUIDO!!!")
    

