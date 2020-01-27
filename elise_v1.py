# Teste de Machine Learning em um jogo de jokenpo aleatório
# O desafio é fazer uma probabilidade da máquina saber
# a chance que você tem de jogar pedra, papel ou tesoura
# Baseado no histórico de jogadas
# Cálculos feitos utilizando regra de 3 simples
import time
import random
from random import choices

s = "sim"
n = "nao"
pd = "pedra"
pp = "papel"
t = "tesoura"
jogadas = 0
pedra = 0
tesoura = 0
papel = 0
possibilidades = [0, 1, 2]
jogada_elise = "x"
win1 = "Você venceu!"
win2 = "Elise venceu!"
vit_player = 0
vit_elise = 0
empates = 0

print("###########################")
print("Bem-vindo ao Jokenpo VS Elise")
print("###########################")

time.sleep(1)
print("Você irá jogar contra a Elise, "
      "um robô que será treinado durante o jogo")

jogar = input("Está pronto para começar? ")
if jogar == s:
    time.sleep(0.5)
    jogada_player = input("pedra, papel ou tesoura? ")
    if jogada_player == pd:
        pedra += 1
        jogadas += 1
    elif jogada_player == pp:
        papel += 2
        jogadas += 1
    else:
        tesoura += 1
        jogadas += 1

porcentagem_papel = (pedra * 100) / jogadas
porcentagem_pedra = (tesoura * 100) / jogadas
porcentagem_tesoura = (papel * 100) / jogadas
pesos_jogada = [porcentagem_papel, porcentagem_pedra,
                porcentagem_tesoura]

time.sleep(0.5)
print("Aguardando a resposta de Elise")
time.sleep(1)
print("Elise está analisando seu histórico de jogadas...")
time.sleep(2)

jogada_maquina = choices(possibilidades, pesos_jogada, k=1)

if jogada_maquina[0] == 0:
    jogada_elise = pp
elif jogada_maquina[0] == 1:
    jogada_elise = t
else:
    jogada_elise = pd

print("Elise jogou %s" % jogada_elise)
time.sleep(0.5)

if jogada_player == jogada_elise:
    print("Houve um empate!")
    empates += 1
elif jogada_player == pd and jogada_elise == t:
    print(win1)
    vit_player += 1
elif jogada_player == pd and jogada_elise == pp:
    print(win2)
    vit_elise += 1
elif jogada_player == t and jogada_elise == pd:
    print(win2)
    vit_elise += 1
elif jogada_player == t and jogada_elise == pp:
    print(win1)
    vit_player += 1
elif jogada_player == pp and jogada_elise == pd:
    print(win1)
    vit_player += 1
else:
    print(win2)
    vit_elise += 1

time.sleep(0.5)
hist = input("Deseja ver o histórico de jogos? ")
if hist == s:
    print("Total de jogos: %d" % jogadas)
    print("Empates: %d" % empates)
    print("Suas vitórias: %d" % vit_player)
    print("Vitórias de Elise: %d" % vit_elise)
