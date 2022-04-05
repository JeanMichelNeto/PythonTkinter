from cgitb import text
from fcntl import F_GET_SEALS
from tkinter import Label, Tk, font
from turtle import width


janela = Tk()
janela.title('Geometria')
janela.geometry('250x250')
# janela.config(bg='#242323')

label_nome = Label(janela, width=10, height=2, text='Nome: ',
                   font=('Arial 10'), fg='#fc3503', bg='black')
#label_nome.place(x=10, y=10)
label_nome.pack()
nome = Label(janela, width=10, height=2, text='Michel ',
             font=('Arial 10'), fg='#fc3503', bg='black')
nome.pack()
#nome.place(x=100, y=10)
#label_nome.grid(row=1, column=0)

label_idade = Label(janela, width=10, height=2, text='Idade: ',
                    font=('Arial 10'), fg='#fc3503', bg='black')
#label_idade.place(x=10, y=60)
label_idade.pack()

idade = Label(janela, width=10, height=2, text='32',
              font=('Arial 10'), fg='#fc3503', bg='black')
idade.pack()

#idade.place(x=100, y=60)
#label_idade.grid(row=2, column=0)

label_pais = Label(janela, width=10, height=2, text='Pais: ',
                   font=('Arial 10'), fg='#fc3503', bg='black')
#label_pais.place(x=10, y=110)
label_pais.pack()

pais = Label(janela, width=10, height=2, text='Brasil',
             font=('Arial 10'), fg='#fc3503', bg='black')
pais.pack()
#pais.place(x=100, y=110)
#label_pais.grid(row=3, column=0)


janela.mainloop()
