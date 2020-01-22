import time
import random
import math

# lista simples
pessoas = [('Amanda', 'CWB'),
           ('Pedro', 'GIG'),
           ('Marcos', 'POA'),
           ('Priscila', 'FLN'),
           ('Jessica', 'CNF'),
           ('Paulo', 'GYN')]

destino = 'GRU'

# criando dicionario de voos
voos = {}
for linha in open('voos.txt'):
    # repetição para importar o arquivo de voos
    #print(linha)
    _origem, _destino, _saida, _chegada, _preco = linha.split(',')
    # colocar _ antes da variavel faz se tornar uma variavel local.
    # linha.split vai quebrar o que estiver entre aspas, pegando apenas os valores sem espaço e sem virgula
    voos.setdefault((_origem, _destino), [])
    voos[(_origem, _destino)].append((_saida, _chegada, int(_preco)))
    
# [1,4, 3,2, 7,3, 6,3, 2,4, 5,3]
def imprimir_agenda(agenda):
    id_voo = -1
    for i in range(len(agenda) // 2):
        nome = pessoas[i][0] 
        origem = pessoas[i][1]
        id_voo += 1
        ida = voos[(origem, destino)][agenda[id_voo]]
        id_voo += 1
        volta = voos[(destino, origem)][agenda[id_voo]]
        print('%10s%10s %5s-%5s R$%3s %5s-%5s R$%3s' % (nome, origem, ida[0], ida[1], ida[2],
                                                       volta[0], volta[1], volta[2]))
        
agenda = [1,4, 3,2, 7,3, 6,3, 2,4, 5,3]
imprimir_agenda(agenda)

# função para calcular minutos
def get_minutos(hora):
    x = time.strptime(hora, '%H:%M')
    #strptime transforma string para tempo
    minutos = x[3] * 60 + x[4]
    # horas * 60 + minutos
    return minutos

get_minutos('6:13')
# chamando a função pra calcular minutos

# criação da função de custo, a mais importante em algoritmo de otimização
def funcao_custo(solucao):
    preco_total = 0
    ultima_chegada = 0
    primeira_partida = 1439
    # 23 * 59, seria o voo que sairia mais tarde
    id_voo = -1
    for i in range(len(solucao) // 2):
        # executa o for somente 6 vezes
        origem = pessoas[i][1]
        id_voo += 1
        ida = voos[(origem, destino)][solucao[id_voo]]
        id_voo += 1
        volta = voos[(destino, origem)][solucao[id_voo]]
        # aqui ja temos os preços e valores
        
        preco_total += ida[2]
        # indice 2 é o indice onde esta o preço na lista de ida
        preco_total += volta[2]
        
        if ultima_chegada < get_minutos(ida[1]):
            ultima_chegada = get_minutos(ida[1])
            
        if primeira_partida > get_minutos(volta[0]):
            primeira_partida = get_minutos(volta[0])
            
    total_espera = 0
    id_voo = -1
    for i in range(len(solucao) // 2):
        origem = pessoas[i][1]
        id_voo += 1
        ida = voos[(origem, destino)][solucao[id_voo]]
        id_voo += 1
        volta = voos[(destino, origem)][solucao[id_voo]]
        
        total_espera +=  ultima_chegada - get_minutos(ida[1])
        #pega o valor da ultima chegada, subtrai com os minutos do voo de ida(chegada)
        total_espera += get_minutos(volta[0]) - primeira_partida
        #valor total da espera
        
    if ultima_chegada > primeira_partida:
        #se cair nesse if, significa que a ultima chegada foi no dia seguinte
        preco_total += 50
        
    return preco_total + total_espera
    # considerando que cada minuto que a pessoa fica, considera 1 real
    
funcao_custo(agenda)
        
# criação dos algoritmos de IA
def pesquisa_randomica(dominio, funcao_custo):
    melhor_custo = 999999999
    for i in range(0, 10000):
        solucao = [random.randint(dominio[i][0], dominio[i][1]) for i in range(len(dominio))]
        custo = funcao_custo(solucao)
        if custo < melhor_custo:
            melhor_custo = custo 
            melhor_solucao = solucao
        return melhor_solucao
    
    
dominio = [(0, 9)] * (len(pessoas) * 2)
# total de 10 voos

solucao_randomica = pesquisa_randomica(dominio, funcao_custo)
custo_randomica = funcao_custo(solucao_randomica) 
imprimir_agenda(solucao_randomica)

# Algoritmo de Hill Climb / Subida da encosta
def subida_encosta(dominio, funcao_custo):
    solucao = [random.randint(dominio[i][0], dominio[i][1]) for i in range(len(dominio))]
    while True:
        vizinhos = []
        
        for i in range(len(dominio)):
            if solucao[i] > dominio[i][0]:
                if solucao[i] != dominio[i][1]:
                    vizinhos.append(solucao[0:i] + [solucao[i] + 1] + solucao[i + 1:])
                # se esse valor for diferente de 9 (numero de voos), posso incrementar para frente
                if solucao[i] < dominio[i][1]:
                    if solucao[i] != dominio[i][0]:
                        vizinhos.append(solucao[0:i] + [solucao[i] - 1] + solucao[i + 1:])
        atual = funcao_custo(solucao)
        melhor = atual
        for i in range(len(vizinhos)):
            custo = funcao_custo(vizinhos[i])
            if custo < melhor:
                melhor = custo
                solucao = vizinhos[i]
                
        if melhor == atual:
            break
    return solucao

solucao_subida_encosta = subida_encosta(dominio, funcao_custo)
custo_subida_encosta = funcao_custo(solucao_subida_encosta) 
imprimir_agenda(solucao_subida_encosta)
                        

# Algoritmo de Temperada Simulada / Recozimento
def tempera_simulada(dominio, funcao_custo, temperatura = 10000.0, resfriamento = 0.95, passo = 1):
    solucao = [random.randint(dominio[i][0], dominio[i][1]) for i in range(len(dominio))]
    
    while temperatura > 0.1:
        
    


