import numpy as np
import pandas as pd
import random as r
import math
from matplotlib import pyplot as plt

#classe ponto
#class Ponto(object):
#    def __init__(self, nome, valor):
#        self.__nome = nome

# 1 Leitura do arquivo

#with open('dados1.csv', 'r') as reader:
df = pd.read_csv('dados1.csv',header=None)#, usecols=['p1','p2','p3'])
print(df)

#Criar os pontos
pontos=[]
#for j in df[i][j]:
#   for i in df[i]:
    pontos=list(range(0, i, j))
#    for j in range(colunas):
#        if(j == colunas - 1):
#            print("%d" %df[i][j], end = "")
#        else:
#            print("%d" %df[i][j], end = "")
#print()
# 2 Criar uma função distância que recebe 2 pontos
#def dist_euclidiana (ponto1, ponto2):
#	dim, soma = len(ponto1), 0 #len retorna o número de caracteres de uma string
#	for i in range(dim): #A função range() cria uma sequência numérica. Padrão o parâmetro start será igual a 0 e o step igual a 1. Ex: cria uma sequencia de 2 a 10 indo de 2 em 2 (list(range(2, 10, 2)) --->[2, 4, 6, 8])
#		soma += math.pow(ponto1[i] - ponto2[i], 2)
#	return math.sqrt(soma)
#print('%.2f' % dist_euclidiana(ponto1, ponto2))

# 3 Sortear os centroides

# 4 Conversar com o Daniel sobre como plotar os pontos lidos e eventualmente pintar os centroides com uma cor diferente

# 5 Calcular as distâncias entre todos os pontos e os centroides

# 6 Atribuir os clusters

# 7 Recalcular os centroides

# 8 Repita até que ninguém mais se mova ou o número máximo de iterações for alcançado
