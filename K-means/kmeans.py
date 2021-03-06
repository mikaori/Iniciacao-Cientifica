# -*- coding: utf-8 -*-
import csv
import numpy as np
import random as r
import math
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

def dist_euclidiana (ponto1,ponto2):
	dim, soma = len(ponto1), 0 #len retorna o número de caracteres de uma string
	for i in range(dim): #A função range() cria uma sequência
                             #numérica. Padrão o parâmetro start será
                             #igual a 0 e o step igual a 1. Ex: cria
                             #uma sequencia de 2 a 10 indo de 2 em 2
                             #(list(range(2, 10, 2)) --->[2, 4, 6, 8])
		soma += math.pow(ponto1[i] - ponto2[i], 2)
	return math.sqrt(soma)

def sumColumn(matrix):
	return np.sum(matrix, axis=0)

def calcularPontoMedio(lista):
	somaColunas,pontoMedio=[], []
	tam=len(lista)
	for i in range(2):
		somaColunas=sumColumn(lista)
		pontoMedio.append(somaColunas[i]/tam)
	return(pontoMedio)

def plotarPontos(df, numero):
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(xs=numero.p1, ys=numero.p2, zs=numero.p3, c='r', marker = 'o')
	ax.scatter(xs=df.p1, ys=df.p2, zs=df.p3, marker= '^')
	plt.show()

def pontoStringFloat (lista):
	return list(map(float, lista))

def comparaValores(lista, valor):
	index = 0;
	for i in range(len(lista)):
		if lista[i] == valor:
			index=i
	return index

def lerArquivo(arquivo):
	with open('dadosteste.csv', 'r') as arquivo:
		leitor = csv.reader(arquivo, delimiter=',')
		dados = []
		for ponto in leitor:
			dados.append(ponto)
		dados = dados[1:]
		dados = list(map(pontoStringFloat, dados))
	return dados

dados = lerArquivo('dados1.csv')
n = int(input('Qual o numero de centroides? '))
centroides = dados[0:n]
contador, t, achei = 0, 0, 0
ultimosCentroides = centroides.copy()

while (t < 20 and achei!=len(centroides)):
	distancias = [[] for i in range(len(centroides))]
	newDistancias=[[] for i in range(len(centroides))]
	cluster1,cluster2,cluster3,fakePoint=[],[],[],[]

	for j in range (len(centroides)):
		if (centroides[j] == ultimosCentroides[j]):
			achei=achei+1;

	ultimosCentroides=centroides #armazena o valoe do ultimo centroide

	for j in range (len(centroides)):
		for i in range(len(dados)):
			distancias[j].append(dist_euclidiana(centroides[j],  dados[i]))

	cluster = [[] for i in range(len(dados))]

	for i in range(len(dados)):
		if ((distancias[0][i]<distancias[1][i]) and (distancias[0][i]<distancias[2][i])):
			cluster[0].append(dados[i])
		elif ((distancias[1][i]<distancias[0][i]) and (distancias[1][i]<distancias[2][i])):
			cluster[1].append(dados[i])
		else:
			cluster[2].append(dados[i])

	for i in range(len(cluster)):
		fakePoint.append(calcularPontoMedio(cluster[i]))

	for j in range(len(fakePoint)):
		for i in range(len(dados)):
			temp = dist_euclidiana(fakePoint[j], dados[i])
			newDistancias[j].append(temp)
	#Achando os novos centroides
	#achar o menor valor de cada lista
	#newDistancia=[[dist ao ponto fake (1)],[dist ao ponto fake (2)],[dist ao ponto fake(3)]]
	for i in range(len(centroides)):
		index = comparaValores(newDistancias[i], min(newDistancias[i]))
		centroides[i] = dados[index]
	#acho o menor valor de cada lista e armazeno em uma lista vai vai conter os 3 menores valores
	#objetivo: comparar cada valor de menorValor[i] com os valores das 3 listas de newDistancia
	#para achar os novos valores de centroides:
	#para cada i faco ele receber o valor do dado no indice encontrado pela funcao comparaValores envio para a funcao comparaValores
	#a lista com as novas distancias e o menor valor que encontrei dessa lista para poder entao achar o indice desse menor valor.
	t=t+1

plot3d(dados, centroides)
print ("centroides finais: ", centroides, "quantas vezes rodei por aqui: ", contador)
