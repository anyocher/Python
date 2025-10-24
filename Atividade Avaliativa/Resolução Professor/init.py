import login
import menu_principal
print("+" * 25)
print("        COTAFRETE")
print("+" * 25)
print("\n")

acesso = login.main()
if acesso:
    menu_principal.main()

print("\n🌷Obrigado por usar o sistema!! Até a proxima :) 🌷 \n")
