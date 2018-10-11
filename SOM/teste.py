# -*- coding: utf-8 -*-
import csv
import random as r
import math
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
from pandas.plotting import scatter_matrix

def gerar_grade (linhas, colunas):
	#gero uma matriz (lista de listas)
	matriz = []

	for i in range (linhas):
		matriz.append([] for j in range(colunas))

	print(matriz)
	return matriz

def init_grade(linhas, colunas, matriz):
	dist_vizinho = 1

	#ordem vizinho a direita e segue sentido horario
	for i in range(linhas):
		for k in range(colunas):
			#vizinhos a direita
			if k < (colunas-1):
				matriz[i][k].append(dist_vizinho)
			if k == colunas:
				matriz[i][k].append(0)
			#vizinhos abaixo
			if i == linha:
				matriz[i][k].append(0)
			else:
				matriz[i][k].append(dist_vizinho)
			#vizinhos a esquerda
			if k == 1:
				matriz[i][k].append(0)
			else:
				matriz[i][k].append(dist_vizinho)
			#vizinhos acima
			if i == 1:
				matriz[i][k].append(0)
			else:
				matriz[i][k].append(dist_vizinho)

	return (matriz)

linhas = 3
colunas = 3

grade = gerar_grade(linhas, colunas)
print(grade)
init_grade(linhas, colunas, grade)
