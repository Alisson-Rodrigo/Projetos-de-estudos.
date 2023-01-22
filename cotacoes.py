import requests
from bs4 import BeautifulSoup
import datetime
from tkinter import *
from PIL import Image, ImageTk


def dollar():
    url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
    response = requests.get(url)
    data = response.json()
    texto = (f'''
    Code: {data['USDBRL']['code']}
    Máxima: {data['USDBRL']['high']}
    Minima: {data['USDBRL']['low']}
    Variação: {data['USDBRL']['varBid']}
    Valor: {data['USDBRL']['ask']}''')
    texto_livre['text'] = texto

def euro():
    url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
    response = requests.get(url)
    data = response.json()
    texto = (f'''
    Code: {data['EURBRL']['code']}
    Máxima: {data['EURBRL']['high']}
    Minima: {data['EURBRL']['low']}
    Variação: {data['EURBRL']['varBid']}
    Valor: {data['EURBRL']['ask']}''')

    texto_livre['text'] = texto


def bitcoin():
    url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
    response = requests.get(url)
    data = response.json()
    texto = (f'''
    Code: {data['BTCBRL']['code']}
    Máxima: {data['BTCBRL']['high']}
    Minima: {data['BTCBRL']['low']}
    Variação: {data['BTCBRL']['varBid']}
    Valor: {data['BTCBRL']['ask']}''')
    texto_livre['text'] = texto


agora = datetime.date.today()
janela = Tk()

image = Image.open("C:/Users/xxxal\Documents/python/POO\Meuprojeto.jpg")
photo = ImageTk.PhotoImage(image)

imagem = Label(janela, image=photo)
imagem.grid(row=0, column=0, rowspan=10, columnspan=10, sticky="nsew")

janela.title('Cotações MOEDAS')
janela.geometry('600x400')

texto_introducao = Label(janela, text=f'COTAÇÃO DO DIA\n\nData: {agora}', font=('Arial 10 bold',10))
texto_introducao.config(bg='blue', activebackground='white', highlightthickness=1)
texto_introducao.grid(row=0, column=0)

botao1 = Button(janela, text='1-Dollar', command=dollar,font=('Arial 10 bold',15))
botao1.grid(row=2, column=0, padx=0, pady=2)
botao1.config(bg='blue', activebackground='white', highlightthickness=1)


botao2 = Button(janela, text='2-Euro', command=euro,font=('Arial 10 bold',15))
botao2.grid(row=2, column=1, padx=20, pady=2)
botao2.config(bg='blue', activebackground='white', highlightthickness=1)


botao3 = Button(janela, text='3-Bitcoin', command=bitcoin,font=('Arial 10 bold',15))
botao3.config(bg='blue', activebackground='white', highlightthickness=1)
botao3.grid(row=2, column=2, padx=0, pady=2)


texto_livre = Label(janela, text='', font=('Arial 10 bold',15))
texto_livre.config(bg='blue', activebackground='white', highlightthickness=1)
texto_livre.grid(row=4, column=0, padx=10, pady=10)

janela.mainloop()
