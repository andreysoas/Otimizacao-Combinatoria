import numpy as np
import numpy.random as rd
from math import floor
import time
from functools import reduce

"""HP() retorna o conjunto com a Heurística permutacional aplicada para cada sequência começada por um elemento i. Enquanto HP_() necessita de um parâmetro que informa qual será o início da sequência."""

def subviz(s):
  a=[]
  scopy2=np.array(s)
  a.append(scopy2)
  for i in range(1,len(s)-1):
    for j in range(i+1,len(s)):
      s[i],s[j]=s[j],s[i]
      a.append(s)
      s=np.copy(scopy2)
  return a

def espelhado(s):
  k = floor(len(s)/2)
  for i in range(1,k+1):
    s[i],s[len(s)-i] = s[len(s)-i],s[i]
    
def trocas(s):
  for i in range(1,len(s)-1,2):
    s[i],s[i+1]=s[i+1],s[i]


def HP(s):
  permutacoes=[]
  scopy = np.array(s)
  for i in range(0,len(s)):
    s=np.copy(scopy)
    s[0],s[i]=s[i],s[0]
    scopy2=np.copy(s)

    #Gerar as trocas dois a dois 
    permutacoes+=subviz(s)
    s=np.copy(scopy2)
    
    espelhado(s)
    permutacoes+=subviz(s)
    s=np.copy(scopy2)
    
    trocas(s)
    scopy3=np.copy(s)
    permutacoes+=subviz(s)
    s=np.copy(scopy3)

    espelhado(s)
    permutacoes+=subviz(s)
  
  return permutacoes


def HP_(s,i):
  permutacoes=[]
  s[0],s[i-1]=s[i-1],s[0]
  scopy2=np.copy(s)

  #-------------------------
  permutacoes+=subviz(s)
  s=np.copy(scopy2)
    
  espelhado(s)
  permutacoes+=subviz(s)
  s=np.copy(scopy2)
    
  trocas(s)
  scopy3=np.copy(s)
  permutacoes+=subviz(s)
  s=np.copy(scopy3)

  espelhado(s)
  permutacoes+=subviz(s)
  
  return permutacoes


def F_obj(permutacoes,d):
  n=len(d[0])
  solucoes = []
  for j,arr_j in enumerate(permutacoes):  # É usado len(permutacoes[0]) porq ainda n tenho o n da dimensão da matriz
    soma=0
    for i in range(0,n):  #0,1,2,3,4,5,6
      if i==n-1:
        soma+=d[arr_j[i]-1][arr_j[0]-1]
      else:
        soma+=d[arr_j[i]-1][arr_j[i+1]-1]
    solucoes.append((arr_j,soma))
    #print('Permutação: ',arr_j,' , Valor de função obj: ',soma)
  return solucoes

def optimal(solucoes):
  min = reduce(
      lambda minimo, atual: minimo if minimo[1] < atual[1] else atual,
      solucoes)
  return min

"""A entrada pra o programa tem de ser: A matriz **d** com distâncias nó-nó(i,j) e um vetor **S** que rótula os pontos mantendo a ordem apresentada na matriz. o "nó" de rótulo i precisa se referir à linha i-1 da matriz"""

def HP_controle(d,s,i):
  ini = time.time()
  permutacoes=np.array(HP_(s,i))
  solucoes = F_obj(permutacoes,d)
  min = optimal(solucoes)
  fim = time.time()
  print('Tempo total:',fim-ini)
  print('\nA solução ótima é:',min)

#Chamar HP_controle com matriz de distâncias,vetor s que rótula os pontos, e o rótulo de início
