# coding: utf-8

import sys
import os

sys.path.append(os.getcwd().split(sep="modules")[0])
import modules
from modules import func

from datetime import datetime
from datetime import date

def prod(i, inicio, param, mmc, mml, notif):
    """
    Deve notificar, pelo telegram, o funcionamento do robô, a uma taxa de tempo específica.
    """
    
    inicio = str(inicio)[:16]
    
    par = param[1].split()[2]; freq = int(param[13].split()[2]); medlonga = int(param[3].split()[2]); medcurta = int(param[2].split()[2]); candle = param[0].split()[2]
    
    preco,instante = func.atualprec(par); atv,bs,atv_nm,bs_nm = func.portfolio(par,1.0)
    
    cap = float(bs) + float(atv)*float(preco)
    
    atv = '%.5f'%(float(atv)); bs = '%.2f'%(float(bs)); preco = '%.2f'%(float(preco)); cap = '%.2f'%(cap)
    
    mmc = '%.2f'%(float(mmc)); mml = '%.2f'%(float(mml))
    
    if ( float(mmc) > float(mml) ): posicao = f'Comprado em {atv_nm}'
    else: posicao = 'Vendido'
    
    dif_min = float((datetime.now() - notif).total_seconds()/60)
    
    if (dif_min >= freq or i ==0):
        
        notif = datetime.now() #Troca o horário da última notificação

        mess = f" - RELATÓRIO {par} - \n \n #Ciclo \n Iníc: {inicio} \n Ciclo: {i} \n \n #Estratégia \n Candle: {candle}m \n MMC: {mmc} {bs_nm} \n ({medcurta} períodos) \n \n MML: {mml} {bs_nm} \n ({medlonga} períodos) \n \n Posic: {posicao} \n \n #Financeiro \n Capital: {cap} {bs_nm} \n Ativo: {atv} {atv_nm} \n Base: {bs} {bs_nm} \n 1 {atv_nm} = {preco} {bs_nm} \n \n Próx. relatório em {freq} min."

        func.adriano('controle',mess)
        
    return notif
