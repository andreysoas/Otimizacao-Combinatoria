# -*- coding: utf-8 -*-
"""FSP via HPk.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i3_Kzm_DxJjri1b8BERRC2P-AFxUtfk1
"""

import numpy as np
from math import floor
import math
import functools
import itertools

def convert_arq(path:str)->list:
  matriz = []
  ant =''
  with open(path,'r') as arqv:
    num=0
    for i in arqv:
      line = []
      for j in i:
        if (j=='\n' or j==' ') and ant!=' ':
          ant = j
          line.append(num)
          num=0
        elif '0'<=j<='9':
          ant = j
          num = num*10 + int(j)
      matriz.append(line)
  arqv.close()

  Matriz = []

  for i in matriz:
    new_lines = []
    for j in range(0,len(i)):
      if j%2 != 0:
        new_lines.append(i[j])
    Matriz.append(new_lines)

  return Matriz

def espelhado(s):
  k = floor(len(s)/2)
  for i in range(1,k+1):
    s[i],s[len(s)-i] = s[len(s)-i],s[i]
    
def trocas(s):
  for i in range(1,len(s)-1,2):
    s[i],s[i+1]=s[i+1],s[i]

######################################
def HP_k(seq:list, k:int):
  
  tam = len(seq)-1
  r = (len(seq)-1)%k #tamanho do último grupo
  numRestantes = tam-r

  countGroups = k-1
  count = 0
  seqs = []
  miniSeq = []
  listRetorno = []

  tamGrupo = int(numRestantes/countGroups)
  for i in range(1,tam-r+1):
    count+=1
    miniSeq.append(seq[i])

    if count == tamGrupo:
      seqs.append(miniSeq)
      countGroups = countGroups-1
      numRestantes = numRestantes - tamGrupo
      if countGroups != 0:
        tamGrupo = int(numRestantes/countGroups)
      else:
        seqs.append(list(seq[-r:]))
      miniSeq = []
      count=0
  
  Lista = list(itertools.permutations(seqs))
  for i in Lista:
    permutation = [seq[0]]
    for j in i:
      permutation+=j
    listRetorno.append(permutation)

  return listRetorno

###################################################

def HPk(s,k):
  permutacoes=[]
  scopy = np.array(s)
  for i in range(0,len(s)):
    s=np.copy(scopy)
    s[0],s[i]=s[i],s[0]
    scopy2=np.copy(s)

    permutacoes.append(s)
    s=np.copy(scopy2)
    
    espelhado(s)
    permutacoes.append(s)

    s=np.copy(scopy2)
    
    trocas(s)
    permutacoes.append(s)

    scopy3=np.copy(s)
    s=np.copy(scopy3)

    espelhado(s)
    permutacoes.append(s)
  
  fromHP_k = []
  for i in permutacoes:
    fromHPk = HP_k(i,k)
    for j in fromHPk:
      fromHP_k.append(j)  

  return fromHP_k

def makesPan(seq:list,M):
  m = len(M)
  antSeq = np.zeros(m)
  newSeq = np.zeros(m)

  for j in seq: # j = 1,2,3,4 ...
    for i in range(m):

      if i == 0:
        newSeq[0] = antSeq[0] + M[i][j-1]

      else:
        if newSeq[i-1] > antSeq[i]:
          newSeq[i] = newSeq[i-1] + M[i][j-1]
        else:
          newSeq[i] = antSeq[i] + M[i][j-1]
    
    antSeq = newSeq
    #print(antSeq)

  return antSeq[-1]

def defineOtimo(S:list,M:list):
  listMakespans = []
  min = 0

  for i in range(len(S)):
    atual = makesPan(S[i],M)
    solucao = list(S[i])

    if i == 0:
      min = atual
      listMakespans.append(solucao)
    
    else:
      if atual < min:
        listMakespans.clear()
        listMakespans.append(solucao)
        min = atual
      
      elif atual == min:
        if solucao not in listMakespans:
          listMakespans.append(solucao)

  print('\nSolução: ',listMakespans,end='\n')
  print('Mínimo: ',min)

def interfaceProgram():
  path = input('Path: ')
  if path == 'end':
    return True

  M = np.array(convert_arq(path))
  M = M.transpose()
  print("Matriz(tempo na máquina / tarefa): ")
  for i in M:
    print(i,end='\n')

  tarefas = list(np.arange(1,len(M[0])+1))
  print("Tarefas: ",tarefas)

  K = int(input('K: '))

  lista = HPk(tarefas,K)
  #lista = HP(tarefas)
  print('quantidade de soluções: ',len(lista))

  defineOtimo(lista,M)
  print('\n')

while True:
  if interfaceProgram():
    print('\nTERMINANDO...',end='\n')
    break