import random
def rolar_dados(n): 
    resultados=[]
    i=0
    while i<n:
        resultados.append(random.randint(1,6))
        i+=1
    return resultados

def guardar_dado(dados_rolados, dados_guardados, dados_a_guardar):
    dados_rolados2=dados_rolados.copy()
    del dados_rolados2[dados_a_guardar]
    dados_guardados2=dados_guardados
    dados_guardados2.append(dados_rolados[dados_a_guardar])
    dados_finais=[dados_rolados2,dados_guardados2]
    return dados_finais

