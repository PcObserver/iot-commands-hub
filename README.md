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
