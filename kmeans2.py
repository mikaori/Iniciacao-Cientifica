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

def sumColumn(matrix):
    return np.sum(matrix, axis=0)

def calcularPontoMedio(lista):
    somaColunas,pontoMedio=[], []
    tam=len(lista)

    somaColunas=sumColumn(lista)
    for i in range(len(somaColunas)):
        pontoMedio.append(somaColunas[i]/tam)
    return(pontoMedio)

def plotarPontos(df, numero):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xs=numero.p1, ys=numero.p2, zs=numero.p3, c='r', marker = 'o')
    ax.scatter(xs=df.p1, ys=df.p2, zs=df.p3, marker= '^')
    plt.show()


with open('dadosteste.csv', 'r') as reader:
    dados = pd.read_csv('dadosteste.csv', usecols=['p1','p2','p3'])
centroides= dados.sample(3);

for t in range(10):
    distancias = [[] for i in range(len(centroides))]
    newDistancias=[[] for i in range(len(centroides))]
    cluster1,cluster2, cluster3, fakePoint=[], [], [], []

    for j in range (len(centroides)):
        for i in range(len(dados)):
            distancias[j].append(dist_euclidiana(centroides.iloc[j],  dados.iloc[i]))

    for i in range(len(dados)):
        if distancias[0][i]<distancias[1][i] and distancias[0][i]<distancias[2][i]:
            cluster1.append(dados.loc[i])
        elif distancias[1][i]<distancias[0][i] and distancias[1][i]<distancias[2][i]:
            cluster2.append(dados.loc[i])
        else:
            cluster3.append(dados.loc[i])

    fakePoint.append(calcularPontoMedio(cluster1))
    fakePoint.append(calcularPontoMedio(cluster2))
    fakePoint.append(calcularPontoMedio(cluster3))

    for j in range(len(fakePoint)):
        for i in range(len(dados)):
            newDistancias[j].append(dist_euclidiana(fakePoint.iloc[j],  dados.iloc[i])) #RETORNA 'list' object has no attribute 'iloc'?????PQ SE CENTROIDE TB É list????????

    for i in range(len(newDistancias)):
        centroides[i].append(min[distancias[0][i]])

print (centroides)
