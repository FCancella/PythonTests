from tkinter import *


janela = Tk()
janela.title('Conversao C para F')
janela.geometry('200x150')


def bt_onclick():
    print (int(ed.get()))
    C = int(ed.get())
    lb['text'] = (C * 9/5) + 32
    
ed = Entry(janela)
ed.place(x= 40, y= 30)

bt = Button (janela, text ='Converter', width = 10, command=bt_onclick)
bt.place(x= 60, y= 55)

lb = Label(janela, text='')
lb.place (x= 85, y=85)

textol = Label (text='Celcius para Farenheit')
textol.pack()


janela.mainloop()
