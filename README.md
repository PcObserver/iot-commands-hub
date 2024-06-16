# Elegos
![Imagem do Projeto](https://github.com/PcObserver/assets/blob/main/elegos_image.png)

Com o rápido avanço da tecnologia, a quantidade de dispositivos IoT vem crescendo exponencialmente. Diversos sistemas oferecem soluções para operar esses dispositivos, mas a maioria deles dá suporte apenas aos da própria marca, criando dificuldades em construir ecossistemas IoT com controle unificado. O projeto “Elegos” consiste de um controle universal de dispositivos IoT que visa unificar o gerenciamento desses dispositivos em uma única plataforma.

Utilizando um hub baseado em Raspberry Pi 3 modelo B, o sistema detecta automaticamente dispositivos na rede local e permite o envio de comandos, mesmo sem conexão com a internet. Além disso, um repositório online de comandos permite a adição e o compartilhamento de novos dispositivos de forma colaborativa. A arquitetura do sistema foi projetada para facilitar a inclusão de novos dispositivos e comandos. Com a conclusão da versão inicial, o projeto busca continuamente expandir suas capacidades, proporcionando um controle mais abrangente e personalizado para os usuários.

## Repositórios Associados

- [Back-end da Comunidade de Dispositivos IoT]([link-do-repositorio-1](https://github.com/PcObserver/iot-commands-hub))
- [Front-end da Comunidade de Dispositivos IoT]([link-do-repositorio-2](https://github.com/PcObserver/TCC-iot-hub))
- [Sitema do Raspberry Pi]([link-do-repositorio-3](https://github.com/PcObserver/TCC-RaspClient))

## Objetivo

Este repositório consiste na implementação do Back-end da comunidade de dispisitivos IoT, sistema web onde usuários podem cadastras marcas, comandos e dispositivos IoT. A API desenvolvida neste repositório é consumida tanto pelo Front-end da comunidade de dispositivos IoT quanto o sistema servido no Raspberry Pi.

## Tecnologias Utilizadas

- Python
- Django
- PostgreSQL 15
- Swagger

## Configuração do Projeto

### Instalando Docker

Este projeto foi desenvolvimento para rodar com Docker. É utilizado Docker e Docker Compose para criação e gerenciameno de containers. Toda a informação necessária para a configuração do Docker pode ser consultada no link da documentação oficial abaixo:

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
