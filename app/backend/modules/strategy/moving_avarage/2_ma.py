# coding: utf-8

#Módulo 2 - Estratégia: Cruzamento das médias móveis

"""
A partir dos dados de mercado e dos parâmetros, emite um sinal de compra/venda. Quando a média móvel curta está 
acima da média móvel longa, via de regra, há uma tendência de subida, por isso deve-se posicionar comprado, do 
contrário, posiciona-se vendido. Por isso o sinal é emitido quando há cruzamento das médias.

Retorna, além do sinal (ordem) os valores das últimas médias móveis, a fim de adicioná-los no arquivo de log.

"""

import pandas as pd

def prod(dados,param):
    
    #1 - PARÂMETROS
    ordem = 'keep'; mmc_atual = 0.0; mml_atual = 0.0 
    medlonga = int(param[3].split()[2]); medcurta = int(param[2].split()[2])
    
    #2 - Reduzindo o tamanho do dado de trabalho
    dados = dados.iloc[-(medlonga + 10):] #Pouco maior que o tamanho da média móvel longa
        
    #3 - Cálculo das médias móveis
        
        #3.1 - Atuais
    mmc_atual = dados['Close'].rolling(window=medcurta).mean()[len(dados)-1] #Curta
    mml_atual = dados['Close'].rolling(window=medlonga).mean()[len(dados)-1] #Longa
    
        #3.2 - Imediatamente anteriores
    mmc_anterior = dados['Close'].rolling(window=medcurta).mean()[len(dados)-2] #Curta
    mml_anterior = dados['Close'].rolling(window=medlonga).mean()[len(dados)-2] #Longa
    
    if mmc_atual > mml_atual and mmc_anterior <= mml_anterior: #Média curta cruzou para cima
        ordem = 'buy'
    if mmc_atual <= mml_atual and mmc_anterior > mml_anterior: #Média curta cruzou para baixo
        ordem = 'sell'
   
    return ordem,mmc_atual,mml_atual
