import csv
import numpy as np
import random as r
import math
from matplotlib import pyplot as plt

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

def gerar_matriz (linhas, colunas, dados):
	matriz= [[] for i in range(linhas)]
	for j in range(linhas):
		matriz[j]=r.sample(dados,colunas)
	matriz = list(map(pontoStringFloat,dados))
	return (matriz)

def dist_euclidiana (ponto1,ponto2):
	dim, soma = len(ponto1), 0
	for i in range(dim):
		soma += math.pow(ponto1[i] - ponto2[i], 2)
	return math.sqrt(soma)

def comparaValores(lista, valor):
	index = 0;
	for i in range(len(lista)):
		if lista[i] == valor:
			index=i
	return index

def d_largura(largura_inicial, i, cte_tempo):
	return largura_inicial * np.exp(-i / cte_tempo)

def d_taxa_aprendizado(taxa_aprendizado_inicial, i, interacoes):
	return taxa_aprendizado_inicial * np.exp(-i / interacoes)

def att_vizinhanca(distancia, largura): #o quanto cada neuronio sofrerá com o reajuste dos pesos
	return np.exp(-(distancia**2) / (2* (largura**2)))

def AcharMatch(peso, x): #busca neuronio vencedor
	distancia = []
	for i in range(len(peso)):
		distancia.append(dist_euclidiana(peso[i],x)) #adiciona a distancia entre cada peso e dado
	index= comparaValores(distancia, min(distancia)) #O menor valor de totdist será o neuronio vencedor
	return peso[index]

def init_largura(pesos): #como achar a largura da grade? li que era o "raio"
	sum_peso=[]
	for i in range(len(pesos)):
		sum_peso.append(sum(pesos[i]))
	index =comparaValores(sum_peso, max(sum_peso)) #maior ponto mais distante
	maior_valor= pesos[index]
	index =comparaValores(sum_peso, min(sum_peso)) #menor ponto mais distante
	menor_valor= pesos[index]
	largura = (dist_euclidiana(maior_valor,menor_valor))/2
	return (dist_euclidiana(maior_valor,menor_valor))/2

arquivo = 'dadosteste.csv'

dados = lerArquivo(arquivo)
#linha = int(input('Sua matriz será? linha = '))
linha=3
#coluna = int(input('coluna = '))
coluna =3
pesos = gerar_matriz(linha,coluna,dados)
interacoes = int(input('numero de interacoes = '))
taxa_aprendizagem_inicial = 0.01
largura_inicial = init_largura(pesos)
taxa_aprendizagem = taxa_aprendizagem_inicial
largura = largura_inicial
contador =0

#ULTIMO VALOR SEMPRE TA DANDO 0 DE CADA PONTO WHY
for j in range(interacoes):

	if j==0 or j%len(dados)==1:
		dadosSortidos=dados
		r.shuffle(dadosSortidos)

	#inicializando valores iniciais
	for i in range(len(dados)):
		neuronio_vencedor = AcharMatch (pesos,dadosSortidos[i%len(dados)])
		print ("neuronio_vencedor: ",neuronio_vencedor)

		#CALCULANDO DISTANCIA LATERAL - dist do neuronio_vencedor para os outros
		for valor in range(len(pesos)):
			print("pesos ",pesos[valor],"neuronio_vencedor: ", neuronio_vencedor)
			valor_distancia = dist_euclidiana(neuronio_vencedor, pesos[valor])
			if valor_distancia >=0.00001:
				#ATUALIZANDO A VIZINHANCA
				if valor_distancia<=largura:
					influencia = att_vizinhanca(valor_distancia,largura)
					for n in range(3): #quero o numero de colunas de um ponto
						w = pesos[valor]
						print("w = ", w)
						pesos[valor][n] = w[n]+(taxa_aprendizagem*influencia*(dadosSortidos[i%len(dados)][n]-w[n]))
						print("novos pesos: ", pesos[i])

		#ATUALIZANDO TAXA DE APRENDIZAGEM
		taxa_aprendizagem = d_taxa_aprendizado(taxa_aprendizagem_inicial,i,interacoes)

		#ATUALIZANDO LARGURA
		largura = d_largura(largura_inicial, i, interacoes)

print ("pesos: ", pesos)
