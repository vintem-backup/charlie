# coding: utf-8

"""
Atualiza (caso exista) ou cria o arquivo de logs a partir das variáveis obtidas, como saídas dos módulos, 
dos movimentos.
"""

import pandas as pd

def prod(param,ordem,mmc,mml,instante,ativo,base,taxa,preco_inst,preco_mov):
    
    #1 - PARÂMETROS
    par = param[1].split()[2]; candle = param[0].split()[2]; medcurta = int(param[2].split()[2])
    medlonga = int(param[3].split()[2])

    logpath = str(param[6].split()[2]).format(par,candle)

    log_name = '{}m_{}x{}-log.csv'.format(candle,medcurta,medlonga)

    #logpath = os.getcwd().split(sep="estrat")[0] + param[6].split()[2] CAMINHO ANTIGO

    #2 - OPERAÇÃO
    
    open_time = []; ORD = []; MMC = []; MML = []; ATIVO = []; BASE = []; PRC_ENT = []; PRC_OP = []; TX = []; CAP = []
    
    capital = float(base) + float(ativo)*float(preco_inst)
    
    open_time.append(instante); ORD.append(ordem); MMC.append(mmc); MML.append(mml); ATIVO.append(ativo);
    BASE.append(base); PRC_ENT.append(preco_inst); PRC_OP.append(preco_mov); TX.append(taxa); CAP.append(capital)
    
    d = {'ORD': ORD, 'MMC': MMC, 'MML': MML, 'ATIVO': ATIVO, 'BASE': BASE, 'PRC_ENT': PRC_ENT,
         'PRC_OP': PRC_OP, 'TX': TX, 'CAP': CAP}
    
    log_corrente = pd.DataFrame(data=d, index=open_time)
    
    #Tenta ler o arquivo, se existir, e o complementa até o instante atual
    try: 

        log = pd.read_csv(logpath+log_name, index_col='Open_time')       #1 - Encontra o arquivo logs.csv na pasta
        print('log lido') #TESTE, APAGAR DEPOIS DE OK
        print(' ') #TESTE, APAGAR DEPOIS DE OK
          
        log = log.append(log_corrente)

    #NÃO Encontra o arquivo logs.csv na pasta, ENTÃO Cria o arquivo.
    except:
        
        print('Criando arquivo de log pela primeira vez') #TESTE, APAGAR DEPOIS DE OK
        log = log_corrente
        print(' ') #TESTE, APAGAR DEPOIS DE OK
    
    log.to_csv(logpath+log_name, index=True, index_label='Open_time', date_format='%Y-%m-%d %H:%M:%S')
    print('Arquivo de log salvo') #TESTE, APAGAR DEPOIS DE OK
    print(' ') #TESTE, APAGAR DEPOIS DE OK
    
    return log
