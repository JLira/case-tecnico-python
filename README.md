# PROVA - PYTHON

Serviço de manipulação de dados e persistência em base de dados relacional.

## Descrição
Este projeto foi desenvolvido na linguagem Python e seu código é 100% natural
ou seja não foi usado qualquer outra biblioteca de terceiro como Pandas por exemplo.<br>
O objetivo é importar para uma base de dados Postgresql o arquivo texto fornecido, 
tratá-lo, validar cnpj e cpf contidos, chamados aqui de certificados.<br> 
A rotina envolve em listar no terminal os certificados válidos e inválidos mostrando 
um resumo no final.<br>
O processamento ocorre dentro de containeres de forma que dois deles são responsáveis
pela execução, sendo um container dedicado ao App e outro container dedicado ao banco de
dados Postgres

### Requisitos
Este projeto foi desenvolvido em Linux na distro Ubuntu 22.04.
Para a sua execução será necessário ter previamente instalado<br> 
o Docker e o docker-compose. <br>
Abaixo seguem os links das respectivas instalações caso não os tenha, é só seguir as
instruçoes encontradas lá:<br>
Docker:<br>
https://docs.docker.com/get-docker/<br>
docker-compose:<br>
https://docs.docker.com/compose/install/#install-compose<br>

Tenha certeza de ter o arquivo fornecido para teste, ele deverá constar na pasta <b>data</b> na raiz do projeto
e o seu nome deve ser "base_teste.txt"
ficando desta forma:<br>
```data/base_teste.txt```

### Instalação e execução do projeto
Com o link do projeto fornecido, faça um clone em sua maquina.<br>
Na pasta onde se encontra o projeto abra um terminal, verifique
se voce está vendo o arquivo docker-compose.yaml e em seguida
digite:<br>
```sudo docker-compose up --build```

O docker irá montar os dois containeres e executará a importação da base de dados
```ruby
Não é certo, mas pode acontecer que durante a execução o processo pare e mostre a seguinte mensagem:
```
```database system is ready to accept connections```

Interrompa com <b>ctrl + c</b> e repita o comando:<br>
```sudo docker-compose up --build```

ao final da execução a seguinte saida será mostrada em seu terminal:
```
app_1  | CPF 04952526976 é válido.
app_1  | CPF 04209828840 é válido.
app_1  | ***********************************************
app_1  | TOTAL CPF VÁLIDOS:49997
app_1  | TOTAL CPF INVÁLIDOS:0
app_1  | ***********************************************
app_1  | TOTAL CNPJ VÁLIDOS:1
app_1  | TOTAL CNPJ INVÁLIDOS:0
prova-python_app_1 exited with code 0
```


### Contato
Jobson Lira<br>
fone: 27 99911-2412<br>
email: jobson.lira@gmail.com<br>
linkedin:<br>
https://www.linkedin.com/in/jobson-lira/
