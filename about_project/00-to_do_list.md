# Charlie tradebot: To do list

## Create........: 2019-JAN-26
## Last Update...: 2019-FEV-06
#### Author......: Marcus Mello 
#### Contact.....: (mandealista@gmail.com)

[PT_br]

# SPRINT - 

## Start: 2019-JAN-26

### I - AWS
1 - Nova conta AWS....................................................[ok]
    1.1 - Configurar VPC, firewalls e lançar instância................[ok]
2 - Configurar instância..............................................[ok]
    2.1 - Instalar e configurar nginx.................................[ok]
    2.2 - Instalar Docker e AWS CLI*..................................[ok]
        *Amazon linux 2 já vem com AWS CLI instalado
    2.3 - Testar o container..........................................[ok]
    2.4 - Testar parte AWS............................................[ok]
        2.4.1 - Alocar um IP teste....................................[ok]
        2.4.2 - Rodar comando.........................................[ok]
        2.4.3 - Dealocar IP teste.....................................[ok]
        2.4.4 - Portar o comando para shell (trocar IP)...............[ok]
3 - Subir shell run_app.sh para init da instância.....................[ok]
4 - Criar AMI*........................................................[ok]
    * Rodar um container prune antes..................................[ok]
5 - Integrar recursos do servidor (Load Balancer, autoScaling)........[ok]

## II - Gitlab_CI
1 - Criar conta no docker hub*........................................[ok]
2 - Imagem do container (dockerfile)*.................................[ok]
        *Obtida em https://hub.docker.com/r/guss77/dind-awscli/
    2.1 - Preparar, buidar, testar....................................[ok]
    2.2 - Push para o hub*............................................[ok]
        *Não foi necessário
3 - Salvar variáveis de estado (para o grupo).........................[ok]
4 - Testar pipeline...................................................[ok]

## III - Framework
1 - Root........................................................[almost_ok]
    1.1 - .gitignore............................................[ok]
    1.2 - .gitlab-ci.yml........................................[ok]
    1.3 - build_and_delivery.sh.................................[ok]
    1.4 - Dockerfile............................................[ok]
    1.5 - README.md.............................................[draft]
    1.6 - requirements.txt......................................[ok]
    1.7 - update.sh.............................................[ok]
        1.7.1 - Comando para matar a instância em produção......[ok]
2 - .AWS........................................................[part]
    2.1 - README.md.............................................[part]
    2.2 - run_app.service.......................................[ok]
    2.3 - run_app.sh............................................[ok]
    2.4 - setup.sh..............................................[ok]
3 - .gitlab_runner..............................................[ok]
    2.1 - Dockerfile*...........................................[ok]
        *Não necessário. Imagem declarada no .gitlab-ci.yml
    3.2 - README.md.............................................[part]

## Dead_line..: 2019-JAN-30
## End_task...: 2019-JAN-28 
## P.S........: Documentação pendente

# SPRINT - 

## Start: 2019-FEV-06

### I - FRAMEWORK
1 - Elasticsearch.....................................................[]
        1.1 - Subir o serviço em container (maquina local)............[]
        1.2 - Manipular elasticsearch com script teste................[]
2 - get_data..........................................................[]
        2.1 - Manipular o bd_es com script teste (não container)......[]
        2.2 - Escrever* programa de aquisição dados (com modelo para
              malha de minuto)........................................[]
              *Apartir de parte do código já escrito e do modelo dispo_
              nível em:https://sammchardy.github.io/binance/2018/01/08/
                       historical-data-download-binance.html
        2.3 - Corrigir modularização do código*.......................[]
              *https://wiki.python.org.br/ModulosPacotes
        2.4 - Containerizar script....................................[]
3 - core_app..........................................................[]
        3.1 - ........................................................[]
4 - docker-compose.yml................................................[]
5 - Revisão...........................................................[]
6 - Testes locais.....................................................[]
7 - gitlab-ci.yml.....................................................[]
8 - Teste pipeline....................................................[]

### III - PRODUCTION HOST SERVER
1 - Recriar infra.....................................................[]
        1.1 - Atenção ao volume EBS persistente.......................[]
        1.2 - "Serviços gerais" (AMI, LC, AS, LB, TG, etc)............[]
2 - Setup da máquina..................................................[]
        2.1 - ........................................................[]
3 - Teste de persistência de dados....................................[]
4 - Codificar* infraestrutura.........................................[]
        *Terraform?

## Dead_line..: 2019-FEV-10
## End_task...: 2019-FEV- 
## P.S........: