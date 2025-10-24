import mod_inputs

def msg_login():
    print("+" * 25)
    print("          Login")
    print("+" * 25)
    print("\n")

def recebe_usuario():
    usuario = mod_inputs.inp_str("Digite seu usuario: ")
    return usuario 

def recebe_senha():
    senha = mod_inputs.inp_str("Digite sua senha: ")
    return senha 

def valida_usuario(usuario, senha):
    cad_usuario = "admin"
    cad_senha = "1234"

    if cad_usuario == usuario and cad_senha == senha:
        acesso = False 
    else:
        print("Usuario ou senha incorretos... Realize novamente!!!")
        acesso = True
    return acesso 

def main():
    msg_login()
    autentica = True
    while autentica:
        usuario = recebe_usuario()
        senha = recebe_senha()
        autentica = valida_usuario(usuario, senha)
        return True

if __name__ == "__main__":
    main()