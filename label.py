from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import font
from turtle import width

janela = Tk()
janela.title('Teste Label')
janela.geometry('250x250')
janela.config(bg='#242323')

label_name = Label(janela, width=10, height=2,
                   text='Nome', font=('Arial 15'), fg='#fc3503', bg='white')  # fg define a cor da fonte do botao, bg background
label_name.grid(row=0, column=1)
"""cria a label o atributo janela 
tem que ser declarado, row define linha e colum a coluna"""
label_idade = Label(janela, width=10, height=2,
                    text='Idade', font=('Arial 15'))
label_idade.grid(row=0, column=2)

label_pais = Label(janela, width=10, height=2,
                   text='País', font=('Arial 15 bold'))  # font define tipo de fonte tamanho e estilo
label_pais.grid(row=0, column=3)


janela.mainloop()
