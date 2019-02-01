# Charlie tradebot: Project Overview

## Create........: 2019-JAN-24
## Last Update...: 2019-JAN-24
#### Author......: Marcus Mello 
#### Contact.....: (mandealista@gmail.com)

[PT_br]

## Estado Atual do Projeto

## Refatorações

    ### Correções

        - Implementar função de saída do movimento em 3 cenários:
    
            1) Recebimento de ordem do módulo de estratégia;
            2) Stop Loss/gain do tipo "escada", a fim de evitar a saida apenas quando a média móvel "curta" cruzar a "longa" para baixo;
            3) Tempo de posição (?);
    
        - Corrigir a entrada no movimento para não ser feita a mercado;
        - Implementar "trava" para evitar "mercado de lado" (evitar falsos positivos);
        - Buscar um indicador de "validação" para entrada no movimento
            - Entrar com montantes diferentes nos cenários em que não haja validação
            - 

    ### Aprimoramentos

        - Implemetar a tomada de dados para constituição de uma malha de 1 min, adquirida por programa conteinerizado, independente, acionado quando solicitado pelo programa controlador.
    
        - Conteirizar os módulos e o banco de dados (REDIS).
    
        - Orquestrar a composição do cluster, bem como seu deploy.
  
    ### Justificativas
  
        - Zelar pela integração contínua (CI) e entrega contínua (CD) com atualizações e correções rápidas e eficazes.
  
        - Observar a segurança de dados sensíveis.
  
        - Seguir metodologia produtiva calcada em preceitos de boas práticas de programação como aquelas descritas no "clean code" e "12factors".
  
        - Atentar para a perfomance, adotando motores de banco de dados mais condizentes com o problema tratado.
  
        - Tornar o programa "cloud agnostic", bem como agnóstico ao mercado, ou seja, que tenha portabilidade e escala para atuar em outros mercados além da binance e além das criptomoedas como, por exemplo, corretoras de valores.
    
        - Melhorar a interação com o programa através de uma interface web, através da qual seja possível:
            1) Alterar a tabela (chave-valor) dos parâmetros de operação do robô.
            2) Acompanhar (com recursos do tipo gráficos interativos) os logs tanto de desempenho (backtest, "teste de tempo real" e produção) quanto do servidor.