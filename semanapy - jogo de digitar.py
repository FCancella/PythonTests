#Bibliotecas a serem usadas - os para limpar o sistema - random para a lista de palavras - time para o cronometro
import os
import random
import time

# limpa o terminal
os.system('cls')

#Lista de palavras escolhidas e que serao randomizadas
Palavras = ['Dormir', 'Casar', 'Ler', 'Escrever', 'Brigar', 'Pular', 'Andar', 'Beber', 'Estudar', 'Caminhar', 'Pedalar', 'Pular', 'Passear']
Palavras_random = random.sample(Palavras, 10)

#contagem regressiva

contagem = 3
while contagem > 0:
    time.sleep(1)
    print(contagem, '...', sep="")
    contagem -=1
time.sleep(0.5)
print ('JÁ!')
time.sleep(0.5)



# limpa o terminal
os.system('cls')

#inicia o cronometro
inicio = time.time()

#funcao que vai mostrar a palavra randomizada e recolher o input do jogar
pontos = 0
for palavra in Palavras_random:
    print (palavra)
    entrada = input ()
    if entrada.upper() == palavra.upper():
        pontos = pontos + 1
    os.system('cls')

#finaliza o cronometro
fim = time.time()
tempo_cronometrado = fim - inicio

#Limita o resultado do cronometro em uma casa decimal
tempo = round(tempo_cronometrado, 1)

#RESULTADO
print ('\nPARABÉNS!!! VOCÊ FEZ {} PONTOS EM UM TEMPO DE {} SEGUNDOS \n'. format (pontos, tempo))
