
def calcular(c,s):
    with open("./%s.txt" %(c),'r', encoding='utf-8') as dados:
        verificador = dados.read().split(";")
        if verificador[1] == c and verificador[2] == s:
            nome = verificador[0]
            with open("./np%s.txt" %(c),'r', encoding='utf-8') as arquivo:
                db = arquivo.readlines()
                listap = []
                valor = 0
                for pedido in db:
                    listap.append(pedido.replace('\n','').split(';'))
                for pedido in listap:
                    if "Cancelado" not in pedido:
                        valor += float(pedido[3]) * int(pedido[0])
                return valor
        else:
            print("======================")
            print("|[x] Senha Incorreta !")
            print("======================")
    dados.close()

