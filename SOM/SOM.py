import csv
import numpy as np
import random as r
import math
from matplotlib import pyplot as plt

def lerArquivo(arquivo):
	with open('dadosteste.csv', 'r') as arquivo:
		leitor = csv.reader(arquivo, delimiter=',')
		dados = []
		for ponto in leitor:
			dados.append(ponto)
		dados = dados[1:]
		dados = list(map(pontoStringFloat, dados))
	return dados

def dist_euclidiana (ponto1,ponto2):
	dim, soma = len(ponto1), 0 #len retorna o número de caracteres de uma string
	for i in range(dim):
		soma += math.pow(ponto1[i] - ponto2[i], 2)
	return math.sqrt(soma)

def gerar_matriz (n_linhas, n_colunas):
	return [[" "]*n_colunas for _ in range(n_linhas)]

def decay_radius(initial_radius, i, time_constant):
	return initial_radius * np.exp(-i / time_constant)

def decay_learning_rate(initial_learning_rate, i, n_iterations):
	return initial_learning_rate * np.exp(-i / n_iterations)

def calculate_influence(distance, radius):
	return np.exp(-distance / (2* (radius**2)))

def AcharMatch(peso, dados):

#inicializações
pesos = gerar_matriz
n = int(input('Sua matriz será? n = '))
m = int(input('m = '))
interacaoes = int (input('Numero de interações: '))
dados = lerArquivo('dadosteste.csv')
vizinhanca = float(input ('Parâmetro de vizinhança: '))
aprendizado = float (input('Taxa de aprendizado: '))

for i in range(interacoes):
	for j in range(len(dados)):


#inicializar os pesos, parametros de vizinhanca e os parametros de taxa de aprendizagem
#enquando cond de fim é falsa, faca
    #para cada vetor de entrada X, faca
        #para cada j, calcule funcao discriminante
        #encontra indice J tal que D(J) é min
        #para todas unidades j em uma vizinhanca especifica do J, e para todos i:
        #w(new)=w(old)+a[x-w(old)]
    #atualiza a taxa de aprendizagem
    #reduz regiao de vizinhana no tempo especifico
    #testa a conficao de fim
