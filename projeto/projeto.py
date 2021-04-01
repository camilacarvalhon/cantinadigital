import random
import os
import cardapio
total = 0
def acessar():
    imprimir_mensagem()
    identificar()

def imprimir_mensagem():
    print("********************************************")
    print("****   Bem-vindo ao Cardápio Digital    ****")
    print("********************************************\n")

def identificar():

    ident=input("Você é estudante?\n(Responda com S para sim e N para não!)\n")
    ident=ident.upper()

    if ( ident == "S"): 
        estudante()
    elif (ident == "N"): 
        visitante()
    else:
        print("Opção invalida, digite uma opção válida.")
        ident=input("Você é estudante?\n(Responda com S para sim e N para não!)\n")
        ident=ident.upper()
        while (ident != "S" and ident != "N"):
            print("Resposta inválida, digite uma resposta válida.")
            ident=input("Você é estudante?\n(Responda com S para sim e N para não!)\n")
            ident=ident.upper()
        if ( ident == "S"): 
            estudante()
        else: 
           visitante()

def estudante():
    print("Para fins de reconhecimento do estudante, preencha os campos abaixo!")   
    nome= input("Qual é o seu nome? \n")
    curso= input("Qual é seu curso? \n")
    print("Olá {}! Seja bem-vind@.".format(nome))
    menu_inicial()

def visitante():
    print("Para fins de melhor atendimento, preencha o campo abaixo!")
    nome= input("Qual é o seu nome? ")
    print("Olá {}! Seja bem-vind@.".format(nome))
    menu_inicial()

def menu_inicial(): 
    while 1:
        print("**Escolha uma das opções abaixo**")
        print("[1] - Sobre nós")
        print("[2] - Cardápio")
        print("[3] - Sair")
        res = int(input("Opcao: "))
        print("**********************************")

        if res == 1:
            print("**************************************************************************************")
            print("* Olá pessoal!\n* O projeto foi desenvolvido no intuito de agilizar o funcionamento de um restaurante\n* de uma instituição de ensino que tem muitos clientes.")   
            print("**************************************************************************************")
        elif res == 2:
            print("Menu Cardapio")
            cardapio.menu_cardapio()
            break
        else:
            exit()
            break
def exit():
    print("***********************************")
    print("** Obrigada pela utilização!     **") 
    print("** Tenha um ótimo dia!           **")  
    print("***********************************")


if(__name__ == "__main__"):
    acessar()