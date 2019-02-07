# coding: utf-8
# Módulo 1 - Coletando e Armazenando dados históricos do mercado

"""
Deve ler o arquivo de dados de mercado, caso exista, ou criá-lo a partir de dados da corretora, respeitando os 
parâmetros do arquivo de parâmetros.
"""

import sys
import os

sys.path.append(os.getcwd().split(sep="modules")[0])
import modules
from modules import func

from datetime import datetime
from datetime import date
import pandas as pd

def prod (param):
    """
    Retorna o framework de trabalho, 'dados', bem como uma variável de controle ('time_aq_comp') a fim de startar 
    ou não a estratégia do módulo seguinte.
    """
    
    par = param[1].split()[2]; candle = param[0].split()[2];  time_aq = param[12].split('=')[1][1:]; datapath = str(param[4].split()[2]).format(par,candle); data_name = 'dados.csv'
    candle_ent = '{}m'.format(candle)

    try:
        dados = pd.read_csv(datapath+data_name, index_col='Open_time', parse_dates=['Open_time','Close_time'], infer_datetime_format=True)        

        print('dados lidos') #TESTE, APAGAR DEPOIS DE OK
        
        dif_minut = abs(float(((datetime.now() - dados.Close_time[len(dados)-1]).total_seconds() - 1)/60)) #Tirando 1s fica ok

        if (dif_minut > float(candle)): 
            
            time_aq = '{} minute ago UTC'.format(int(dif_minut) + int(candle))
            time_aq_comp = '{} minute ago UTC'.format(int(dif_minut)) #Necessário apenas para msg de controle
            
            #Faz a solicitação do complemento do dado
            hist_complem = func.data_historico(par, candle_ent, time_aq)
            
            #Junta os dataframes
            dados = dados.append(hist_complem) 
            
            #Despreza a última amostra caso o fechamento do último candle seja maior que o presente
            if ( dados.Close_time[len(dados)-1] > datetime.now() ): dados = dados.iloc[:len(dados)-1] 
    
            mess = 'Foi preciso completar o dado em {}'.format(time_aq_comp) #TESTE, APAGAR DEPOIS DE OK
            print(mess) #TESTE, APAGAR DEPOIS DE OK
            
        #Não foi preciso completar o dado, pois o candle fechado já foi analisado.
        else:
            time_aq = 'bypass'
            print('Não foi preciso completar o dado, pois o último candle fechado já foi analisado.') #TESTE, APAGAR DEPOIS DE OK
    
    #NÃO Encontra o arquivo dados.csv na pasta, ENTÃO Cria o arquivo até o instante atual.
    except:
        mess = 'Arquivo não encontrado, criando arquivo de dados.' #TESTE, APAGAR DEPOIS DE OK
        print(mess) #TESTE, APAGAR DEPOIS DE OK
        
        dados = func.data_historico(par, candle_ent, time_aq)
        
        #Despreza a última amostra caso o fechamento do último candle seja maior que o presente
        if ( dados.Close_time[len(dados)-1] > datetime.now() ): dados = dados.iloc[:len(dados)-1]
        
    #Salva os dados históricos
    dados.to_csv(datapath+data_name, index=True, index_label='Open_time', date_format='%Y-%m-%d %H:%M:%S') 

    return dados, time_aq