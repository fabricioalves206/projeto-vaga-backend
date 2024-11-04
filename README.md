### Descrição

Este projeto é uma API para a empresa fictícia ACMEVita, permitindo que usuários consultem dados sobre departamentos, colaboradores e dependentes. A API foi desenvolvida com Django e pode ser executada em um ambiente Docker para facilitar a configuração e a execução.

---

## Funcionalidades

1. **Consultar todos os departamentos**: Permite visualizar a estrutura de departamentos da ACMEVita.
2. **Consultar colaboradores de um departamento**: Permite visualizar os colaboradores de cada departamento e identificar se possuem dependentes.

---

## Requisitos

- **Docker**

Caso não o tenha instalado em sua máquina, siga o tutorial para Ubuntu disponível no link <https://docs.docker.com/engine/install/ubuntu/> e para Windows <https://docs.docker.com/desktop/install/windows-install/>

---

## Configuração e Instalação

1. Clone o repositório e navegue até o diretório do projeto:

   ```bash
   git clone https://github.com/fabricioalves206/projeto-vaga-backend.git
   cd acmevita
2. Configure as variáveis de ambiente:
    - Crie um arquivo **.env** com as variáveis de ambiente necessárias, sendo elas **DEBUG** e **SECRET_KEY**.
    
    Nesse desafio, irei expor aqui no repositório a SECRET_KEY por motivos de conviniência.
    
    ```bash
    SECRET_KEY=django-insecure-&v7ys^ddd76d$%19ig-wr3#m#q*zay#+^gij5s@tg65!#$n@e)
    DEBUG=False
3. Rode o projeto com Docker
    - Primeiramente, crie uma imagem docker. Substitua **<NOME_DA_IMAGEM>** por um nome a sua escolha.
    ```bash
    docker build -t <NOME_DA_IMAGEM> .
- Execute o contêiner
    ```bash
    docker docker run -it -p 8000:8000 <NOME_DA_IMAGEM>

## Endpoits da API

Os endpoints disponíveis são:
- **GET/0.0.0.0:8000/api/v1/departments**: Retorna uma lista de todos os departamentos em formato JSON.
- **GET/0.0.0.0:8000/api/v1/departments/<department_id>/employees**: Retorna uma lista de colaboradores de um departamento específico com a flag have_dependents indicando se possuem dependentes.
- **GET/0.0.0.0:8000/swagger**: Retorna a documentação da API com Swagger

## Estrutura do Projeto

```plaintext
acmevita/
├── config/                    # Diretório principal do projeto Django
│   ├── __init__.py
│   ├── settings.py            # Configurações do projeto
|   ├── asgi.py                # Arquivo para deploy assíncrono ASGI
│   ├── urls.py                # URLS principais do projeto
│   └── wsgi.py                # Arquivo para deploy WSGI
├── user_department_api/       # App 'user_department_api' com as funcionalidades da API
│   ├── __init__.py
│   ├── fixtures/              # Dados para popular o banco de dados com o comando loaddata
|   ├── migrations/            # Diretório para as migrações do banco de dados
│   ├── admin.py               # Configurações do admin para o app
│   ├── apps.py                # Configuração do app Django
│   ├── models.py              # Modelos de dados
│   ├── views.py               # Views para os endpoints da API
│   ├── serializers.py         # Serializadores para transformar modelos em JSON
│   ├── urls.py                # URLS específicas do app
│   └── tests.py               # Testes unitários do app
├── .env                       # Variáveis de ambiente
├── Dockerfile                 # Arquivo para criação da imagem Docker
├── entrypoint.sh              # Script para roda o comando makemigrations, migrate e loaddata 
├── requirements.txt           # Dependências do projeto
├── manage.py                  # Script de gerenciamento do Django
README.md                      # Documentação do projeto
.gitignore