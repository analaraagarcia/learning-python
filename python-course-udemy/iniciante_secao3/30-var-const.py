"""
Variáveis, constantes e complexidade de código
CONSTANTE = não mudam
muitas condições no mesmo if (ruim)
   <- contagem complexidade (ruim)
"""

velocidade = 61 # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar pega

velocidade_carro_radar_1 = velocidade > RADAR_1
multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)and velocidade > RADAR_1

if velocidade_carro_radar_1:
    print('Velocidade carro passou do radar 1')

if multado_radar_1 and velocidade_carro_radar_1:
    print('Carro multado em radar 1')