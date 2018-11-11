# -*- coding: utf-8 -*-
import csv
import numpy as np
import math
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt

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

def calcularPontoMedio(lista, colunas):
	somaColunas,pontoMedio=[], []
	tam=len(lista)
	for i in range(colunas):
		somaColunas=sumColumn(lista)
		pontoMedio.append(somaColunas[i]/tam)
	return(pontoMedio)

def pontoStringFloat (lista):
	return list(map(float, lista))

def comparaValores(lista, valor):
	index = 0;
	for i in range(len(lista)):
		if lista[i] == valor:
			index=i
	return index

def lerArquivo(arquivo):
	with open(arquivo, 'r') as arquivo:
		leitor = csv.reader(arquivo, delimiter=',')
		dados = []
		for ponto in leitor:
			dados.append(ponto)
		dados = dados[1:]
		dados = list(map(pontoStringFloat, dados))
	return dados

def plot3d(dados, pesos):
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	dados = pd.DataFrame(dados, columns=["x","y","z"])
	pesos = pd.DataFrame(pesos, columns=["x","y","z"])
	ax.scatter(pesos.x, pesos.y, pesos.z)
	ax.scatter(dados.x, dados.y, dados.z, c='r', marker='d')
	plt.show()

def main():
	dados = lerArquivo('dadosteste.csv')
	n = int(input('Qual o numero de centroides? '))
	centroides = dados[0:n]
	t, match = 0, 0
	ultimosCentroides = centroides.copy()
	n_colunas=len(dados[0])

	while (t < 100 and match!=1):
		distancias = [[] for i in range(len(centroides))]
		newDistancias=[[] for i in range(len(centroides))]
		cluster1,cluster2,cluster3,fakePoint=[],[],[],[]
		contador = 0

		#print('centroides: ', centroides)
		#print('ultimosCentroides', ultimosCentroides)
		for j in range (len(centroides)):
			if (centroides[j] == ultimosCentroides[j]):
				contador=contador+1
				print('centroides[j]', centroides[j],'ultimosCentroides', ultimosCentroides[j],'contador', contador)

		if contador==len(centroides):
			match=1
			print(match)

		ultimosCentroides=centroides.copy() #armazena o valor do ultimo centroide
		print('ultimosCentroides: ',ultimosCentroides)
		for j in range (len(centroides)):
			for i in range(len(dados)):
				distancias[j].append(dist_euclidiana(centroides[j],  dados[i]))

		#print ('distancias: ', distancias)

		cluster = [[] for i in range(len(centroides))] #inicializando os clusters

		for i in range(len(dados)):
			for j in range(len(centroides)):
				if j==0 or distancias[j][i]<menor:
					menor = distancias[j][i]
					n_centroide=j #pega em qual centroide está
			cluster[n_centroide].append(dados[i])

		print('\ncluster: ', cluster)

		for i in range(len(centroides)):
			fakePoint.append(calcularPontoMedio(cluster[i], n_colunas))

		#print('\nfakePoint: ', fakePoint)

		for j in range(len(fakePoint)):
			for i in range(len(dados)):
				#newDistancia=[[dist ao ponto fake (1)],[dist ao ponto fake (2)],[dist ao ponto fake(3)]]
				newDistancias[j].append(dist_euclidiana(fakePoint[j], dados[i]))

		#print('\nnewDistancias', newDistancias)

		#para achar os novos valores de centroides:
		for i in range(len(centroides)):
			centroides[i] = dados[comparaValores(newDistancias[i], min(newDistancias[i]))]
			print(centroides[i])
		#para cada i faco ele receber o valor do dado no indice encontrado pela funcao comparaValores envio para a funcao comparaValores
		#a lista com as novas distancias e o menor valor que encontrei dessa lista para poder entao achar o indice desse menor valor.

		t=t+1

	print ("\ncentroides finais: ", centroides, "quantas vezes rodei por aqui: ", t)

	plot3d(centroides, dados)

main()
