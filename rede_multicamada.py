
import numpy as np

# função de ativação
def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

def sigmoidDerivada(sig):
    return sig * (1 - sig)

#a = sigmoid(0.5)
#b = sigmoidDerivada(a)

#implementação camada oculta (operação xor)
    
entradas = np.array([[0,0],
                    [0,1],
                    [1,0],
                    [1,1]])
    
saidas = np.array([[0],[1],[1],[0]])

pesos0 = np.array([[-0.424, -0.740, -0.961],
                   # pesos x1 / pesos x2
                   [0.358, -0.577, -0.469]])

pesos1 = np.array([[-0.017], [-0.893], [0.148]])

#pesos0 = 2*np.random.random((2,3)) - 1
#pesos1 = 2*np.random.random((3,1)) - 1

epocas = 21000
taxaAprendizagem = 0.5
momento = 1

for j in range(epocas):
    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada, pesos0)
    # faz o dot unir os arrays entradas com o array pesos0
    camadaOculta = sigmoid(somaSinapse0)
    
    somaSinapse1 = np.dot(camadaOculta, pesos1)
    camadaSaida = sigmoid(somaSinapse1)
    
    # calculo erro = respostaCorreta - respostaCalculada ou
    # somar os erros e dividir pela qtd de respostas
    
    erroCamadaSaida = saidas - camadaSaida
    mediaAbsoluta = np.mean(np.abs(erroCamadaSaida))
    print("Erro: " + str(mediaAbsoluta))
    
    derivadaSaida = sigmoidDerivada(camadaSaida)
    deltaSaida = erroCamadaSaida * derivadaSaida
    
    #matriz transposta (linhas p colunas e colunas p linhas)
    pesos1Transposta = pesos1.T
    
    deltaSaidaXPeso = deltaSaida.dot(pesos1Transposta)
    # acima: ainda não é o resultado final, precisamos fazer 
    # a multiplicação pelo valor da Derivada
    
    deltaCamadaOculta = deltaSaidaXPeso * sigmoidDerivada(camadaOculta)
    
    camadaOcultaTransposta = camadaOculta.T
    pesosNovo1 = camadaOcultaTransposta.dot(deltaSaida)
    
    # aplicação do back propagation
    pesos1 = (pesos1 * momento) + (pesosNovo1 * taxaAprendizagem)   
    
    camadaEntradaTransposta = camadaEntrada.T
    pesosNovo0 = camadaEntradaTransposta.dot(deltaCamadaOculta)
    pesos0 = (pesos0 * momento) + (pesosNovo0 * taxaAprendizagem)
    
    
    