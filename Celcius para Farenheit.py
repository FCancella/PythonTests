print ('OPCAO 1 - C para F')
print ('OPCAO 2 - F para C')
Q = input ('Oque deseja fazer? 1 ou 2 :')
if (Q == '1'):
    C = float(input('Temperatura C: '))
    print("Temperatura em Farehnheit:", (C * (9 / 5) + 32))
else:
    F = float(input('Temperatura F: '))
    print("Temperatura em Celcius: ", ((F - 32) * (5 / 9)))