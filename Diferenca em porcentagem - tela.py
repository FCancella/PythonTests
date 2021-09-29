from tkinter import *

janela = Tk()
janela.title('Diferença')
janela.geometry('220x150')

texto1 = Label(text='Primeiro valor :')
texto1.place (x=2, y=27)

texto2 = Label(text='Segundo valor :')
texto2.place (x=2, y=47)

#textoP = Label(text='______%')
#textoP.place (x=120, y=82)

texto = Label (text='Diferença entre valores')
texto.pack()
#_____________________________________________
ed = Entry(janela)
ed.place(x= 92, y= 30, width = 120)

ed2 = Entry(janela)
ed2.place(x= 92, y= 50, width = 120)

lb = Label(janela, text='')
lb.place (x= 125, y=95)

def bt_onclick():
    V1 = int(ed.get())
    V2 = int(ed2.get())
    conta = ((V2-V1)/V1)*100
    lb['text'] = round(conta, 2), '%'

bt = Button (janela, text ='Calcular', width = 11, height = 4 ,command=bt_onclick)
bt.place(x= 3, y= 76)

janela.mainloop()