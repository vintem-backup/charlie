#!/bin/bash

echo 'Saindo da pasta teste'
cd ..

#Exportando variáveis
echo 'Exportando variáveis'
export server_name='DEV_(marcus)'
export `grep image_name environment`
export `grep container_name environment`

#Para o container em teste se houver
echo 'Parando container'
docker stop $container_name

#Exclui o container em teste se houver
echo 'Excluindo container'
docker container rm $container_name

#Exclui Imagem
echo 'Excluindo Imagem'
docker rmi $image_name

#Construção do Artefato
echo 'Construindo imagem'
docker image build -t $image_name .

#Roda container
echo 'Rodando container'
docker container run -d --name $container_name -e MACHINE=$server_name $image_name