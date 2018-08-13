import numpy as np
import pandas as pd
import random as r
import math
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def dist_euclidiana (ponto1,ponto2):
	dim, soma = len(ponto1), 0 #len retorna o número de caracteres de uma string
	for i in range(dim): #A função range() cria uma sequência numérica. Padrão o parâmetro start será igual a 0 e o step igual a 1. Ex: cria uma sequencia de 2 a 10 indo de 2 em 2 (list(range(2, 10, 2)) --->[2, 4, 6, 8])
		soma += math.pow(ponto1[i] - ponto2[i], 2)
	return math.sqrt(soma)

def calcularPontoMedio(lista):
    somaX, somaY, somaZ = 0, 0, 0
    pontoMedio=[]
    tam=len(lista)
    print(lista)

    for i in lista:
        somaX+=(lista[0][i])
    for j in lista:
        somaY+=(lista[1][i])
    for k in lista:
        somaZ+=(lista[2][i])

    pontoMedio.append(somaX/tam)
    pontoMedio.append(somaY/tam)
    pontoMedio.append(somaZ/tam)

    print(somaX)
    return(pontoMedio)

def plotarPontos(df, numero):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xs=numero.p1, ys=numero.p2, zs=numero.p3, c='r', marker = 'o')
    ax.scatter(xs=df.p1, ys=df.p2, zs=df.p3, marker= '^')
    plt.show()


with open('dados1.csv', 'r') as reader:
    dados = pd.read_csv('dados1.csv', usecols=['p1','p2','p3'])
print(1)
centroides= dados.sample(3);
print(2)
qualCluster=[]

for t in range(10):
    distancias = [[] for i in range(len(centroides))]

    for j in range (len(centroides)):
        for i in range(len(dados)):
            distancias[j].append(dist_euclidiana(centroides.iloc[j],  dados.iloc[i]))

    for i in range(len(dados)):
        if distancias[0][i]<distancias[1][i] and distancias[0][i]<distancias[2][i]:
            qualCluster.append(0)
        elif distancias[1][i]<distancias[0][i] and distancias[1][i]<distancias[2][i]:
            qualCluster.append(1)
        else:
            qualCluster.append(2)

    cluster1,cluster2, cluster3, fakePoint=[], [], [], []

    for i in range(len(dados)):
        if qualCluster[i] == 0:
            cluster1.append(dados.loc[i])
        elif qualCluster[i] == 1:
            cluster2.append(dados.loc[i])
        else:
            cluster3.append(dados.loc[i])

    fakePoint.append(calcularPontoMedio(cluster1))
    fakePoint.append(calcularPontoMedio(cluster2))
    fakePoint.append(calcularPontoMedio(cluster3))
