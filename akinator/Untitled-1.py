from tkinter import *
import tkinter.font as font 

printar='ola'
print(printar)
janela = Tk()
janela.title('jogo da velha')
texto_orientacao = Label(janela, text='clique aqui para comecar o jogo')
texto_orientacao.grid(column=0,row=1)
botao = Button(janela,text='aa',command=printar)
botao.grid(column=0, row=2)


janela.mainloop() 