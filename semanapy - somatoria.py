def summation(num):
    numeros_da_somatoria = []
    for i in (range (num + 1)):               #Para cada elemento (numero) em um range de 0 até X+1 (x+1 pois o range nao contaria a ultima casa so valhor escolhido pelo usuario)
        numeros_da_somatoria.append(i)        #Adicione ele na 'numeros_da_somatoria'
    return (sum(numeros_da_somatoria))        #Retorne a somatoria dessa lista
print (summation(120))
