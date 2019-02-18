#!/bin/bash

#Recupera o ID desta instância:
instanceid=`/usr/bin/curl -s http://169.254.169.254/latest/meta-data/instance-id`
    #OBS.: É preciso liberar a porta 80 para este CIDR (169.254.169.254/32)

#Associa o IP a esta instância
aws ec2 associate-address --region us-east-1 --instance-id $instanceid --public-ip 3.92.67.179

#Exportando variáveis
#credenciais
export home='/home/ec2-user'
export `grep GITLAB_REGISTRY_LOGIN $home/credentials.txt`
export `grep GITLAB_REGISTRY_PASSWORD $home/credentials.txt`

#Ambiente
export `grep server_name $home/environment`
export `grep image_name $home/environment`
export `grep container_name $home/environment`
export `grep docker_host $home/environment`
export `grep path_to_image $home/environment`

#Limpando credenciais
rm -f $home/credentials.txt

#Para e exclui este container, em caso de reinicio do script
docker stop $container_name && docker container rm $container_name

#Loga no registry
docker login registry.gitlab.com -u $GITLAB_REGISTRY_LOGIN -p $GITLAB_REGISTRY_PASSWORD

#Baixa imagem do container
docker pull $docker_host/$path_to_image/$image_name

#Dispara o container da aplicacao
docker container run -d --name $container_name -e MACHINE=$server_name $docker_host/$path_to_image/$image_name