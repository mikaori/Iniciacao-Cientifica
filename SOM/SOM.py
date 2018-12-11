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
import seaborn as sns

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

def calcularDistanciaGrade(pesos, linha, coluna, distancias, neuronio_x, neuronio_y):
	#calcula distancia entre vizinhos na seguinte sequencia: para o lado, para baixo

	#for i in range(len(pesos)):
	#	print(pesos[i])
	aux1 = 0

	for i in range (linha+linha-1):
		for j in range (coluna+coluna-1):
			if (i%2==0 and j%2==0):
				distancias.append(0)
			elif (i%2==0 and j%2==1):
				value = dist_euclidiana(pesos[aux1], pesos[aux1+1])
				distancias.append(value)
				aux1 = aux1 + 1
			elif (i%2==1 and j%2==0):
				distancias.append(dist_euclidiana(pesos[aux1], pesos[aux1-coluna]))
				aux1 = aux1 + 1
			else:
				distancias.append(0)

			if (j==coluna+coluna-2): # pq é o ultimo da linha então não terá vizinho para calcular
				au1x = aux1 + 1

			neuronio_x.append(i)
			neuronio_y.append(j)

	aux = 0
	for i in range (linha+linha-1):
		sum = 0 #calcula a media das distancias entre os grupos
		for j in range (coluna+coluna-1):
			if (i%2==1 and j%2==1):
				sum = distancias[aux]+distancias[aux+2]+distancias[aux+coluna-1]+distancias[aux+coluna+2]+distancias[aux+coluna+coluna-1]
				distancia[i][j].append(sum/4)
				aux = aux + 1
		if (i%2==0 and i!=0):
			aux = aux + coluna + 1 #acabou a linha

	'''for i in range(len(pesos)):
		if i%coluna==0: #se o elemento é ele mesmo
			distancias.append(0)
			neuronio_x.append(i%coluna)
			neuronio_y.append(i/2)
		if ((i+1)%coluna)!=0 and i+1<linha*coluna: #distancia para o ponto do lado - se o proximo nao for na linha de baixo ou se é menor que o total de neuronios
			#print(' pesos[i]', pesos[i],' pesos[i+1]) ', pesos[i+1])
			distancias.append(dist_euclidiana(pesos[i], pesos[i+1]))
			neuronio_x.append(i%coluna)
			neuronio_y.append((i+1)/3)
		if i+coluna<linha*coluna: #distancia para o ponto abaixo - só nao fará se o ponto estiver na ultima linha
			distancias.append(dist_euclidiana(pesos[i], pesos[i+coluna]))
			neuronio_x.append(i%coluna)
			neuronio_y.append((i+coluna)/3)'''
	#print ('distancia de casa ponto para os vizinhos: ', distancias)
	#print ('neuronio_x ', neuronio_x, 'neuronio_y ', neuronio_y)

	return distancias, neuronio_x, neuronio_y

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

def plotMatrizU(pesos, coluna, linha):
	distancias=[]
	neuronio_x=[]
	neuronio_y=[]

	distancias, neuronio_x, neuronio_y = calcularDistanciaGrade(pesos, coluna, linha, distancias, neuronio_x, neuronio_y)

	print('x: ',neuronio_x)
	print('y: ',neuronio_y)

	x = np.array(x)
	y = np.array(y)
	z = np.array(distancias)
	#print(neuronio_x, neuronio_y, distancias)
	df = pd.DataFrame.from_dict(np.array([x,y,z]).T)
	df.columns = ['neuronio_x','neuronio_y','distancia']
	df['distancia'] = pd.to_numeric(df['distancia'])

	pivotted= df.pivot('neuronio_y','neuronio_x','distancia')
	sns.heatmap(pivotted,cmap='RdBu')
	plt.show()

	print(neuronio_x, neuronio_y, distancias)

def main():
	dados = lerArquivo('dados1.csv')

	#linha = int(input('Sua matriz será? linha = '))
	linha = 3
	#coluna = int(input('coluna = '))
	coluna = 3

	grade = gerar_grade(linha, coluna)
	init_grade(linha, coluna, grade)

	pesos = init_pesos(linha, coluna, dados)
	print ("pesos: ", pesos)

	interacoes = int(input('numero de interacoes = '))
	#print ("dados: ", dados)

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

	plot3d(pesos, dados)
	plotMatrizU(pesos, coluna, linha)

main()
