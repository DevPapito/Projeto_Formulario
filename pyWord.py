from pynput.keyboard import Key, Controller
from tkinter import *
from time import sleep

class programa:
    def __init__(self):
        self.root = Tk()
        self.button = None

        self.config()
        self.buttonFun()

        self.root.mainloop()

    def config(self):
        self.root.geometry('500x200')
    
    def buttonFun(self):
        button = Button(self.root,text='enviar comando',command=self.executerWither)
        button.place(relx=0.05,rely=0.05,height=100,width=500)
        self.button = button
    
    def executerWither(self):
        sleep(10)
        var = """
                A Organização das Nações Unidas (ONU) surgiu como resultado das devastadoras consequências da Segunda Guerra Mundial. Após o término do conflito, em 1945, líderes de todo o mundo se uniram em uma série de conferências internacionais, incluindo a Conferência de São Francisco, para estabelecer uma instituição que promovesse a paz e a cooperação entre as nações. Assim, em 24 de outubro de 1945, a ONU foi oficialmente fundada, marcando o início de uma nova era na história das relações internacionais. Com a assinatura da Carta das Nações Unidas por 51 países fundadores, a ONU se tornou a principal organização para a manutenção da paz e segurança global, representando uma tentativa coletiva da comunidade internacional de estabelecer uma ordem mundial baseada na diplomacia e no respeito mútuo entre as nações.
            """

        keyB.type(var)


keyB = Controller()

programa()



