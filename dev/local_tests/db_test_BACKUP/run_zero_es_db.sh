#!/bin/bash

#1 - Exportando variáveis

#1.1 - Ambiente
echo 'Exportando Variáveis de Ambiente'
long_path=`pwd`
root=`echo ${long_path%/dev/local_tests/db_test}`

#1.1.1 - Nome da máquina
export server_name='DEV_(marcus)'

#1.1.2 - app_get_data container
export `grep app_get_data_docker_host $root/config/environment`
export `grep app_get_data_path_to_image $root/config/environment`
export `grep app_get_data_image_name $root/config/environment`
export `grep app_get_data_container_name $root/config/environment`

#2 - Para e exclui o container em teste
echo 'Parando e excluindo container'
docker stop $app_get_data_container_name && docker container rm $app_get_data_container_name

#3 - Pull image
echo 'Baixando imagem'
docker pull $app_get_data_docker_host/$app_get_data_path_to_image/$app_get_data_image_name

#4 - Run app
echo 'Running container'
docker run -d --name $app_get_data_container_name -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" $app_get_data_docker_host/$app_get_data_path_to_image/$app_get_data_image_name