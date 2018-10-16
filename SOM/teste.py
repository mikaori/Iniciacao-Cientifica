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
		for j in range (colunas):
			neuronio = []
			matriz.append(neuronio)
	return matriz

def init_grade(linhas, colunas, matriz):
	#percorrendo a matriz
	for i in range (linhas*colunas):
		#pegando um ponto da matriz
		for j in range (linhas):
			for k in range (colunas):
				px=j
				py=k

				if j==1 and k==1:
					px=1
					py=1

				#calculando a distancia do ponto da matriz para o restante
				for j in range (linhas):
					for k in range (colunas):
						distManhattan=abs(px-j)+abs(py-k)
						matriz[i].append(distManhattan)
				print(matriz)
				print('FINALIZEI DISTANCIA MANHATTAN')
	print(matriz)

	return (matriz)

linhas = 3
colunas = 3

grade = gerar_grade(linhas, colunas)
print(grade)
init_grade(linhas, colunas, grade)
