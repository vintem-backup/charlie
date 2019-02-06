
# coding: utf-8

# PROGRAMA PRINCIPAL

# In[1]:


#Bibliotecas e módulos

import sys
import os
from datetime import datetime
from datetime import date
import time

import modules
from modules import func
from modules import coleta
from modules import estrategia
from modules import acao
from modules import log
from modules import notifica_ciclo


# In[2]:


#Procura os diretórios de dados e log, se não existirem, cria-os.

param = open('parameters.txt').readlines(); par = param[1].split()[2]

par = param[1].split()[2]; candle = param[0].split()[2]; medcurta = int(param[2].split()[2])
medlonga = int(param[3].split()[2])

datapath = str(param[4].split()[2]).format(par,candle); data_name = 'dados.csv'

logpath = str(param[6].split()[2]).format(par,candle)

log_name = '{}m_{}x{}-log.csv'.format(candle,medcurta,medlonga)

if not os.path.exists(datapath): os.makedirs(datapath)

if not os.path.exists(logpath):os.makedirs(logpath)


# In[ ]:


#Programa propriamente dito

i=0; mmc = 0.0; mml = 0.0
notificacao = datetime.now()
inicio = datetime.now()
mess = 'PAR {}: (Re)Início de Ciclos'.format(par)
func.adriano('controle',mess)

while True:
    print('cilco {}:'.format(i)) #TESTE, APAGAR DEPOIS DE OK
    print(' ') #TESTE, APAGAR DEPOIS DE OK
    
    #Coleta de dados
    dados,tempo = coleta.prod(param)
    
    #Se atualizou o arquivo de dados, testa a estratégia
    if (tempo != 'bypass'):
        ordem,mmc,mml = estrategia.prod(dados,param)
        print(' ') #TESTE, APAGAR DEPOIS DE OK

        mess = 'Ordem = {}, MMC = {}, MML = {}'.format(ordem,mmc,mml) #TESTE, APAGAR DEPOIS DE OK
        print(mess) #TESTE, APAGAR DEPOIS DE OK
        print(' ') #TESTE, APAGAR DEPOIS DE OK

        instante,ativo,base,taxa,preco_inst,preco_mov = acao.prod(param,ordem)
        print(' ') #TESTE, APAGAR DEPOIS DE OK
        
        mess = 'instante = {},ativo = {},base = {},taxa = {},preco_inst = {},preco_mov = {}.'.format(instante,ativo,base,taxa,preco_inst,preco_mov)  #TESTE, APAGAR DEPOIS DE OK
        print(mess) #TESTE, APAGAR DEPOIS DE OK
        print(' ') #TESTE, APAGAR DEPOIS DE OK

        log_df = log.prod(param,ordem,mmc,mml,instante,ativo,base,taxa,preco_inst,preco_mov)
        
    notificacao = notifica_ciclo.prod(i, inicio, param, mmc, mml, notificacao)
    
    i+=1
    
    #Calcula o tempo de descanso
    dif_minut = abs(float(((datetime.now() - dados.Close_time[len(dados)-1]).total_seconds() - 1)/60))
    descanso = int( abs((float(candle) - float(dif_minut))*60) ) 
    
    #Testes
    print (' ')
    print(dados.Close_time[-5:])
    print (' ')
    print ('agora = ',datetime.now())
    
    print(' ') #TESTE, APAGAR DEPOIS DE OK
    print('Time sleep de {} seg'.format(descanso))
    
    time.sleep(descanso)