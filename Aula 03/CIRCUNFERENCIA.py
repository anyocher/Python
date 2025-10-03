# CALCULO DE CIRCUNFERINCIA APLICADO DENTRO DE UM LAÇO WHILE 
import math  # biblioteca para usar o valor de pi

while True:
    print("-----Cálculo do Raio da Circunferência-----\n")

    try:
        circunferencia = float(input("Digite o valor da circunferência (C): "))
        raio = circunferencia / (2 * math.pi) #uso da biblioteca 
        print(f"O raio da circunferência é: {raio:.2f}")

    except ValueError:
        print("Entrada inválida....")
    
    continuar = input("\nDeseja calcular novamente? (s/n): ")
    if continuar != 's':
        print("Encerrando o programa.")
        break
    

