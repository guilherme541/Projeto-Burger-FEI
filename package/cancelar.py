import os

produto = ["X-Salada","X-Burger","Cachorro Quente", "Misto Quente", "Salada de Frutas","Refrigerante","Suco Natural"]
codigo = ["1","2","3","4","5","6","7"]
# Função Para o usuario e o extrato do pedido do cliente.
def cancela_pedido(c,s):
    with open("./%s.txt" %(c),'r', encoding='utf-8') as dados:
        verificador = dados.read().split(";")
        if verificador[1] == c and verificador[2] == s:
            nome = verificador[0]
            dados.close()
            os.remove("./%s.txt" % c)
            os.remove("./np%s.txt" % c)
            print("=================================")
            print("Sr. %s pedido cancelado |" % nome)
            print("==================================")
        else:
            print("======================")
            print("|[x] Senha Incorreta !")
            print("======================")

# Função Para cancelar o produto que o cliente escolheu.
#Função Não Esta funcionano corretamente.
def cancela_pedido2(c,s):
    with open("./%s.txt" %(c),'r', encoding='utf-8') as dados:
        verificador = dados.read().split(";")
        if verificador[1] == c and verificador[2] == s:
            nome = verificador[0]
            arquivo = open('./np%s.txt' % c, 'r', encoding='utf-8')
            codigo = int(input("Digite o codigo do produto que gostaria de cancelar: "))
            quantidade = int(input("Digite a quantidade do produto que gostaria de cancelar: "))
            db = arquivo.readlines()  
            listap = []
            arquivo.close()
            status = 'Cancelado'
            for linha in db:
                pedidos = linha.replace("\n", "").split(";")
                listap.append(pedidos)  
                if codigo == int(pedidos[1]): 
                    if quantidade == int(pedidos[0]) and 'Cancelado' not in pedidos[4]:
                            print('Pedido Cancelado')
                            a = pedidos
                            del(pedidos)
                            a[4] = status       
        
            else:
                print("Pedido Inexiste")
        arquivo.close()


