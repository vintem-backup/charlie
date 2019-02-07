#!/bin/bash

#Recupera o ID desta instância:
instanceid=`/usr/bin/curl -s http://169.254.169.254/latest/meta-data/instance-id`
    #OBS.: É preciso liberar a porta 80 para este CIDR (169.254.169.254/32)

#Associa o IP a esta instância
aws ec2 associate-address --region us-east-1 --instance-id $instanceid --public-ip 3.92.67.179

#Exportando variáveis
#credenciais
echo 'Exportando Credenciais'

export home='/home/ec2-user'
export `grep GITLAB_REGISTRY_LOGIN $home/credentials.txt`
echo 'GITLAB_REGISTRY_LOGIN = ' $GITLAB_REGISTRY_LOGIN

export `grep GITLAB_REGISTRY_PASSWORD $home/credentials.txt`
echo 'GITLAB_REGISTRY_PASSWORD = ' $GITLAB_REGISTRY_PASSWORD

#Ambiente
echo 'Exportando Variáveis de Ambiente'

export `grep server_name $home/environment`
echo 'server_name = ' $server_name

export `grep image_name $home/environment`
echo 'image_name = ' $image_name

export `grep container_name $home/environment`
echo 'container_name = ' $container_name

export `grep docker_host $home/environment`
echo 'docker_host = ' $docker_host

export `grep path_to_image $home/environment`
echo 'path_to_image = ' $path_to_image

#Limpando credenciais
echo 'Excluindo credenciais'
#rm -f $home/credentials.txt

#Para e exclui o container em teste
echo 'Parando e excluindo container'
docker stop $container_name && docker container rm $container_name

#Loga no registry
echo 'Logando no registry.gitlab.com'
docker login registry.gitlab.com -u $GITLAB_REGISTRY_LOGIN -p $GITLAB_REGISTRY_PASSWORD

#Pull image
echo 'Baixando imagem'
docker pull $docker_host/$path_to_image/$image_name

#Run app
echo 'Running container'
docker container run -d --name $container_name -e MACHINE=$server_name $docker_host/$path_to_image/$image_name