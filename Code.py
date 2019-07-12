# Programa desenvolvido para aprimoramento de conhecimento na linguagem Python
# Início do desenvolvimento: 12/07/2019
# Final do desenvolvimento: 12/07/2019

# Importando biblioteca de interface gráfica
import tkinter as tk
from tkinter import *

# Função: Botão calcular
def bt_calc() :
    # Verifica se o valor informado é um número ou não
    if(str(en_alt.get()).isnumeric() and str(en_peso.get()).isnumeric()) :
        altura = float(en_alt.get())
        peso   = float(en_peso.get())
        imc    = peso / (altura * altura)
        lb_imc["text"] = imc
    else :
        lb_imc["text"] = "Valores informados inválidos."

# Função: Botão limpar
def bt_limp() :
    en_alt.delete(first=0, last=1000)
    en_peso.delete(first=0, last=1000)
    lb_imc["text"] = " "

# Criando a janela principal
janela = tk.Tk()

# Define um título para a janela
janela.title("IMC")

# Redimensionar a janela
# Largura x Altura + Distância da Esquerda do vídeo + Distância do Topo do vídeo
janela.geometry("300x300+100+100")

# Criando a label altura
lb_alt = Label(janela, text="Altura:")
lb_alt.place(x=35, y=40)

# Criando o entry altura
en_alt = Entry(janela)
en_alt.place(x=85, y=40)

# Criando a label peso
lb_pes = Label(janela, text="Peso:")
lb_pes.place(x=35, y=100)

# Criando o entry peso
en_peso = Entry(janela)
en_peso.place(x=85, y=100)

# Criando a label imc
lb_imc = Label(janela, text="IMC:")
lb_imc.place(x=35, y=160)

# Criando a label resultado imc
lb_imc = Label(janela)
lb_imc.place(x=85, y=160)

# Criando o botão calcular
bt = Button(janela, width = 14, text = "Calcular", command = bt_calc)
bt.place(x=35, y=230)

# Criando o botão limpar
bt = Button(janela, width = 14, text = "Limpar", command = bt_limp)
bt.place(x=150, y=230)

# Comando para execução
janela.mainloop()