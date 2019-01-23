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
import tkinter as tk
import tkinter as ttk
from tkinter import messagebox

# ---------------------------------------------------------------------------------------------------------------------------DEFINIÇÃO DE LISTAS DEFAULT e VARIAVEIS
lista1 = ['Prodsmart', 'James', 'Talkdesk', 'Codacy', 'Veniam', 'Sensei', 'DefinedCrowd', 'Heptasense', 'Aptoide', 'Probe.ly']
lista2 = [1500000, 3900000, 24500000, 6700000, 26900000, 500000, 1100000, 1000000, 3700000, 435000]
lista3 = ['prodsmart.com', 'james.finance', 'talkdesk.com', 'codacy.com', 'veniam.com', 'sensei.tech', 'definedcrowd.com', 'heptasense.com', 'aptoide.com', 'probe.ly']
MATS = [lista1, lista2, lista3]
TITLE_FONT = ("Verdana", 12)
# ---------------------------------------------------------------------------------------------------------------------------DEFINIÇÃO DE LISTAS DEFAULT e VARIAVEIS

#------------------------------------------------------------------------------------------------------------------------MODEL
def fazLista(lista):
    stringWrite = ""
    for i in range(0, len(lista[0])):  # Para cada linha da matriz
        stringWrite = stringWrite + "" + str(lista[0][i]) + ' - ' + str(round(lista[1][i])) + '€ - ' + str(lista[2][i]) + "\n"  # 1 tab a separar
    return stringWrite


def gravaTexto(lista):
    stringWrite = ""
    for i in range(0, len(lista[0])): # Para cada linha da matriz
        if len(str(lista[0][i]))  >= 12: # se a startup tem mais do que 12 caracteres
            stringWrite = stringWrite + "" + str(lista[0][i]) + '\t' +  '|' + ' ' + str(round(lista[1][i])) + '\t' + '|' + ' ' + str(lista[2][i]) + "\n" # 1 tab a separar
        elif len(str(lista[0][i])) <= 7: # se a startup tem menos que 7
            stringWrite = stringWrite + "" + str(lista[0][i]) + '\t' + '\t' + '\t' + '|' + ' ' + str(round(lista[1][i])) + '\t' + '|' + ' ' + str(lista[2][i]) + "\n" # 2 tab a separar
        else: #else
            stringWrite = stringWrite + "" + str(lista[0][i]) + '\t' + '\t' + '|' + ' ' + str(round(lista[1][i])) + '\t' + '|' + ' ' + str(lista[2][i]) + "\n" # 3 tab
            #para ficar alinhado só
        text = open('MATS.txt', 'w+') # Cria e abre para escrita o ficheiro MATS.txt
        text.write("STARTUPs 2018 – 10 melhores em Lisboa e outras \n") # Escreve o header o ficheiro
        headString = str("Nome" + '\t' + '\t' + '\t' + '|' + '\t' +  'Valor' + '\t' + '|' + '\t' + "Website" + "\n") # Header da lista
        text.write(headString) # Grava header da lista
        text.write(stringWrite) # Grava a matriz MATS para o ficheiro texto
        text.close


def dumpBinary(lista):  # Definição de função para gravar ficheiro binário
    binary = open('MATS', 'wb')
    pickle.dump(lista, binary)  # dump em binário
    binary.close()


def loadBinary():  # Definição de função para leitura de ficheiro binário
    binary = open('MATS', 'rb')
    data = pickle.loads(binary.read())  # dump em binário
    binary.close()
    return data


def graficoBarra(a, b):
    plt.rcdefaults()  # Função para configuração grafica
    fig, ax = plt.subplots(figsize=(8, 8))  # Função para configuração grafica

    y_pos = np.arange(len(a))  # Define lista1 como informação a ser usada no eixo
    ax.barh(y_pos, b)  # Transforma dados da lista2 (Valores) em barras horizontais colocadas a partir do eixo Y
    plt.style.use('ggplot')  # Utiliza o estilo gráfico GGPlot

    ax.set_yticks(y_pos)  # Definição de espacamento entre etiquetas
    ax.set_yticklabels(a)  # Associa labels aos nomes inseridos na lista1(empresas)
    ax.invert_yaxis()  # Tabela é populada de cima para baixo
    ax.set(xlabel='Montante investido', ylabel='Startups')  # Define labels gerais para X e Y
    ax.set_title('STARTUPs 2018 – 10 melhores em Lisboa e outras')  # Define titulo do gráfico

    plt.show()  # Desenha gráfico


def graficoCircular(a, b):  # Definição de função para gráfico circular
    fig, ax = plt.subplots(figsize=(8, 6),
                           subplot_kw=dict(aspect="equal"))  # Define tamanho da imagem do gráfico e aspect ratio

    def func(pct, allvals):  # Transforma valores da lista2 em percentagem
        absolute = int(pct / 100. * np.sum(allvals))
        return "{:.1f}%".format(pct, absolute)

    wedges, texts, autotexts = ax.pie(b, autopct=lambda pct: func(pct, b), textprops=dict(
        color="b"))  # Define valores a serem apresentados nas parcelas do gráfico circular

    ax.legend(wedges, a,  # Configuração de legenda do gráfico circular
              title="StartUps",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold")  # Configuração de texto do gráfico circular

    ax.set_title("STARTUPS 2018 – 10 melhores em Lisboa e outras")  # Definição de titulo do gráfico

    plt.show()  # Traça o gráfico


def novaStartup(lista, a, b, c):  # Introdução de novos dados no array
    b = float(b)
    lista[0].append(a)
    lista[1].append(b)
    lista[2].append(c)
    return lista



def restartPrograma():  # Restart do software no fim de utilização
    print("\nRegressar ao menu principal ou sair?")
    print("1 - Regressar ao menu principal")
    print("0 - Sair do software")
    sair = int(input("Insira a opção desejada: "))
    while sair != 1 and sair != 0:
        print("Opção não reconhecida.")
        sair = int(input("Insira a opcao desejada: "))
    return sair

#------------------------------------------------------------------------------------------------------------------------FIM MODEL

#------------------------------------------------------------------------------------------------------------------------CONTROLLER
try:
    lista = loadBinary()
except FileNotFoundError:
    print("O ficheiro binário não existe! Um ficheiro será criado com a matriz original.")
    dumpBinary(MATS)
    lista = loadBinary()
#------------------------------------------------------------------------------------------------------------------------FIM CONTROLLER

#------------------------------------------------------------------------------------------------------------------------VIEWER
class StartlisApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames =  {}
        self.title("Projeto AP")

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "NSEW")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global lista
        globLista = []
        globLista = lista

        label = tk.Label(self, text = "Projeto de AP", font = TITLE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text = "Startups", command = lambda: controller.show_frame(PageOne))
        button1.pack()
        print(globLista)
        button2 = tk.Button(self, text="Gráfico Horizontal", command= lambda: graficoBarra(globLista[0], globLista[1]))
        button2.pack()

        button3 = tk.Button(self, text="Gráfico Circular", command=lambda: graficoCircular(globLista[0], globLista[1]))
        button3.pack()
        

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global lista
        globLista = []
        globLista = lista

        listaLabel = tk.Label(self, text = fazLista(globLista))
        listaLabel.pack(pady=10, padx=10)

        def updateLista():
            listaLabel['text'] = fazLista(globLista)

        button1 = tk.Button(self, text="Adicionar Startup", command=lambda: controller.show_frame(PageTwo))
        button1.pack()

        button2 = tk.Button(self, text="Gravar em Ficheiro Texto", command=lambda: gravaTexto(globLista))
        button2.pack()

        button3 = tk.Button(self, text="Actualizar Lista", command=lambda: updateLista())
        button3.pack()

        button4 = tk.Button(self, text="Voltar", command=lambda: controller.show_frame(StartPage))
        button4.pack()



class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global lista
        globLista = []
        globLista = lista

        labelNome = tk.Label(self, text = "Insira o nome da startup")
        labelNome.grid(row = 0)
        labelInvest = tk.Label(self, text = "Insira o montante investido")
        labelInvest.grid(row = 1)
        labelWebsite =  tk.Label(self, text = "Insira o website")
        labelWebsite.grid(row = 2)
        
        e1 = tk.Entry(self)
        e1.grid(row = 0, column = 1)
        e2 = tk.Entry(self)
        e2.grid(row = 1, column = 1)
        e3 = tk.Entry(self)
        e3.grid(row = 2, column = 1)

        def callback(globLista):
            a = e1.get()
            b = e2.get()
            c = e3.get()

            if ((len(a) == 0) or (len(b) == 0) or (len(c) == 0)):
                messagebox.showerror("Erro", "Por favor insira os dados da startup!")
            else:
                newLista = novaStartup(globLista, a, b, c)
                dumpBinary(newLista)
                messagebox.showinfo("Informação", "Startup introduzida com sucesso!")

        button1 = tk.Button(self, text="Introduzir", command=lambda: callback(globLista))
        button1.grid(row = 3, column = 0)

        button2 = tk.Button(self, text="Voltar", command=lambda: controller.show_frame(StartPage))
        button2.grid(row = 3, column = 1)

app = StartlisApp()
app.mainloop()

#------------------------------------------------------------------------------------------------------------------------FIM VIEWER