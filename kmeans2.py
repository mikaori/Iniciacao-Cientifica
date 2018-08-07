import numpy as np
import pandas as pd
import random as r
import math
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#construindo a main
def main():


if __name__ == "__main__":
    main()

def imprime_matriz(matriz):

    linhas = len(matriz)
    colunas = len(matriz[0])

    for i in range(linhas):
        for j in range(colunas):
            if(j == colunas - 1):
                print("%d" %matriz[i][j], end = "")
            else:
                print("%d" %matriz[i][j], end = "")
    print()

# 1 Leitura do arquivo

with open('dados1.csv', 'r') as reader:
    df = pd.read_csv('dados1.csv', usecols=['p1','p2','p3'])
print(df)

# 2 Criar uma função distância que recebe 2 pontos
def dist_euclidiana (ponto1,ponto2):
	dim, soma = len(ponto1), 0 #len retorna o número de caracteres de uma string
	for i in range(dim): #A função range() cria uma sequência numérica. Padrão o parâmetro start será igual a 0 e o step igual a 1. Ex: cria uma sequencia de 2 a 10 indo de 2 em 2 (list(range(2, 10, 2)) --->[2, 4, 6, 8])
		soma += math.pow(ponto1[i] - ponto2[i], 2)
	return math.sqrt(soma)

# 3 Sortear os centroides
def sortearPontos(df):
    return (df.sample(3))

# 4 Conversar com o Daniel sobre como plotar os pontos lidos e eventualmente pintar os centroides com uma cor diferente
#para duas dimensões
#plt.scatter(x=df.p1, y=df.p2)
#plt.scatter(x=numero.p1, y=numero.p2, c='r')
#plt.show();
def plotarPontos(df, numero):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xs=numero.p1, ys=numero.p2, zs=numero.p3, c='r', marker = 'o')
    ax.scatter(xs=df.p1, ys=df.p2, zs=df.p3, marker= '^')
    plt.show()

# 5 Calcular as distâncias entre todos os pontos e os centroides
def distanciaPontosCentroides():
    distCentroPonto=[];
    centroides = sortearPontos(df);
    #print(df.shape)
    #Shape eh uma funcao que DataFrame possui para retornar uma tupla com valor de (linha, coluna)
    #Ao colocar variavel.shape[0], estamos acessando o item que esta na primeira possicao da tupla
    #Ou seja, o numero de linhas no nosso caso. Com numero de linhas,
    #fazemos um for para o range (intervalo) de 0 a NumeroDeItens

    for j in range(centroides.shape[0]):
        for k in range(df.shape[0]):
            distCentroPonto.append(dist_euclidiana(centroides.iloc[j],  df.iloc[k]))
#print(len(distCentroPonto)) #quantidade de distancias calculadas

#imprime_matriz(distCentroPonto);
# 6 Atribuir os clusters
for ponto in distCentroPonto:
    for ponto+1 in distCentroPonto:
        for ponto+2 in distCentroPonto:
# 7 Recalcular os centroides

# 8 Repita até que ninguém mais se mova ou o número máximo de iterações for alcançado
