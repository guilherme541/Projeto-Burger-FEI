
from package.menu import novo_menu

def insere_pedido(c,s):
        with open("./%s.txt" %(c),'r', encoding='utf-8') as dados:
            verificador = dados.read().split(";")
            if verificador[1] == c and verificador[2] == s:
                novo_menu(c)
            else:
                print("======================")
                print("|[x] Senha Incorreta !")
                print("======================")
        dados.close()