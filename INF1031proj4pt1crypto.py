
# Criptografa e descriptografa o texto com base em um numero (fator) e usa a posicao de cada caractere na tabela ASCII
# Encrypts and decrypts text based on a number (fator) and uses the position of each character in the ASCII table

def encrip(palavra, fator):
    x=''
    for i in palavra:
        if ord(i)+fator > 122:
            x+= chr(ord(i)+fator-91)
        else:
            x+= chr(ord(i)+fator)
    return x

def decrip(palavra, fator):
    y=''
    for i in palavra:
        if ord(i)-fator < 32:
            y+= chr(ord(i)-fator+91)
        else:
            y+= chr(ord(i)-fator)
    return y

palavra = input('Digite uma palavra:')
print('\nORIGINAL')
print(palavra)

print('\nCRIPTOGRAFADA')
print (encrip(palavra,11))

print('\nDESCRIPTOGRAFADA')
print (decrip(encrip(palavra,11), 11))

print('\n')