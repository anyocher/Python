start_campo = True
campo = 1
while start_campo:

    match campo:
        case 1:
            try:
                nome = str(inout("Diga a seguir seu nome: "))
                campo =+ 1
            except:
                print("Nome invalido... tente novamente!!")

        case 2:
                try:
                idade = int(input("Diga a seguir sua idade: "))
                campo =+ 1

        case 3:
                try:
                peso = float(input("Diga a seguir seu peso: "))