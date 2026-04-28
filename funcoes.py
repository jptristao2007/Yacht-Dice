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

def calcula_pontos_regra_simples(faces):
    dic={1:0,2:0,3:0,4:0,5:0,6:0}
    for i in range(len(faces)):
        if faces[i] in dic.keys():
            dic[faces[i]]+=faces[i]
    return dic 
def calcula_pontos_soma(faces):
    soma_simples=0
    for numeros in faces:
        soma_simples+=numeros
    return soma_simples
def calcula_pontos_sequencia_baixa(faces):
    if (1 in faces and 2 in faces and 3 in faces and 4 in faces):
        return 15
    elif 2 in faces and 3 in faces and 4 in faces and 5 in faces:
        return 15
    elif 3 in faces and 4 in faces and 5 in faces and 6 in faces:
        return 15 
    else:
        return 0 
def calcula_pontos_sequencia_alta(faces):
    if 1 in faces and 2 in faces and 3 in faces and 4 in faces and 5 in faces:
        return 30
    elif 2 in faces and 3 in faces and 4 in faces and 5 in faces and 6 in faces:
        return 30
    else:
        return 0
    
def calcula_pontos_full_house(dados):
    vezes={1:0,2:0,3:0,4:0,5:0,6:0}
    for n in dados:
        vezes[n]+=1
    if 2 in vezes.values() and 3 in vezes.values():
        i=0
        soma=0
        while i<len(dados):
            soma+=dados[i]
            i+=1
        return soma
    else:
        return 0 

def calcula_pontos_quadra (dados):
    vezes={1:0,2:0,3:0,4:0,5:0,6:0}
    for n in dados:
        vezes[n]+=1
    for v in vezes.values():

        if v>=4:
            i=0
            soma=0
            while i<len(dados):
                soma+=dados[i]
                i+=1
            return soma
    
    return 0 

        
