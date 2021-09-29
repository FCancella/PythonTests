# *range apresenta os numero diretamente em forma de "lista",
# diferente do range que só faria isso com o for...in

def contar(n):
    return [*range(1, n+1)]
print (contar(17))