from funcoes import *

cartela= { 'regra_simples': {1:-1,2:-1,3:-1,4:-1,5:-1,6:-1},
          'regra_avancada': {'sem_combinacao':-1,
                             'quadra':-1,
                             'full_house':-1,
                             'sequencia_baixa':-1,
                             'sequencia_alta':-1,
                             'cinco_iguais':-1}}

for rodada in range(12):
    dados_rolados=rolar_dados(5)
    dados_guardados=[]
    rerrolagens=0
    jogada_finalizada=False 

    while jogada_finalizada == False:

        print("\nDados rolados:", dados_rolados)
        print("Dados guardados:", dados_guardados)
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        opcao=input()

        if opcao == '1':
            print(f"Digite o índice do dado a ser guardado (0 a {len(dados_rolados)-1}):")
            i = int(input())
            dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, i)
        
        elif opcao == '2':
            print(f"Digite o índice do dado a ser guardado (0 a {len(dados_guardados)-1}):")
            i = int(input())
            dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, i)
        
        elif opcao == '3':
            if rerrolagens >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados_rolados = rolar_dados(5 - len(dados_guardados))
                rerrolagens += 1
        
        elif opcao == '4':
            imprime_cartela(cartela)
        
        elif opcao == '0':
            print("Digite a combinação desejada:")
            categoria = input()

            dados = dados_guardados + dados_rolados

            if categoria in ['1','2','3','4','5','6']:
                numero= int(categoria)

                if cartela['regra_simples'][numero] != -1:
                    print("Essa combinação já foi utilizada.")
                else:
                    cartela = faz_jogada(dados, categoria, cartela)
                    jogada_finalizada = True

            elif categoria in cartela['regra_avancada']:
                if cartela['regra_avancada'][categoria] != -1:
                    print("Essa combinação já foi utilizada.")
                else:
                    cartela = faz_jogada(dados, categoria, cartela)
                    jogada_finalizada = True
            
            else:
                print("Combinação inválida. Tente novamente.")
        
        else:
            print("Opção inválida. Tente novamente.")

pontuacao = 0

soma_simples = sum(cartela['regra_simples'].values())
pontuacao += soma_simples

if soma_simples >= 63:
    pontuacao += 35

pontuacao += sum(cartela['regra_avancada'].values())

imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao}")