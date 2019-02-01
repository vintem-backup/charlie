# Charlie tradebot: To do list

## Create........: 2019-JAN-26
## Last Update...: 2019-JAN-28
#### Author......: Marcus Mello 
#### Contact.....: (mandealista@gmail.com)

[PT_br]

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

## End: 2019-JAN-30 (Dead line)
## End: 2019-JAN-28 (Real end)