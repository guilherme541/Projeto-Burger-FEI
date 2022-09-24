import datetime 
from package.valor import calcular

def extrato(c,s):
    with open("./%s.txt" %(c),'r', encoding='utf-8') as dados:
        verificador = dados.read().split(";")
        if verificador[1] == c and verificador[2] == s:
            nome = verificador[0]
            with open("./np%s.txt" %(c),'r', encoding='utf-8') as arquivo:
                hora = datetime.datetime.now()
                db = arquivo.readlines()
                print('''
Nome: {0}
CPF: {1}
Total:R$: {2}                
Data: {3}
Itens do Produto:                '''.format(nome,c , calcular(c,s)  ,hora))
                #Repetição para printar os itens do produto do menu.
                for linha in db:
                    pedidos = linha.replace("\n", "").split(";")  
                    a = int(pedidos[0]) * float(pedidos[3])
                    print(pedidos[0],'  -   ', pedidos[2], '-',' Preço unitário ',pedidos[3],'Valor: ',a , pedidos[4])
            
            
            arquivo.close()

        else:
            print("======================")
            print("|[x] Senha Incorreta !")
            print("======================")
    dados.close() 