import random
lista = []
print ("Names List: ")
print ("0- Felipe")
print ("1- Antonio")
print ("2- Gustavo")
print ("3- Eric ")
print ("4- Callou")
print ("5- Joaquim")
print ("6- Pedro")
print ("7- Lucas")
print ("8- Gabriel")
print ("9- Rodrigo")
lista.append("Name: Felipe ; Age: 16; Class: 10c1")     #namelist[0]
lista.append("Name: Antonio  ; Age; 16; Class: 9c1")    #namelist[1]
lista.append("Name: Gustavo ; Age: 16; Class: 11c2")    #namelist[2]
lista.append("Name: Eric ; Age: 16; Class: 9c1")        #namelist[3]
lista.append("Name: Callou; Age: 16; Class: 12c2")      #namelist[4]
lista.append("Name: Joaquim ; Age: 17; Class: 11c1")    #namelist[5]
lista.append("Name: Pedro ; Age: 16; Class: 10c1")      #namelist[6]
lista.append("Name: Lucas; Age: 13; Class: 7c1")        #namelist[7]
lista.append("Name: Gabriel ; Age: 13; Class: 7c2")     #namelist[8]
lista.append("Name: Rodrigo ; Age: 17; Turma: 12c2")    #namelist[9]

resposta = (input ("Seu nome esta na lista?: "))
while True:
    if resposta.upper() == "SIM":
         numero = (int (input("What's your number?: ")))
         nameindex = numero
         print (lista[nameindex])
    else:
        nn = input ("What's your name?: ")
        na = input ("What's your age?: ")
        nc = input ("What's your class?: ")
        lista.append("Name: {} ; Age: {}; Class: {}".format(nn, na, nc))
        print (lista[-1])
        print ('SEJA BEM VINDO A FESTA, {}!!'.format(nn))
