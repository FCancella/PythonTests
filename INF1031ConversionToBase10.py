#Felipe Cancella 2210487

import random
while True:
    #Escolhas
    j=(input('\n---\nPedra/Papel/Tesoura: ')).upper()
    m=random.choice(['PEDRA', 'PAPEL', 'TESOURA'])
    r=(j+m)

    print('\nJogador: %s' %j)
    print('Maquina: %s' %m)
    
    #Resultados
    if r=='PEDRATESOURA' or r=='PAPELPEDRA' or r=='TESOURAPAPEL':
        print('\nVOCÊ GANHOU!')
    elif j==m:
        print('\nEMPATE')
    else:
        print('\nVOCÊ PERDEU!')

    #Continuar?
    cont = input("\nQuer jogar mais uma? (s/n): ")
    if cont.upper() == "S":
        continue

    print("\nTchau...")
    break 
