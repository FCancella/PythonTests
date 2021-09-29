
def find_average(nums):
    if sum(nums) == 0: # Se apenas tiver 0 na lista, ou a lista for vazia, a media será 0
        return 0
    else:               # Caso contrario, some todos os numeros, e divida pela quantidade de elementos (tirando os 0s)
        return (sum(nums)/(len(nums) - nums.count(0)))

print ( find_average ([-6, 29, 74, 36, 18, 13, 34, 47, 19, 0, 5, 60, 94, 95, -3]) )