# Elegos
![Imagem do Projeto](https://github.com/PcObserver/assets/blob/main/elegos_image.png)

Com o rápido avanço da tecnologia, a quantidade de dispositivos IoT vem crescendo exponencialmente. Diversos sistemas oferecem soluções para operar esses dispositivos, mas a maioria deles dá suporte apenas aos da própria marca, criando dificuldades em construir ecossistemas IoT com controle unificado. O projeto “Elegos” consiste de um controle universal de dispositivos IoT que visa unificar o gerenciamento desses dispositivos em uma única plataforma.

Utilizando um hub baseado em Raspberry Pi 3 modelo B, o sistema detecta automaticamente dispositivos na rede local e permite o envio de comandos, mesmo sem conexão com a internet. Além disso, um repositório online de comandos permite a adição e o compartilhamento de novos dispositivos de forma colaborativa, permitindo a inclusão de novos dispositivos e comandos, bem como avaliação das contribuições criadas pelos usuários pela própria comunidade utilizando um sistema de avaliação por votos positivos.

## Repositórios Associados
- [Back-end da Comunidade de Dispositivos IoT](https://github.com/PcObserver/iot-commands-hub)
- [Front-end da Comunidade de Dispositivos IoT](https://github.com/PcObserver/TCC-iot-hub)
- [Sistema do Raspberry Pi](https://github.com/PcObserver/TCC-RaspClient)

## Objetivo

Este repositório consiste na implementação do Back-end da comunidade de dispisitivos IoT, sistema web onde usuários podem cadastras marcas, comandos e dispositivos. A API desenvolvida neste repositório é consumida tanto pelo Front-end da comunidade de dispositivos IoT, quanto pelo sistema servido no Raspberry Pi.

## Tecnologias Utilizadas

- Python 3.11.5
- Django 5.0.4
- PostgreSQL 15
- Swagger

## Configuração do Projeto

### Instalando Docker

Este projeto foi desenvolvimento para rodar com Docker. É utilizado Docker e Docker Compose para criação e gerenciameno de containers. Toda a informação necessária para a configuração do Docker pode ser consultada no link da documentação oficial abaixo:

[https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)

### Configurando variáveis de ambiente

Para configurar as variáveis de ambiente necessárias para rodar o projeto localmente, crie um arquivo `.env` dentro do diretório `iot_commands_hub`, e ponha o conteúdo abaixo dentro do arquivo:

```
SECRET_KEY='Uei4bxPzarB021Z2B0PzGw'
DEBUG=True

# DATABASE SETTINGS
DATABASE_NAME='iot_commands_hub'
DATABASE_USER='postgres'
DATABASE_PASSWORD='postgres'
DATABASE_HOST='db'
DATABASE_PORT='5432'
```

Com estas configurações feitas, basta rodar o comando `docker-compose up` para inicializar o sistema. 

O projeto também oferece uma documentação dos endpoints da API, disponibilizada pelo Swagger, que pode ser acessada no link abaixo após iniciar o sistema:
[http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/)





















# README - IoT Commands Hub

Este repositório implementa o back-end da comunidade de dispositivos IoT do Elegos. O programa oferece a implementação de uma API Rest, juntamente com Swagger para verificar os endpoints disponíveis

## Configuração do Projeto

### Instalando Docker

Este projeto foi desenvolvimento para rodar com Docker. É utilizado docker e docker compose. Toda a informação necessária para a configuração do Docker pode ser consultada no link da documentação oficial abaixo:

[https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)

### Configuring environment variables

Para configurar as variáveis de ambiente necessárias para rodar o projeto localmente, crie um arquivo `.env` dentro do diretório `iot_commands_hub`, e ponha o conteúdo abaixo dentro do arquivo:

```
SECRET_KEY='Uei4bxPzarB021Z2B0PzGw'
DEBUG=True

# DATABASE SETTINGS
DATABASE_NAME='iot_commands_hub'
DATABASE_USER='postgres'
DATABASE_PASSWORD='postgres'
DATABASE_HOST='db'
DATABASE_PORT='5432'
```

Com estas configurações feitas, basta rodar o comando `docker-compose up` para inicializar o sistema. 

A documentação disponibilizada pelo Swagger pode ser acessada em:
[http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/)
