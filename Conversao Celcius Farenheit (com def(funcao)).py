print ('   OPCAO 1 - C para F')
print ('   OPCAO 2 - F para C')
oq = int (input ('   Oque deseja fazer? 1 ou 2 : '))
if oq == '1' or '_1':
    C = float(input('   Temperatura em Celcius: '))
    def cf(C):
     return C * (9 / 5) + 32
    print ('   Temperatura em Farehnheit:', cf(C))
elif oq == '2' or '_2':
    F = float(input ('   Diga uma Temp em F: '))
    def fc(F):
     return (F - 32) * (5 / 9)
    print ("   Temperatura em Farenheit:"(fc(F)))
