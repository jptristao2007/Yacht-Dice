import random
def rolar_dados(n): 
    resultados=[]
    i=0
    while i<n:
        resultados.append(random.randint(1,6))
        i+=1
    return resultados