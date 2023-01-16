
# Criptografa e descriptografa o texto com base em uma palavra chave (senha) e usa a posicao de cada caractere na tabela ASCII
# Encrypts and decrypts text based on a keyword (senha) and uses the position of each character in the ASCII table

# senha: "ABACAXI"

def encrip(palavra, senha):
    #Deixa as duas do mesmo tamanho
    if len(palavra) > len(senha):
        senha = senha*len(palavra)
        senha = senha[:(len(palavra))]
    x=''
    #Para cada letra: somar fator ou somar fator e tirar 26 (VOLTAR PRO COMECO)
    for i in palavra:
        fator = ord(senha[0])-65
        if ord(i)+fator > 90:
            x+= chr(ord(i)+fator-26)
        else:
            x+= chr(ord(i)+fator)
        palavra = palavra[1:]
        senha = senha[1:]
    return x

def desencrip(palavra, senha):
    if len(palavra) > len(senha):
        senha = senha*len(palavra)
        senha = senha[:(len(palavra))]
    x=''
    for i in palavra:
        fator = ord(senha[0])-65
        if ord(i)-fator < 65:
            x+= chr(ord(i)-fator+26)
        else:
            x+= chr(ord(i)-fator)
        palavra = palavra[1:]
        senha = senha[1:]
    return x

palavra = (input('Digite uma palavra:')).upper()

print('\nORIGINAL')
print(palavra)

print('\nCRIPTOGRAFADA')
cripto = encrip(palavra,'ABACAXI')
print(cripto)

print('\nDESCRIPTOGRAFADA')
descripto = desencrip(cripto, 'ABACAXI')
print (descripto)

print('\n')