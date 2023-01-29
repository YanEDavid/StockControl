# StockControl

🚧🚧🚧🚧🚧🚧UNDER CONSTRUCTION🚧🚧🚧🚧🚧🚧

🚧🚧🚧🚧🚧🚧PARA TESTAR🚧🚧🚧🚧🚧🚧

Passos a serem reproduzidos
  - Instalar a biblioteca virtualenv
    ~~~python
    pip install virtualenv
    ~~~
  - Criar/entrar na virtualenv
    ~~~python
    python -m virtualenv -p=”Caminho onde está o python.exe” venv
    ~~~
    ~~~cmd
    venv\Scripts\activate
    ~~~
  - Assim que entrar na virtualenv, instalar o Django
    ~~~python
    pip install django
    ~~~
  - Após instalar o django, atualizar as migrações
    ~~~python
    py manage.py migrate
    ~~~
    ~~~python
    py manage.py makemigrations
    ~~~
  - Criar um administrador
    ~~~python
    py manage.py createsuperuser
    ~~~
  - Inicializar o servidor
    ~~~python
    py manage.py runserver
    ~~~
  - Entrar no endereço padrão
    ~~~python
    localhost:8000
    ~~~

Desenvolvido por: *David Rodrigues e Yan Sardinha*
