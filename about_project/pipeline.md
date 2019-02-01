# Charlie tradebot: Pipeline CI/CD

## Create........: 2019-JAN-23
## Last Update...: 2019-JAN-23
#### Author......: Marcus Mello 
#### Contact.....: (mandealista@gmail.com)

[PT_br]

#### Construido para gitlab CI, apresenta uma solução docker + AWS EC2 para o paradigma de uma aplicação de alta disponibilidade em nuvem.

Após um commit e respectivo push o runner deve processar os seguintes jobs:

### Job 1 - Build and delivery | dividido em três estágios:
    a) Before_script:
    1.1 - Logar em registry.gitlab.com;
    b) Script:
    1.2 - "Builda" a imagem a partir do contexto (Dockerfile);
    1.3 - "Push" da imagem para o registry.gitlab.com

### Job 2 - Update app | dá um "refresh" no servidor de produção para que o mesmo rode a nova versão do app:
    A shell deve usar comandos do AWS CLI para terminar a atual instância em produção que roda o app. Espera-se que o AutoScaling lance uma nova instância no lugar da que foi terminada
 
## Pré requesitos

1 - Instância EC2, devidamente configurada como um servidor NGINX, a fim de responder às solicitações de "Health Check" do load balancer. Além disso, deve ter docker e AWS CLI instalados;

2 - Embarcar no sistema as credenciais* AWS bem como as do registry.gitlab.com;
        
        *Embarcar também as credenciais da corretora

3 - Embarcar no init do sistema a shell run_app.sh*;
        
        *- Comando AWS CLI para "capturar" o IP alocado;
         - Logar em registry.gitlab.com;
         - Docker run.

4 - Criar uma AMI a partir desta instância. Esta AMI será o ponto de partida (launch configuration) do autoscaling;

5 - Um autoscaling devidamente configurado para manter sempre 1 instância (quantidade mínima desejada). Isso garante disponibilidade em qualquer cenário;

6 - Firewall de borda (network ACLs) e de máquina (security groups) devidamente configurados;

7 - Uma imagem de container com Docker, Python e AWS CLI instalados, a fim de servir como runner do gitlab CI;

8 - Embarcar as credenciais como variáveis de ambiente (de grupo) no gitlab CI.