import numpy as np
import time

#lambda (x,y): x if x < y else y
  def vizinho(d,i,caminho,disponiveis):
    disponiveis.remove(i)
    if len(caminho)==len(d[0]): 
      return caminho
    else:
      minimo = -1
      ind = -1
      for j in disponiveis:
        if(j==disponiveis[0]):
          minimo = d[i-1][j-1]
          ind = j
        else:
          if d[i-1][j-1] < minimo:
            minimo = d[i-1][j-1]
            ind = j
    caminho.append(ind)
    caminho=vizinho(d,ind,caminho,disponiveis)
    return caminho
    
  def HVP(d,inicio,disponiveis): #d é a matriz , i é o inicio, var é a lista de variáveis
    ini = time.time()
    caminho = [inicio] #[1] , [1,2,3,4,5,6]
  
    caminho_final = vizinho(d,inicio,caminho,disponiveis)

    print('Solução: ',caminho_final)
    #return caminho_final
    print('Custo: ',f_obj(caminho_final,d))
    fim = time.time()
    print('Tempo total: ',fim-ini)
# disponiveis = [1,2,3,4,5,6]

def f_obj(solucao,d):
  soma=0
  for i in range(0,len(solucao)-1): 
    soma+=d[solucao[i]-1][solucao[i+1]-1]

  soma+=d[solucao[-1]-1][solucao[0]-1]
  return soma
