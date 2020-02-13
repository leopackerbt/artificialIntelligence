# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:04:18 2020

@author: leonardo.packer
"""


import numpy as np
from sklearn import datasets

# função de ativação
def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

def sigmoidDerivada(sig):
    return sig * (1 - sig)

base = datasets.load_breast_cancer()
entradas = base.data
valoresSaida = base.target
saidas = np.empty([569, 1], dtype=int)
for i in range(569):
    saidas[i] = valoresSaida[i]

pesos0 = 2*np.random.random((30,3)) - 1
pesos1 = 2*np.random.random((3,1)) - 1

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
    
    
    