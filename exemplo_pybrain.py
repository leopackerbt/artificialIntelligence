from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer, BiasUnit
from pybrain.structure import FullConnection

rede = FeedForwardNetwork()

camadaEntrada = LinearLayer(2)
camadaOculta = SigmoidLayer(3)
camadaSaida = SigmoidLayer(1)

#bias camada oculta
bias1 = BiasUnit()

#bias camada saida
bias2 = BiasUnit()

# adicionando as camadas dentro da rede (principal)
rede.addModule(camadaEntrada)
rede.addModule(camadaOculta)
rede.addModule(camadaSaida)
rede.addModule(bias1)
rede.addModule(bias2)

# ligação entre camada entrada e camada oculta
entradaOculta = FullConnection(camadaEntrada, camadaOculta)
ocultaSaida = FullConnection(camadaOculta, camadaSaida)

# ligação bias 1 para camada oculta
biasOculta = FullConnection(bias1, camadaOculta)

# ligação bias 2 para camada saida
biasSaida = FullConnection(bias2, camadaSaida)

# a rede irá ser construida aqui
rede.sortModules()

print(rede)
print(entradaOculta.params)
print(ocultaSaida.params)
print(biasOculta.params)
print(biasSaida.params)
