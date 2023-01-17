
#Registra quantas tentativas foram feitas de forma aleatoria até gerar "Qty" numeros iguais que vao de um range de "first" até "last".
#As tentativas sao registradas no arquivo tenta.txt

#Attempts are recorded in the file tenta.txt 
#Register how many attempts were randomly made until generating "Qty" equal numbers ranging from "first" to "last".

import random
arq=open('tenta.txt', 'w')

def ig(Qty,first,last):
    attempts=1
    numbers=[]
    while True:
        found=False
        #Generate "Qty" random numbers and add them to a list
        for i in range (Qty):
            x=random.randint(first,last)
            numbers.append(x)

        #Check if all numbers are the same
        for i in numbers[1:]:
            if i != numbers[0]:
                attempts+=1
                arq.write(str(numbers))
                arq.write('\n')
                numbers=[]
                found=False
                break
            found=True

        if found==True:
            arq.write(str(numbers)) #print last attempt on the file
            arq.write(" Attempts: %d" %attempts)

            print('%d attempts' %attempts)
            print(numbers)
            break
            
            
ig(4, 1,8)
arq.close()