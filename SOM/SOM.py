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
