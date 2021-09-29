animais_sem_pelo = ('Peixe', 'Tartaruga', 'Tatu')
animais_com_pelo = ('Cachorro', 'Gato', 'Leao')

animais_gerais = (animais_sem_pelo + animais_com_pelo)

print ('\n--- No nosso zoologico temos: --- \n')
for animais in animais_gerais:
    print ('-', animais)