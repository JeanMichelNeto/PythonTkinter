from tkinter import *

corback = '#242323'

janela = Tk()  # objeto janela ele é manipulado pelas funções
janela.title('Nova Janela')  # titulo janela
janela.geometry('600x250')  # tamanho largura por altura
janela.config(bg=corback)

janela.iconphoto(False, PhotoImage(file='favicon.png'))  # adicionarfavicon
janela.resizable(width=False, height=False)


janela.mainloop()
