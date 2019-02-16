# coding: utf-8

#Módulo 3 - Ação: Executa as ordens de compra e venda (se for o caso)

"""
A partir do arquivo de parâmetros e da ordem emitida pelo módulo de estratégia, este módulo pode proceder, 
basicamente, de duas formas: produção ou teste.

2 - DESENVOLVIMENTO: Apenas opera sobre o montante fictício, atualizando as variáveis em caso de estratégia 
indicar movimento. Retorna as mesmas variáveis acima, a menos de instante
"""

import sys
import os

sys.path.append(os.getcwd().split(sep="modules")[0])
import modules
from modules import func

def prod(param,ordem):
    
    """
    Executa as ordens, notifica no telegram. 
    Retorna: composição do portfólio e os preços (instantâneo e aquele, de fato, do movimento), bem como a taxa do        
    movimento, caso haja, além do instante que quele moviento aconteceu.
    """
    
    #1 - PARÂMETROS
        
        #1.1 - Default 
    taxa = 0.0; preco_mov = 0.0
        #1.2 - Arquivo de parâmetros
    par = param[1].split()[2]; fator = float(param[14].split()[2]) #É o limitador de montante
        #1.3 - corretora
    ativo,base,atv_nm,bs_nm = func.portfolio(par,fator); preco_inst,instante = func.atualprec(par)

    #2 - TESTES LÓGIGOS

    if ordem != 'keep': #Vai comprar ou vender
    
        if ordem == 'buy':
            mont = float(base)
            mess='Sinal de Compra.'
            movimento = 'comprados'
            
        if ordem == 'sell':
            mont = float(ativo)
            mess='Sinal de Venda.'
            movimento = 'vendidos'
            
        func.adriano('ordem',mess) #Notifica o Sinal
        
        #Execução da ordem
        amount = func.montante(par,ordem,mont)
        taxa, preco_mov, filled = func.ordem(par,ordem,amount,'market')    
       
        mess2 = '{} {} {} a um preço de {} {}, com uma taxa de {} {}'.format(filled, atv_nm, movimento, round(float(preco_mov),2), bs_nm, round(float(taxa),2), bs_nm)
       
        if (filled != 0.0): func.adriano('ordem',mess2) #Notifica o movimento concluido com sucesso
        
        ativo,base,atv_nm,bs_nm = func.portfolio(par,fator) #Atualiza os montantes
    
    return instante,ativo,base,taxa,preco_inst,preco_mov
