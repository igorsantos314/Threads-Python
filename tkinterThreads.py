import _thread as thread, time
from tkinter import *
from tkinter import messagebox
from random import randint

janela = Tk()
janela.geometry('400x400')

btBlack = Button(text='  ', bg='black')
btRed = Button(text='  ', bg='red')

def mensagem():
    messagebox.showinfo('Olá Igor')

def poscicao(cont):
    for i in range(0,400,10):
        time.sleep(1)
        btBlack.place(x=i,y=i)

def poscicao2(cont):
    for i in range(0,400,10):
        eixoX = randint(10,300)
        eixoY = randint(10,300)

        time.sleep(1)
        btRed.place(x=eixoX,y=eixoY)

btMen = Button(text='Mensagem', command= mensagem) 
btMen.pack()

#for i in range(5):
thread.start_new_thread(poscicao,(1,))
thread.start_new_thread(poscicao2,(1,))

janela.mainloop()