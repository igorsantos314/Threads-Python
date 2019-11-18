import _thread as th, time
from tkinter import *
from tkinter import messagebox

def addProgressBar(val):
    for i in range(100):
        time.sleep(1)
        lblProgress['text'] += ' ' 

        valor = int(lblValor['text']) + 1
        lblValor['text'] = str(valor)

def iniciarContagem():
    th.start_new_thread(addProgressBar, (1,))

def mensagem():
    messagebox.showinfo('Perceba que a Progree Bar Continuas :)')

janela = Tk()
janela.geometry('400x400')
janela.title('Barra de Progresso')

lblInfo = Label(text='Progresso: ')
lblInfo.place(x=10, y=340)

lblValor = Label(text='0', fg='green')
lblValor.place(x=90, y=340)

lblProgress = Label(text='', font='Arial 12 bold', bg='green')
lblProgress.place(x=10, y=360)

btInicio = Button(text='Iniciar Carregamento', command=iniciarContagem)
btInicio.pack()

btM = Button(text='Mensagem', command=mensagem)
btM.pack()

janela.mainloop()