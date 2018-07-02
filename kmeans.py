#coding:utf-8
import numpy as np
import pandas as pd
import random as r
from matplotlib import pyplot as plt

def insertionSort(v):
    i = 1 #elemento atual
    while i < len(v):
        temp = v(i) #variavel temporario para armazenamento
        trocou = False
        j = i-1 #com quem quero comparar o i - elemento antecessor
        while j>=0 and v[j]>temp:
            v[j+1] = v[j]
            trocou = True
            j-=1
        if trocou:
            v[j+1] = temp
        i+=1
    return v[0]

def SorteiaPontos():
    ponto = r.shuffle(lista)

def lerTxt():
    f = open(os.path.expanduser("dados1.txt"))
    lines = f.readlines()

    for line in list:
        x.append(line.split()[0])
        y.append(line.split()[1])
        z.append(line.split()[2])
    f.close()
    print(x,y,z)

    plt.plot(x,y,z)
    plt.show()

def distEuclidiana(a, b):
    return(sqrt((a[1]-b[1])**2)+(a[2]-b[2])+a[3]-b[3])

def main():
    k=3
    centroids=[SorteiaPontos(), SorteiaPontos(), SorteiaPontos()]

    #plotar os centroids
    fig = plt.figure(figsize=(5,5))
    plt.scatter(f['x'], f['y'], f['z'], color='k')
    colmap ={1: 'r', 2: 'g', 3'b'}
    for i in centroids.keys():
        plt.scatter(*centroids[i], color=colmap[i])
    plt.show();

def atribuicao():
    clusters = [cluster1,cluster2,cluster3]

    distCentroid1 = []
    distCentroid2 = []
    distCentroid3 = []
    distancias = [distCentroid1, distCentroid2, distCentroid3]
    i = 0
    for i<len(distancias):
        for i<len(lista):
            for i<len(centroids):
                if (centroids(i)!=lista(i)):
                    distancias(i) = distEuclidiana(centroids(i), lista(i))
                i+=1
            i+=1
        i+=1

    for i<len(lista):
        for i<len(centroids):
            if (centroids(i)!=lista(i)):
