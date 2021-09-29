n1 = float (input ('Numero :'))
n2 = float (input ('Outro numero:'))
print ('+ SOMA')
print ('- DIMINUIR')
print ('* MULTIPLICAR')
print ('** ELEVAR')
print ('/ DIVIDIR')
f = input ('Oque deseja fazer? ex: +, -, *, **, /:')
s = ( n1 + n2)
v = ( n1 * n2)
m = ( n1 - n2)
e = ( n1 ** n2)
d = ( n1 / n2)
if (f == '+'):
    print (s)
elif (f == '*'):
    print (v)
elif (f == '-'):
    print (m)
elif (f == '**'):
    print (e)
if (f == '/'):
    print (d)

print ("=====!!!PARABENS!!!=====")
