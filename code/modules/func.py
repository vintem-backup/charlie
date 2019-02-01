# coding: utf-8

"""
Módulo da coleção de funções criadas no projeto. 
Ao adicionar uma nova função a este módulo, também importar as biliotecas, caso o compilador acuse falta das mesmas, 
para o espaço indicado.
"""

#BIBLIOTECAS 

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from binance.client import Client
from datetime import datetime
from datetime import date
from binance.exceptions import BinanceAPIException
#import calendar
import telegram # Importa bibliotecas do Adriano
from telegram.ext import Updater, CommandHandler  #Importa bibliotecas do Adriano
import time

#Valida credenciais de API da binance ----------------------

api_path = os.getcwd().split(sep="modules")[0]+'/api.txt'

api = open(api_path).readlines()

api_key = api[0].split()[2]
api_secret = api[1].split()[2]

client = Client(api_key, api_secret)
#-----------------------------------------------------------

def data_historico(par,candle,time_aq):
    """
    Função que recupera os dados históricos de um par junto à Binance.
    """
    
    hist1 = client.get_historical_klines(par, candle, time_aq)
    
    open_time = []; Open = []; High = []; Low = []; Close = []; Volume = []
    Close_time = [] ;Quote_asset_volume = []; Number_of_trades = []
    #Taker_buy_base_asset_volume = []; Taker_buy_quote_asset_volume = [] ; Can_be_ignored = []
    for i in range(0,len(hist1)):
        open_time.append(float(hist1[i][0])); Open.append(float(hist1[i][1])); 
        High.append(float(hist1[i][2])); Low.append(float(hist1[i][3]))
        Close.append(float(hist1[i][4])); Volume.append(float(hist1[i][5]))
        Close_time.append(float(hist1[i][6])); #Quote_asset_volume.append(float(hist1[i][7]))
        Number_of_trades.append(float(hist1[i][8]))#; Taker_buy_base_asset_volume.append(float(hist1[i][9]))
        #Taker_buy_quote_asset_volume.append(float(hist1[i][10])); Can_be_ignored.append(float(hist1[i][11]))
    
    ts_open_time = [datetime.fromtimestamp(x/1000) for x in open_time]
    ts_close_time = [datetime.fromtimestamp(x/1000) for x in Close_time]
    
    d = {'Open': Open, 'High': High, 'Low': Low, 'Close': Close, 
         'Close_time': ts_close_time, 'Volume': Volume, 'N_of_trades': Number_of_trades}
    df_hist = pd.DataFrame(data=d, index=ts_open_time)
    
    #'Open_time': ts_open_time, retirei esta coluna do dataframe
    
    return df_hist #open_time,Open,High,Low,Close,Close_time,Volume,Number_of_trades


# In[1]:


def adriano(tipo,mess):
    """
    Disparador de mensagens para grupos específicos do telegram. Importante colar no local adequado a id do grupo.
    """
    
    # Parametros do Adriano
    bot = telegram.Bot(token='454164830:AAGYDxHizoRpQUbFsZEaAFZOmfR_14RqPBk')
    
    if tipo == 'ordem':
        ident = -292468956 #"Charlie_ordens"
        #-292524429 - Numeração anterior (Relatório de ordens)
    
    if tipo == 'controle':
        ident = -313228619 #"Charlie_controle"
        #-304610738 - Numeração anterior (Controle de ciclos)
    
    try:
        bot.send_message(chat_id=ident, text=mess)
    except:
        mess = 'Falha no telegram'
        #mail_sender2(mess)
        print (mess)


# In[4]:


def atualprec(par):
    """
    Esta função retorna o preço mais atualizado do ativo, bem como o open_time para rotulá-lo.
    """
    
    tickers = client.get_ticker(symbol=par)
    cot = float(tickers['lastPrice'])
    opentime = datetime.fromtimestamp(tickers['openTime']/1000) #Aqui deveria ser float(tickers['o...])? (10/08/18)
    
    return cot,opentime


# In[5]:


def portfolio(par,fator):
    """
    Esta função recebe o par e retorna os montantes em carteira, tanto do ativo, quanto da moeda base, bem 
    como os nomes dos componentes do par.
    """
    
    if par == 'BTCUSDT': m = 4
    else: m = 3
    
    atv_nm = par[:-m]
    bs_nm = par[-m:]
        
    ativo = float(client.get_asset_balance(asset = atv_nm)['free'])
    base = fator*(float(client.get_asset_balance(asset = bs_nm)['free']))
    
    return ativo,base,atv_nm,bs_nm


# In[6]:


def montante(par,op,mont_ent):
    """
    Esta função ajusta o montante da ordem de acordo com as especificações da binance.
    """
    
    cotacao = 0.0
    amin = 0.0
    n = 0
    erro = 'PAR - {}: Montante para {} não calculado;'.format(par,op)
    
    while n<3:
        try:
            cotacao = float(client.get_ticker(symbol=par)['lastPrice'])
            amin = float(client.get_symbol_info(par)['filters'][1]['stepSize'])
            
            if (amin != 0.0 and cotacao != 0.0): n = 5 #Sai do loop de tentar obter os parâmetros da corretora
            
            decimal = ('%f' % (amin)) #Transforma o amin em string com representação decimal

            trunc = decimal.index('1') #Localiza a posição da substring '1' na string 'decimal'

            if (trunc != 0): trunc = trunc - 1 #Atualiza a "casa" de truncamento 
            
        except BinanceAPIException as e:
            erro=erro+' "func_montante",'+' erro:'+str(e.code)+'. '+str(e.message)+'\n'
            n=n+1
            time.sleep(1)
    
    if n != 3: #Retira "1 amin" a fim de garantir arredondamento abaixo
        
        if op == 'buy': mont = abs(float(round(((mont_ent - amin*cotacao)/cotacao),trunc)))
        
        if op == 'sell': mont = abs(float(round((mont_ent - amin), trunc)))
    else: 
        mont = 0.0 #Indica que não foi possível calcular o mointante
        telegram_bot('ordem',erro)
    
    return mont  


# In[ ]:


def ordem(par,side,amount,tipo):
    """
    Esta função tenta tanto disparar as ordens de compra e venda para a binance, como obter o log das mesmas.
    """
    
    #Parâmetros
    taxa = 0.0; filled = 0.0; avg = 0.0; n = 0; m = 0; erro = 'PAR - {}: Ordem de {} não disparada;'.format(par,side)
    erro2 = 'PAR - {}: Log da ordem de {} não obtido;'.format(par,side)
    
    order = [] #Lista dos dados oredem 
    resp_ordem =[] #Lista dos dados do log de oredem
    
    while n < 3: #Início do loop que tenta a ordem. Tenta 3 vezes
        
        try: #Tenta dar a ordem
            order = client.create_order(symbol=par,side=side,type=tipo,quantity=amount)
            
            if len(order) != 0:
                
                while m < 3: #Início do loop que tenta obter o log da ordem. Tenta 3 vezes
                    
                    try: #Tenta obter o log da a ordem
                        
                        resp_ordem = client.get_my_trades(symbol=par,limit=1)
                        avg = float(resp_ordem[0]['price'])
                        filled = float(resp_ordem[0]['qty'])
                        taxa = avg*filled*0.00075             
                        
                        if len(resp_ordem) != 0:
                            
                            m = 5 #Saida do Loop que tenta obter o log da ordem
                            
                    except BinanceAPIException as e: #Se não conseguiu obter o log da ordem
                        
                        erro2 = erro2 + '"func_ordem",' + 'erro:' + str(e.code) + '.' + str(e.message) + '\n'
                        m = m + 1
                        time.sleep(1)
                        
                    n = 5 #Saida do Loop que tenta dar ordem
                
                if m == 3: telegram_bot('ordem',erro2) #Notifica em caso de log de ordem não obtido
                    
        except BinanceAPIException as e: #Se não conseguiu dar a ordem
            
            erro = erro + '"func_ordem",' + 'erro:' + str(e.code) + '.' + str(e.message) + '\n'
            n = n + 1
            time.sleep(1)
    
    if n == 3: telegram_bot('ordem',erro) #Notifica em caso de ordem não disparada
        
    return taxa, avg, filled
