# API REST com Aiohttp + Aiopg

CRUDE de uma API REST com os endpoints implementados com aiohttp e acesso à base de dados com aiopg.

## Requisitos
* docker
* docker-compose
* python3.7
* virtualenv

## Banco de Dados

A plataforma de banco de dados utilizada foi `PostgreSQL` em sua versão `11.0`. A instância de banco de dados utilizada foi criada com a utilização de contêiner Docker.

### Criação da instância

O artefato necessário para criação da instância encontra-se em `docker/docker-compose.yml`.Considerando que o usuário se encontra no diretório raiz do projeto:

```shell
docker-compose -f docker/docker-compose.yml -d
```

## Aplicação


