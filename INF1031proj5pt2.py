
# Conversao de numeros para base 10 de forma recursiva e iterativa
# Conversion of numbers to base 10 recursively and iteratively

#Recursiva
def unfunc(num,base):
    s = 'ABCDEF'
    x = 0
    if num == 0 or num == '':
        return x
    elif num[-1] in s:
        pos = int(s.index(num[-1]))
        x += (10 + pos)
        return unfunc(num[:-1] , base)*base + x # Multiplica pela base pra n precisar criar um 3 parametro ("RECURSAO * b" é equivalente a ir elevando a base por 0, 1, 2, 3, etc e multiplicando isso pelo resultado)
    else:
        pos = int(num[-1])
        x += pos
        return unfunc(num[:-1],base)*base + x
        
print ('\nRecursiva Reversa -')
print ('10011 na base 2 para base 10 -',unfunc('10011',2))
print ('CAD na base 16 para base 10 -',unfunc('CAD',16))
print ('12C na base 16 para base 10 -',unfunc('12C',16))
print ('116 na base 16 para base 10 -',unfunc('116',16))

#Iterativa
def uniter(num,base):
    s = 'ABCDEF'
    f = len(num)
    x = 0
    for i in range (f):
        if num[-1] in s:
            pos = int(s.index(num[-1]))
            x += (10 + pos)*(base**i)
        else:
            pos = int(num[-1])
            x += pos*(base**i)
        num = num[:-1]
    return x

print ('\nIterativa Reversa -')
print ('10011 na base 2 para base 10 -',uniter('10011',2))
print ('CAD na base 16 para base 10 -',uniter('CAD',16))
print ('12C na base 16 para base 10 -',uniter('12C',16))
print ('116 na base 16 para base 10 -',uniter('116',16))
print ('\n')