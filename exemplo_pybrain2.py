from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import SoftmaxLayer
from pybrain.structure.modules import SigmoidLayer

# 2 = 2 neuronios camada entrada
# 3 = 3 neuronios camada oculta
# 1 = 1 neuronio saida
rede = buildNetwork(2, 3, 1)

# tambem posso personalizar a rede
# aqui setamos que a camada de saída irá usar SoftmaxLayer
# desligamos o bias, e setamos a camada oculta usando função sigmoid
#rede = buildNetwork(2, 3, 1, outclass = SoftmaxLayer,
#                    hiddenclass = SigmoidLayer, bias = False)

# a entrada é do tipo linear layer
#print(rede['in'])

# a camada oculta possui funçao de ativação sigmoid
#print(rede['hidden0'])

# a saida possui linear layer
#print(rede['out'])

#print(rede['bias'])

# 2 atributos previsores e 1 classe
base = SupervisedDataSet(2, 1)
base.addSample((0, 0), (0, ))
base.addSample((0, 1), (1, ))
base.addSample((1, 0), (1, ))
base.addSample((1, 1), (0, ))

# prints de teste
print(base['input'])
print(base['target'])

# para efetivamente fazer o treinamento
treinamento = BackpropTrainer(rede, dataset = base, learningrate = 0.01,
                              momentum = 0.06)

for i in range(1, 30000):
    erro = treinamento.train()
    if i % 1000 == 0:
        print("Erro: %s" % erro)
        
print(rede.activate([0, 0]))
print(rede.activate([1, 0]))
print(rede.activate([0, 1]))
print(rede.activate([1, 1]))

