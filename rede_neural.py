# código feito do zero por Leonardo Packer
#feed forward

# explicações básicas sobre redes neurais
# a entrada é um numero que tem um peso da conexão com o nó/neurônio da camada OCULTA ( a do meio )
# esse peso é multiplicado e vai gerar um valor na camada OCULTA
# esse irá multiplicar o valor com o ultimo peso, gerando um valor para a SAÍDA
# os pesos serão colocados em matrizes para ser feito o cálculo

# 10 > entrada > 10 * 0.2(peso) > oculto > 2 * 0.5(peso) > saída > 1

# o algoritmo irá comparar a saída com o resultado correto, em caso de erro
# irá calcular a diferença, e começará a alterar os pesos para chegar mais próximo do resultado

# no final do cálculo deverá ser adicionada uma tendência (bias)
# depois do BIAS vc ativa o neurônio colocando a Função de ativação

# Sigmoid: qualquer valor que vc colocar, o sigmoid irá entender como 0 ou 1

# até aqui temos o neurônio oculto, então devemos fazer os cálculos de matrizes, adicionar o BIAS
# e a função de ativação