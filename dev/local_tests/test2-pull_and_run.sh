#!/bin/bash

#Exportando variáveis
#credenciais
echo 'Exportando Credenciais'

export `grep GITLAB_REGISTRY_LOGIN credentials.txt`
export `grep GITLAB_REGISTRY_PASSWORD credentials.txt`

#Ambiente
echo 'Exportando Variáveis de Ambiente'

export server_name='DEV_(marcus)'
export `grep image_name ../environment`
export `grep container_name ../environment`
export `grep docker_host ../environment`
export `grep path_to_image ../environment`

#Limpando credenciais
echo 'Excluindo credenciais'
#rm -f `pwd`/credentials.txt

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