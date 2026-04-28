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
    dados_guardados2=dados_guardados.copy()
    dados_guardados2.append(dados_rolados[dados_a_guardar])
    dados_finais=[dados_rolados2,dados_guardados2]
    return dados_finais

def remover_dado(dados_rolados, dados_no_estoque, dados_para_remover):
    dados_rolados2=dados_rolados.copy()
    dados_rolados2.append(dados_no_estoque[dados_para_remover])
    dados_no_estoque_2=dados_no_estoque.copy()
    del dados_no_estoque_2[dados_para_remover]
    return [dados_rolados2, dados_no_estoque_2]