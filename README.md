# PROVA - PYTHON

Serviço de manipulação de dados e persistência em base de dados relacional.

## Descrição
Este projeto foi desenvolvido na linguagem Python e seu código é 100% natural
ou seja não foi usado qualquer outra biblioteca de terceiro como Pandas por exemplo
O objetivo é importar para uma base de dados Postgresql o arquivo texto fornecido, 
trata-lo, validar cnpj e cpf contidos, chamados aqui de certificados. 
A rotina envolve em listar no terminal os certificados válidos e inválidos mostrando 
um resumo no final.
O processamento ocorre dentro de containeres de forma que dois deles são responsaveis
pela execução, sendo um container dedicado ao App e outro container dedicado ao banco de
dados Postgres

Requisitos
Este projeto foi desenvolvido em Linux na distro Ubuntu 22.04.
Para a execução deste projeto será necessário ter previamente instalado 
o Docker e o docker-compose. 
Abaixo seguem os links das respectivas instalações caso não os tenha, é só seguir as
instruçoes encontradas lá:
Docker:
https://docs.docker.com/get-docker/

docker-compose:
https://docs.docker.com/compose/install/#install-compose

Tenha certeza de ter o arquivo fornecido para teste, ele deverá constar na pasta data na raiz do projeto
e o seu nome deve ser "base_teste.txt"
ficando desta forma:
data/base_teste.txt

Instalação e execução do projeto
com o link do projeto fornecido, faça um clone em sua maquina.
Na pasta onde se enconta o projeto abra um terminal, verifique
se voce está vendo o arquivo docker-compose.yaml e em seguida
digite:
sudo docker-compose up --build

O docker irá montar os dois containeres e executará a importação da base de dados

Não é certo mas pode acontecer que durante a execução o processo pare e mostre a seguinte mensagem:
database system is ready to accept connections

interrompa com ctrl + c e repita o comando:
sudo docker-compose up --build

ao final da execução a seguinte saida será mostrada em seu terminal:

app_1  | CPF 04952526976 é válido.
app_1  | CPF 04209828840 é válido.
app_1  | ***********************************************
app_1  | TOTAL CPF VÁLIDOS:49997
app_1  | TOTAL CPF INVÁLIDOS:0
app_1  | ***********************************************
app_1  | TOTAL CNPJ VÁLIDOS:1
app_1  | TOTAL CNPJ INVÁLIDOS:0
prova-python_app_1 exited with code 0

Contato
Jobson Lira
fone: 27 99911-2412
email: jobson.lira@gmail.com
linkedin:
https://www.linkedin.com/in/jobson-lira/