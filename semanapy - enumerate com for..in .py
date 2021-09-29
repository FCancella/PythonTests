import os
os.system('cls')

Lista_de_frutas = ['maca', 'banana', 'uvas', 'pesego', 'pera', 'cereja', 'abacaxi']

#Para cada numero de futas e frutas na lista Lista de fruta, print numero da fruta, fruta (contagem a partir do numero 1, e nao 0)
print ('VENHA COMPRAR!!\n')
for x, y in enumerate(Lista_de_frutas, 1):
    print (x,'-',y.capitalize())
print ('')