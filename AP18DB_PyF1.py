# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 11:29:09 2018

@author: João Reis, Luís Silvério, Ricardo Cardoso
"""
#-----------------------------------------------------------
    #STARTLIS – StartUps Lisboa 2018
    #Projecto prático de Algoritmia e Programação
    #Docente: Prof. Doutor Paulo Enes da Silveira
    #1º Semestre 2018/2019
    #Curso de Eng. Informática - 1º Ano - Turma - Diurno
#-----------------------------------------------------------


#IMPORT BIBLIOTECAS
import numpy as np #Transformações de valores
import matplotlib.pyplot as plt #Gráficos
import pickle as pickle #Ficheiros Binários
import os.path #Load de MATS binário
import sys #Exit na opção de ler binário

# ---------------------------------------------------------------------------------------------------------------------------DEFINIÇÃO DE LISTAS DEFAULT e VARIAVEIS
lista1 = ['Prodsmart', 'James', 'Talkdesk', 'Codacy', 'Veniam', 'Sensei', 'DefinedCrowd', 'Heptasense', 'Aptoide', 'Probe.ly']
lista2 = [1500000, 3900000, 24500000, 6700000, 26900000, 500000, 1100000, 1000000, 3700000, 435000]
lista3 = ['prodsmart.com', 'james.finance', 'talkdesk.com', 'codacy.com', 'veniam.com', 'sensei.tech', 'definedcrowd.com', 'heptasense.com', 'aptoide.com', 'probe.ly']
MATS = [lista1, lista2, lista3]

# ---------------------------------------------------------------------------------------------------------------------------DEFINIÇÃO DE LISTAS DEFAULT e VARIAVEIS



#------------------------------------------------------------------------------------------------------------------------DEFINIÇÃO DE FUNÇÕES
def fazLista(lista):
    stringWrite = ""
    for i in range(0, len(lista[0])): # Para cada linha da matriz
        if len(str(lista[0][i]))  >= 12: # se a startup tem mais do que 12 caracteres
            stringWrite = stringWrite + "" + str(lista[0][i]) + '\t' +  '|' + ' ' + str(lista[1][i]) + '\t' + '|' + ' ' + str(lista[2][i]) + "\n" # 1 tab a separar
        elif len(str(lista[0][i])) <= 7: # se a startup tem menos que 7
            stringWrite = stringWrite + "" + str(lista[0][i]) + '\t' + '\t' + '\t' + '|' + ' ' + str(lista[1][i]) + '\t' + '|' + ' ' + str(lista[2][i]) + "\n" # 2 tab a separar
        else: #else
            stringWrite = stringWrite + "" + str(lista[0][i]) + '\t' + '\t' + '|' + ' ' + str(lista[1][i]) + '\t' + '|' + ' ' + str(lista[2][i]) + "\n" # 3 tab
            #para ficar alinhado só
    return stringWrite



def dumpBinary():#Definição de função para gravar ficheiro binário
    binary = open('MATS', 'wb')
    pickle.dump(MATS, binary) # dump em binário
    binary.close()

def loadBinary():#Definição de função para leitura de ficheiro binário
    binary = open('MATS', 'rb')
    data = pickle.loads(binary.read()) # dump em binário
    binary.close()
    return data

def graficoBarra(a,b):
    plt.rcdefaults()#Função para configuração grafica
    fig, ax = plt.subplots()#Função para configuração grafica  

    
    y_pos = np.arange(len(lista1)) #Define lista1 como informação a ser usada no eixo 
    ax.barh(y_pos, lista2) #Transforma dados da lista2 (Valores) em barras horizontais colocadas a partir do eixo Y
    plt.style.use('ggplot') #Utiliza o estilo gráfico GGPlot

    ax.set_yticks(y_pos) # Definição de espacamento entre etiquetas
    ax.set_yticklabels(lista1) #Associa labels aos nomes inseridos na lista1(empresas)
    ax.invert_yaxis()  #Tabela é populada de cima para baixo
    ax.set(xlabel='Montante investido', ylabel='Startups') # Define labels gerais para X e Y
    ax.set_title('STARTUPs 2018 – 10 melhores em Lisboa e outras') # Define titulo do gráfico
    
    plt.show() # Desenha gráfico

def graficoCircular(a,b): # Definição de função para gráfico circular
    fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(aspect="equal")) # Define tamanho da imagem do gráfico e aspect ratio
 
    
    def func(pct, allvals): # Transforma valores da lista2 em percentagem
        absolute = int(pct/100.*np.sum(allvals))
        return "{:.1f}%".format(pct, absolute)

    wedges, texts, autotexts = ax.pie(lista2, autopct=lambda pct: func(pct, lista2), textprops=dict(color="b")) # Define valores a serem apresentados nas parcelas do gráfico circular
    
    ax.legend(wedges, lista1, # Configuração de legenda do gráfico circular
              title="StartUps",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))
    
    plt.setp(autotexts, size=8, weight="bold") # Configuração de texto do gráfico circular
    
    ax.set_title("STARTUPS 2018 – 10 melhores em Lisboa e outras") #Definição de titulo do gráfico
    
    plt.show() #Traça o gráfico

def novaStartup(lista1, lista2, lista3): #Introdução de novos dados no array
    x = int(input("\nQual é a quantidade de startups a inserir? "))

    while x > 0:
        a = input("\nInsira o nome da startup: ")
        lista1.append(a)
        b = input("\nInsira o montante investido: ")
        lista2.append(b)
        c = input("\nInsira o site da startup: ")
        lista3.append(c)
        x -= 1
        
    return lista1, lista2, lista3

def restartPrograma():#Restart do software no fim de utilização
    print("\nRegressar ao menu principal ou sair?")
    print("1 - Regressar ao menu principal")
    print("0 - Sair do software")
    sair = int(input("Insira a opção desejada: "))
    while sair != 1 and sair != 0:
        print("Opção não reconhecida.")
        sair = int(input("Insira a opcao desejada: "))
    return sair

#-------------------------------------------------------------------------------------------------------------------FIM DE DEFINIÇÃO DE FUNÇÕES
    



#------------------------------------------------------------------------------------------------------------ROTINA PARA INICIALIZAR AS LISTAS GRAVADAS------------------------------------
if (os.path.exists('MATS')): #esta rotina tem de ser implementada para ele ir buscar os valores gravados no ficheiro binário
    MATS = loadBinary()
    lista1 = MATS[0]
    lista2 = MATS[1]
    lista3 = MATS[2]
#----------------------------------------------------------------------------------------------------------------------------FIM DE ROTINA
    
#SOFTWARE STARTS HERE!
sair=3
    
while sair!=0:
    # ----------------------------------------------------------------------------------------------------------------------------------MENU
    print("\n")
    print(" ######  ########    ###    ########  ######## ##     ## ########   ###### ")
    print("##    ##    ##      ## ##   ##     ##    ##    ##     ## ##     ## ##    ##")
    print("##          ##     ##   ##  ##     ##    ##    ##     ## ##     ## ##      ")
    print(" ######     ##    ##     ## ########     ##    ##     ## ########   ###### ")
    print("      ##    ##    ######### ##   ##      ##    ##     ## ##              ##")
    print("##    ##    ##    ##     ## ##    ##     ##    ##     ## ##        ##    ##")
    print(" ######     ##    ##     ## ##     ##    ##     #######  ##         ###### ")
    print("\n")
    print(" #######    #####      ##    ####### ")
    print("##     ##  ##   ##   ####   ##     ##")
    print("       ## ##     ##    ##   ##     ##")
    print(" #######  ##     ##    ##    ####### ")
    print("##        ##     ##    ##   ##     ##")
    print("##         ##   ##     ##   ##     ##")
    print("#########   #####    ######  ####### ")
    print(" ___________________________________________")
    print("|     Escolha a opcao desejada              |")
    print("|                                           |")
    print("|1 - Apresentar as 10 Melhores Startups     |")
    print("|2 - Criar um grafico de Barras Horizontais |")
    print("|3 - Criar um Grafico Circular              |")
    print("|4 - Gravar em ficheiro de texto            |")
    print("|5 - Gravar em ficheiro binário             |")
    print("|6 - Ler ficheiro texto                     |")
    print("|7 - Ler ficheiro binário                   |")
    print("|0 - Sair                                   |")
    print("|___________________________________________|")
    menu=int(input("Insira a opcao desejada: "))
    
    while menu!=1 and menu!=2 and menu!=3 and menu!=4 and menu!=5 and menu!=6 and menu!=7 and menu!=0: #Verificação de condições do input
        print("Opção não reconhecida.")
        menu=int(input("Insira a opcao desejada: "))
    #------------------------------------------------------------------------------------------------------------------------------------- FIM DE MENU
    
    
    
    
    #-----------------------------------------------------------------------------------------------SAIR
    if menu==0:
        sair=0
    
    #--------------------------------------------------------FIM DE SAIR
 
    
    
    
    #----------------------------------------------------------------------------------------------------------------------------APRESENTAR DADOS
    if menu == 1:
        print("STARTUPs 2018 – 10 melhores em Lisboa e outras")
        print("Nome", '\t', '\t', '  ', '  ', ' |' , ' ', 'Valor', ' ',  '|', '\t', "Website") 
        print(fazLista(MATS))
    #    for i in range(len(MATS[0])):
    #        print(MATS[0][i] , "|" , MATS[1][i] , "|" , MATS[2][i])
        
        
        
        choice = 1
        while choice == 1:
            print("\n \nDeseja adicionar uma startup à lista?")
            print("1 - Sim")
            print("2 - Nao")
            choice = int(input("Insira a opção: "))
        
            if choice == 1:
                lista1, lista2, lista3 = novaStartup(lista1, lista2, lista3)
                for i in range(len(lista1)):
                    print("\n")
                    print(lista1[i] , "|" , lista2[i], "|" , lista3[i])
        
            elif choice == 2:
                dumpBinary()
        
            else:
                print("Opção não reconhecida.")
                
        #---------------RESTART------------------
        sair = restartPrograma()
    #----------------------------------------------------------------------------------------------------------------------------APRESENTAR DADOS
    
    
    
    #----------------------------------------------------------------------------------------------------------------------------GRAFICO HORIZONTAL
    if menu == 2 :
        graficoBarra(lista1,lista2)
    
        choice = 1
        while choice == 1:
            print("\n \nDeseja adicionar uma startup à lista?")
            print("1 - Sim")
            print("2 - Nao")
            choice = int(input("Insira a opção: "))
    
            if choice == 1:
                lista1, lista2, lista3 = novaStartup(lista1, lista2, lista3)
                graficoBarra(lista1, lista2)
    
            elif choice == 2:
                dumpBinary()
    
            else:
                print("Opção não reconhecida.")
                
                
                
        #---------------RESTART------------------
        sair = restartPrograma()
    #------------------------------------------------------------------------------------------------------------------------FIM GRAFICO HORIZONTAL            
    
    
    
    
    #---------------------------------------------------------------------------------------------------------------------------GRAFICO CIRCULAR
    if menu == 3 :
        graficoCircular(lista1,lista2)
    
        choice = 1
        while choice == 1:
            print("\n \nDeseja adicionar uma startup à lista?")
            print("1 - Sim")
            print("2 - Nao")
            choice = int(input("Insira a opção: "))
    
            if choice == 1:
                lista1, lista2, lista3 = novaStartup(lista1, lista2, lista3)
                graficoCircular(lista1, lista2)
    
            elif choice == 2:
                dumpBinary()
    
            else:
                print("Opção não reconhecida.")
                
                
                
        #---------------RESTART------------------
        sair = restartPrograma()
    #---------------------------------------------------------------------------------------------------------------------FIM GRAFICO CIRCULAR
    
    
    #----------------------------------------------------------------------------------------------------------------------------------- GRAVAR FICHEIRO TEXTO
    if menu == 4:
        text = open('MATS.txt', 'r+') # Cria e abre para escrita o ficheiro MATS.txt
        text.write("STARTUPs 2018 – 10 melhores em Lisboa e outras \n") # Escreve o header o ficheiro
        headString = str("Nome" + '\t' + '\t' + '\t' + '|' + '\t' +  'Valor' + '\t' + '|' + '\t' + "Website" + "\n") # Header da lista
        text.write(headString) # Grava header da lista
        text.write(fazLista(MATS)) # Grava a matriz MATS para o ficheiro texto
        text.close
        
        #---------------RESTART------------------
        sair = restartPrograma()
    #-----------------------------------------------------------------------------------------------------------------------------------FIM GRAVAR TEXTO
    
    
    #---------------------------------------------------------------------------------------------------------------GRAVAR FICHEIRO BINARIO
    if menu == 5:
        dumpBinary()
        
        
        #---------------RESTART------------------
        sair = restartPrograma()
    #--------------------------------------------------------------------------------------------------------------------FIM DE GRAVAR FICHEIRO BINARIO
    
    
    
    
    #--------------------------------------------------------------------------------------------------------------------LER FICHEIRO TEXTO
    if menu == 6:
        text = open('MATS.txt', 'r') # Abre o ficheiro de texto
        print(text.read())
        
        
        #---------------RESTART------------------
        sair = restartPrograma()
    #---------------------------------------------------------------------------------------------------------------------LER FICHEIRO TEXTO
    
    
    
    
    
    #--------------------------------------------------------------------------------------------------------------------------LER FICHEIRO BINARIO
    if menu == 7:
        try:
            data = loadBinary()
        #print(data) #deve retornar uma matriz identica ao MATS
    
        except FileNotFoundError:
            print("O ficheiro binário não existe!")
            sys.exit(1)
    
        print("Deseja criar um gráfico de barras ou circular com os dados binários?")
        print("1 -- Gráfico de Barras")
        print("2 -- Gráfico Circular")
        print("3 -- Mostrar apenas os dados")
        choice = int(input("Insira a opção: "))
        while choice!=1 and choice!=2 and choice!=3:
            print("\nOpção não reconhecida. Tente novamente.")
            choice = int(input("Insira a opção: "))
            
        if choice==1:#GRAFICO BARRAS
            graficoBarra(lista1,lista2)
    
        if choice==2:#GRAFICO CIRCULAR
            graficoCircular(lista1,lista2)
            
        if choice==3:#DADOS EM FORMATO LISTA
            print("STARTUPs 2018 – 10 melhores em Lisboa e outras")
            print("Nome", '\t', '\t', '  ', '|' , ' ', 'Valor', ' ',  '|', '\t', "Website")
            print(fazLista(MATS))
            #for i in range(len(MATS[0])):
            #print(MATS[0][i] , "|" , MATS[1][i] , "|" , MATS[2][i])
            
        #---------------RESTART------------------
        sair = restartPrograma()
            
    #--------------------------------------------------------------------------------------------------------------------FIM DE LER FICHEIRO BINARIO    
if sair==0:
    print("\nObrigado por utilizar o software STARTLIS Lisboa 2018. Volte sempre.")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        