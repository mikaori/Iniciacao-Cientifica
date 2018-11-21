# -*- coding: utf-8 -*-
import csv
import random as r
import math
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
from pandas.plotting import scatter_matrix
import copy


def lerArquivo(arquivo):
	with open(arquivo, 'r') as arquivo:
		leitor = csv.reader(arquivo, delimiter=',')
		dados = []
		for ponto in leitor:
			dados.append(ponto)
		dados = dados[1:]
		dados = list(map(pontoStringFloat, dados))
	return dados

def pontoStringFloat (lista):
	return list(map(float, lista))

def gerar_grade (linhas, colunas):
	#gero uma matriz (lista de listas)
	matriz = []

	for i in range (linhas):
		for j in range (colunas):
			neuronio = []
			matriz.append(neuronio)
	return matriz

def init_pesos(linhas, colunas, dados):
	matriz= [[] for i in range(linhas)]
	aux = copy.deepcopy(dados)
	matriz=r.sample(aux, linhas*colunas)
	return matriz

def init_grade(linhas, colunas, matriz):
	contador = 0
	for j in range (linhas):
		for k in range (colunas):
			px=j
			py=k

			#print('px',j,'py',k)
			#calculando a distancia do ponto da matriz para o restante
			for x in range (linhas):
				for y in range (colunas):
					distManhattan=abs(px-x)+abs(py-y)
					matriz[contador].append(distManhattan)
			contador=contador+1
			#print(matriz)

	return (matriz)

def dist_euclidiana (ponto1, ponto2):
	dimensao, soma = len(ponto1), 0
	for i in range(dimensao):
		soma += math.pow(ponto1[i] - ponto2[i], 2)
	return math.sqrt(soma)

def comparaValores(lista, valor):
	index = 0;
	for i in range(len(lista)):
		if lista[i] == valor:
			index=i
	return index

def d_largura(largura_inicial, i, cte_tempo):
	return largura_inicial * math.exp(-i / cte_tempo)

def d_taxa_aprendizado(taxa_aprendizado_inicial, i, interacoes):
	return taxa_aprendizado_inicial * math.exp(-i / interacoes)

def att_vizinhanca(distancia, largura): #o quanto cada neuronio sofrerá com o reajuste dos pesos
	return math.exp(-(distancia**2) / (2* (largura**2)))

def AcharMatch(peso, x): #busca neuronio vencedor
	distancia = []
	for i in range(len(peso)):
		distancia.append(dist_euclidiana(peso[i], x)) #adiciona a distancia entre cada peso e dado
	index= comparaValores(distancia, min(distancia)) #O menor valor de totdist será o neuronio vencedor
	return peso[index]

def init_largura(pesos): #como achar a largura da grade? li que era o "raio"
	sum_peso = []
	for i in range(len(pesos)):
		sum_peso.append(sum(pesos[i]))
	index = comparaValores(sum_peso, max(sum_peso)) #maior ponto mais distante
	maior_valor = pesos[index]
	index = comparaValores(sum_peso, min(sum_peso)) #menor ponto mais distante
	menor_valor = pesos[index]
	largura = (dist_euclidiana(maior_valor, menor_valor))/2
	return (dist_euclidiana(maior_valor, menor_valor))/2

def plot3d(dados, pesos):
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	dados = pd.DataFrame(dados, columns=["x", "y", "z"])
	pesos = pd.DataFrame(pesos, columns=["x", "y", "z"])
	ax.scatter(pesos.x, pesos.y, pesos.z)
	ax.scatter(dados.x, dados.y, dados.z, c='r', marker='d')
	plt.show()

def plotMatrizU(pesos, n_colunas):
	dist_matriz=[]
	neuronio=[]
	neuronio_comp=[]


	dist_matriz.append(dist_euclidiana(pesos[0], pesos[0]))
	neuronio.append(0)
	neuronio_comp.append(0)
	dist_matriz.append(dist_euclidiana(pesos[0], pesos[1]))
	neuronio.append(0)
	neuronio_comp.append(1)
	dist_matriz.append(dist_euclidiana(pesos[1], pesos[2]))
	neuronio.append(1)
	neuronio_comp.append(2)

	dist_matriz.append(dist_euclidiana(pesos[0], pesos[3]))
	neuronio.append(0)
	neuronio_comp.append(4)
	dist_matriz.append(dist_euclidiana(pesos[1], pesos[4]))
	neuronio.append(1)
	neuronio_comp.append(4)
	dist_matriz.append(dist_euclidiana(pesos[2], pesos[5]))
	neuronio.append(2)
	neuronio_comp.append(5)

	dist_matriz.append(dist_euclidiana(pesos[3], pesos[3]))
	neuronio.append(3)
	neuronio_comp.append(3)
	dist_matriz.append(dist_euclidiana(pesos[3], pesos[4]))
	neuronio.append(3)
	neuronio_comp.append(4)
	dist_matriz.append(dist_euclidiana(pesos[4], pesos[5]))
	neuronio.append(4)
	neuronio_comp.append(5)

	dist_matriz.append(dist_euclidiana(pesos[3], pesos[6]))
	neuronio.append(3)
	neuronio_comp.append(6)
	dist_matriz.append(dist_euclidiana(pesos[4], pesos[7]))
	neuronio.append(4)
	neuronio_comp.append(7)
	dist_matriz.append(dist_euclidiana(pesos[5], pesos[8]))
	neuronio.append(6)
	neuronio_comp.append(8)

	dist_matriz.append(dist_euclidiana(pesos[6], pesos[6]))
	neuronio.append(6)
	neuronio_comp.append(6)
	dist_matriz.append(dist_euclidiana(pesos[6], pesos[7]))
	neuronio.append(6)
	neuronio_comp.append(7)
	dist_matriz.append(dist_euclidiana(pesos[7], pesos[8]))
	neuronio.append(7)
	neuronio_comp.append(8)

	df = pd.DataFrame({'neuronio': neuronio, 'neuronio comparado': neuronio_comp, 'distancia': dist_matriz})
	ax = df.plot.hexbin(x='neuronio', y='neuronio comparado', C='distancia', gridsize=10, cmap="viridis")
	plt.show()

def main():
	dados = lerArquivo('dadosteste.csv')

	#linha = int(input('Sua matriz será? linha = '))
	linha = 3
	#coluna = int(input('coluna = '))
	coluna = 3

	grade = gerar_grade(linha, coluna)
	init_grade(linha, coluna, grade)

	pesos = init_pesos(linha, coluna, dados)
	print ("pesos: ", pesos)

	interacoes = int(input('numero de interacoes = '))
	print ("dados: ", dados)

	taxa_aprendizagem_inicial = 0.01
	largura_inicial = init_largura(pesos) #A LARGURA AINDA É CONFORME OS VALORES DOS PESOS?
	taxa_aprendizagem = taxa_aprendizagem_inicial
	largura = largura_inicial
	contador = 0
	n_colunas = len(dados[0])
	index=0

	for j in range(interacoes):

		if j==0 or j%len(dados)==1:
			dadosSortidos = copy.deepcopy(dados)
			r.shuffle(dadosSortidos)

		#inicializando valores iniciais
		for i in range(len(dados)):
			neuronio_vencedor = AcharMatch (pesos, dadosSortidos[i%len(dados)])
			#print ("neuronio_vencedor: ", neuronio_vencedor)
			#print ("index: ",index)
			#CALCULANDO DISTANCIA LATERAL - dist do neuronio_vencedor para os outros
			for valor in range(len(pesos)):
				#print("pesos ", pesos[valor], "neuronio_vencedor: ", neuronio_vencedor)
				valor_distancia = dist_euclidiana(neuronio_vencedor, pesos[valor])
				#print("\n 2 dados: ", dados, " pesos: ", pesos)
				if valor_distancia >= 0.00001:
					#ATUALIZANDO sA VIZINHANCA
					if valor_distancia <= largura:
						#print("d_quadrado[valor] = ")
						dist_grade_neuronio = copy.deepcopy(grade[valor])
						influencia = att_vizinhanca(dist_grade_neuronio[valor], largura)
						#achar o index na lista d_quadrado q representa o ponto na list
						for n in range(n_colunas): #quero o numero de colunas de um ponto
							w = pesos[valor]
							#print("w = ", w)
							pesos[valor][n] = w[n]+(taxa_aprendizagem*influencia*(dadosSortidos[i%len(dados)][n]-w[n]))
							#print("novos pesos: ", pesos[i])

				#print("\n 3 dados: ", dados, " pesos: ", pesos)
			#ATUALIZANDO TAXA DE APRENDIZAGEM
			taxa_aprendizagem = d_taxa_aprendizado(taxa_aprendizagem_inicial, i, interacoes)
			#print("taxa aprendizagem: ",taxa_aprendizagem)

			#ATUALIZANDO LARGURA
			largura = d_largura(largura_inicial, i, interacoes)
			#print("largura: ", largura)
			#print(dados)

	#print ('pesos: ', pesos)

	#plot3d(pesos, dados)
	plotMatrizU(pesos, n_colunas)

main()
