#lista dos produtos.
produto = ["X-Salada","X-Burger","Cachorro Quente", "Misto Quente", "Salada de Frutas","Refrigerante","Suco Natural"]
codigo = ["1","2","3","4","5","6","7"]
valortabela = ["R$10,00", "R$10,00", "R$7,50", "R$8,00", "R$5,50","R$4,50","R$6,25"]    #Tabela criada apenas para mostra ao usuario    
valor = ["10.00", "10.00", "7.50", "8.00", "5.50","4.50","6.25"]    #lista criada para adicionar esses valor para poder converter futuramente em  float   
def novo_menu(c): 
    with open("./np%s.txt" %(c),'a', encoding='utf-8') as dados:
            print('''
==============================================
|Código          Produto               Preço |
==============================================
            ''')
            for i in range(0, len(codigo)):
                print("{0:<15} {1:<20} {2:<15}".format(codigo[i],produto[i],valortabela[i]))
                print()
            while True:
                p = int(input("Digite o Codigo do Produto que deseja efetuar o pedido:  "))

                if p == 1: 
                    with open("./np%s.txt" %(c),'a', encoding='utf-8') as dados:    
                        quantidade = int(input("Digite a Quantidade de %s que deseja:  " % produto[0]))
                        dados.write('{0};{1};{2};{3};\n'.format(quantidade,codigo[0], produto[0],valor[0]))
                        dados.close()
                        confirmação = (input("Gostaria de adicionar mais produtos? (S/N)"))
                        if confirmação == "S" or confirmação == "s":
                            print()
                        else:
                            break
                
                elif p == 2 :
                    with open("./np%s.txt" %(c),'a', encoding='utf-8') as dados:    
                        quantidade = int(input("Digite a Quantidade de %s que deseja:  " % produto[1]))
                        dados.write('{0};{1};{2};{3};\n'.format(quantidade,codigo[1], produto[1],valor[1]))
                        dados.close()                    
                        confirmação = (input("Gostaria de adicionar mais produtos? (S/N):   "))
                        if confirmação == "S" or confirmação == "s":
                            print()
                        else:
                            break
                elif p == 3 :
                    with open("./np%s.txt" %(c),'a', encoding='utf-8') as dados:    
                        quantidade = int(input("Digite a Quantidade de %s que deseja:  " % produto[2]))
                        dados.write('{0};{1};{2};{3};\n'.format(quantidade,codigo[2], produto[2],valor[2]))
                        dados.close()                   
                        confirmação = (input("Gostaria de adicionar mais produtos? (S/N):   "))
                        if confirmação == "S" or confirmação == "s":
                            print()
                        else:
                            break
                elif p == 4 :
                    with open("./np%s.txt" %(c),'a', encoding='utf-8') as dados:    
                        quantidade = int(input("Digite a Quantidade de %s que deseja:  " % produto[3]))
                        dados.write('{0};{1};{2};{3};\n'.format(quantidade,codigo[3], produto[3],valor[3]))
                        dados.close()                    
                        confirmação = (input("Gostaria de adicionar mais produtos? (S/N):   "))
                        if confirmação == "S" or confirmação == "s":
                            print() 
                        else:
                            break
                elif p == 5 :
                    with open("./np%s.txt" %(c),'a', encoding='utf-8') as dados:    
                        quantidade = int(input("Digite a Quantidade de %s que deseja:  " % produto[4]))
                        dados.write('{0};{1};{2};{3};\n'.format(quantidade,codigo[4], produto[4],valor[4]))
                        dados.close()                    
                        confirmação = (input("Gostaria de adicionar mais produtos? (S/N):   "))
                        if confirmação == "S" or confirmação == "s":
                            print()
                        else:
                            break               
                elif p == 6 :
                    with open("./np%s.txt" %(c),'a', encoding='utf-8') as dados:    
                        quantidade = int(input("Digite a Quantidade de %s que deseja:  " % produto[5]))
                        dados.write('{0};{1};{2};{3};\n'.format(quantidade,codigo[5], produto[5],valor[5]))
                        dados.close()                    
                        confirmação = (input("Gostaria de adicionar mais produtos? (S/N):   "))
                        if confirmação == "S" or confirmação == "s":
                            print()
                        else:
                            break                         
                elif p == 7 :
                    with open("./np%s.txt" %(c),'a', encoding='utf-8') as dados:    
                        quantidade = int(input("Digite a Quantidade de %s que deseja:  " % produto[6]))
                        dados.write('{0};{1};{2};{3};\n'.format(quantidade,codigo[6], produto[6],valor[6]))
                        dados.close()                    
                        confirmação = (input("Gostaria de adicionar mais produtos? (S/N):   "))
                        if confirmação == "S" or confirmação == "s":
                            print()
                        else:
                            break                         
                        
                if p != 1 and p != 2 and p != 3 and p != 4 and p != 5 and p != 6 and p != 7 and p != 8 :
                    print()
                    print("Não Encontramos esse produto em nosso cardapio !")