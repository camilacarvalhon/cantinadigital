import projeto
import random
total = 0
def menu_cardapio():

    while 1:

        print("** Escolha uma das opções abaixo! **")
        print("[1] - Café da manhã")
        print("[2] - Almoço")
        print("[3] - Janta")
        print("[4] - Finalizar pedido")
        print("[5] - Sair")
        res = int(input("Opção: "))
        
        if res == 1:
           cafe_da_manha()
        elif res == 2:
            almoco()
        elif res == 3:
            janta()
        elif res == 4:
            finalizar_pedido()
            break
        elif res== 5:
            exit()
            break
        else:
            print("ERRO: A opção não se encontra defenida!\n Tente novamente!")
            menu_cardapio()
            
def cafe_da_manha():
      global total
      n = 0
      while (n != 5):
        print("\n*************************")
        print("1)Pão de queijo R$ 1,00")
        print("2)Café R$ 0,50")
        print("3)Misto Quente R$ 2,50")
        print("4)Queijo Quente R$ 2,00")
        pedido_cafe= int(input("Digite seu pedido: "))

        if (pedido_cafe == 1):
            total = total + 1.00

        elif (pedido_cafe == 2):
            total = total + 0.50

        elif (pedido_cafe == 3):
            total = total + 2.50

        elif (pedido_cafe == 4):
            total = total + 2.00

        else:
            print("ERRO: A opção não se encontra defenida!\n Tente novamente!")
        
        return total
def almoco():
      global total
      n = 0
      while (n != 5):
        print("\n*************************")
        print("1)Prato Executivo R$ 13,00")
        print("2)Prato Feito R$ 14,00")
        print("3)Prato do Dia R$ 12,50")
        print("4)Prato da Semana R$ 13,50")
        pedido_almoco= int(input("Digite seu pedido: "))

        if (pedido_almoco == 1):
            total = total + 13.00

        elif (pedido_almoco == 2):
            total = total + 14.00

        elif (pedido_almoco == 3):
            total = total + 12.50

        elif (pedido_almoco == 4):
            total = total + 13.50

        else:
            print("ERRO: A opção não se encontra defenida!\n Tente novamente!")
        
        return total
def janta():
      global total
      while 1:
        print("\n*************************")
        print("1)Prato da Executivo R$ 13,00")
        print("2)Prato Feito R$ 14,00")
        print("3)Prato da Noite R$ 12,50")
        print("4)Prato da Semana R$ 13,50")
        pedido_janta= int(input("Digite seu pedido: "))

        if (pedido_janta == 1):
            total = total + 13.00

        elif (pedido_janta == 2):
            total = total + 14.00

        elif (pedido_janta == 3):
            total = total + 12.50

        elif (pedido_janta == 4):
            total = total + 13.50

        else:
            print("ERRO: A opção não se encontra defenida!\n Tente novamente!")
    
        return total
def exit():
    print("***********************************")
    print("**  Obrigada pela utilização!    **") 
    print("**    Tenha um ótimo dia!        **")  
    print("***********************************")

def finalizar_pedido():
    for i in range(1):
        numero=random.randint(10000,100000)
        print("***************************************")
        print("****        NOTA FISCAL            ****")
        print("***************************************")
        print("****  O numero do seu pedido:      ****")
        print("****  {}                        ****".format(numero))
        print("****  Valor total:                 ****")
        print("****                               ****")
        print("****  R$ {:.2f}                      ****".format(total))
        print("****                               ****")
        print("****  Obrigada pela preferência!   ****")
        print("***************************************")

