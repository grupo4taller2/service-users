#!/bin/bash

if [ "lint" == "$1" ]
then
	docker exec fiuber.service-users.dev flake8

elif [ "copiar" == "$1" ]
then
	echo 'copiaaaaar'
	
elif [ "montar" == "$1" ]
then
	echo 'montar'
fi
