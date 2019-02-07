#!/bin/sh

#Exportando variáveis
echo 'Exportando variáveis'
export `grep image_name environment`
export `grep container_name environment`
export `grep docker_host environment`
export `grep path_to_image environment`

#Constroi Imagem
echo 'Buildando Imagem'
docker image build -t $docker_host/$path_to_image/$image_name .

#Pushing Image
echo 'Upload da Imagem para o registry'
docker push $docker_host/$path_to_image/$image_name