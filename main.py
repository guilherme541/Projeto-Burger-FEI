#Importação dos modulos que estão na pasta package
from package.menu import novo_menu
from package.cancelar import cancela_pedido , cancela_pedido2
from package.autenticador import autenticação
from package.inserir import insere_pedido
from package.valor import calcular
from package.extrato import extrato



def novo_pedido():  # Novo pedido Cadastro do Cliente e catalogo.
    n = input('Nome: ')
    c = input('CPF: ')
    s = input('Senha: ')
    try: #Verificando se ja tem um CPF cadastrado.
        dados = open('%s.txt'%(c),'r')
        npedido = open("np%s.txt" %(c),'r')
        for elemento in dados.readlines():
            print('''

================================================
|[x] O CPF: %s já possui um pedido em andamento|
================================================

''' % (c))
        dados.close()
        npedido.close()
    except: #Criação do arquivo para armazenar o Nome, CPF, Senha.
        dados = open("%s.txt" %(c),'a')
        npedido = open("np%s.txt" %(c),'a')
        dados.write('{0};{1};{2};{3}\n'.format(n, c, s, s))
        dados.close()
        npedido.close()
        novo_menu(c) #Chamando o menu com o cpf

if __name__ == '__main__': #Verificando e inciando o Loop.
        while True:  # Menu a onde o Usuario podera escolher as opçoes
            print('''

    ================================================
    |         Seja Bem-Vindo(a) à Burger FEI       |
    ================================================
    | (1) - NOVO PEDIDO                            |
    ------------------------------------------------
    | (2) - CANCELAR PEDIDO                        |
    ------------------------------------------------
    | (3) - INSERE PEDIDO                          |
    ------------------------------------------------
    | (4) - CANCELAR PRODUTO                       |
    ------------------------------------------------
    | (5) - VALOR DO PEDIDO                        |
    ------------------------------------------------
    | (6) - EXTRATO DO PEDIDO                      |
    ================================================
    | (0) - SAIR                                   |
    ================================================


    '''

    )
            entrada = int(input("Digite a opção: "))
            #Criar Usuario
            if entrada == 1:
                novo_pedido()
            #Inserir Pedido
            elif entrada == 2:
                print("Digite o seu Login!")
                c = input("CPF: ")
                s = input("Senha: ")
                aut = autenticação(c)
                if aut == True:
                    cancela_pedido(c,s)
                else:
                    print("============================================================")
                    print("|[x] CPF Incorreto ou não esta cadastrado em nosso sistema !")
                    print("============================================================")
            #Cancelar Pedido        
            elif entrada == 3:
                print("Digite o seu Login!")
                c = input("CPF: ")
                s = input("Senha: ")
                aut = autenticação(c)
                if aut == True:
                    insere_pedido(c,s)
                else:
                    print("============================================================")
                    print("|[x] CPF Incorreto ou não esta cadastrado em nosso sistema !")
                    print("============================================================")
            
            #Cancelar Produto 
            #Função Não Esta funcionando corretamente.   
            elif entrada == 4:
                print("Digite o seu Login!")
                c = input("CPF: ")
                s = input("Senha: ")
                aut = autenticação(c)
                if aut == True:
                    cancela_pedido2(c,s)
                else:
                    print("============================================================")
                    print("|[x] CPF Incorreto ou não esta cadastrado em nosso sistema !")
                    print("============================================================")
            #Valor a Pagar
            elif entrada == 5:
                print("Digite o seu Login!")
                c = input("CPF: ")
                s = input("Senha: ")
                aut = autenticação(c)
                if aut == True:
                    valor = calcular(c,s)
                    print("==========================")
                    print("|Valor a pagar : R$ %s |" %(valor))
                    print("==========================")
                else:
                    print("============================================================")
                    print("|[x] CPF Incorreto ou não esta cadastrado em nosso sistema !")
                    print("============================================================")
            elif entrada == 6:
                print("Digite o seu Login!")
                c = input("CPF: ")
                s = input("Senha: ")
                aut = autenticação(c)
                if aut == True:
                    extrato(c,s)
                else:
                    print("============================================================")
                    print("|[x] CPF Incorreto ou não esta cadastrado em nosso sistema !")
                    print("============================================================")
            elif entrada == 0:
                break
            else:
                print("Opção incorreta, tente novamente. ")