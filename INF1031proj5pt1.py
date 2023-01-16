
# Conversao de base de numeros na base 10 de forma recursiva e iterativa
# Base 10 Numbers conversion recursively and iteratively

#Recursiva
def func(num,base):
    s='ABCDEF'
    x=''
    if num/base > 0:
        if num%base > 9:
            x+= s[(num%base)-10]
            return func(num//base,base) + x
        x += str(num%base)
        return func(num//base,base) + x
    else:
        return x[::-1]
        
print ('\nRecursiva -')
print ('19 para base 2 -',func(19,2))
print ('278 para base 16 -',func(278,16))
print ('3245 para base 16 -',func(3245,16))
print ('300 para base 16 -',func(300,16))

#Iterativa
def iter(num,base):
    s='ABCDEF'
    y=''
    while num/base > 0:
        if num%base > 9:
            y+= s[(num%base)-10]
            num=num//base
        else:
            y += str(num%base)
            num=(num//base)
    return y[::-1]

print ('\nIterativa -')
print ('19 para base 2 -',iter(19,2))
print ('278 para base 16 -',iter(278,16))
print ('3245 para base 16 -',iter(3245,16))
print ('300 para base 16 -',iter(300,16))
print ('\n')