import requests
from tkinter import *
import tkinter.font as font 
import random
from IPython.display import clear_output
import time


def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    print(texto)




janela = Tk()
janela.title('jogo da velha')
texto_orientacao = Label(janela, text='clique aqui para comecar o jogo')
texto_orientacao.grid(column=0,row=1)
botao = Button(janela,text='aa',command=pegar_cotacoes)

janela.mainloop() 