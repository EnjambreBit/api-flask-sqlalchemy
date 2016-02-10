# api-flask-sqlalchemy

Este repositorio contiene un ejemplo de API desarrollada utilizando
Flask y SQLAlchemy.

El objetivo principal del repositorio es ilustrar algunas ideas que detallamos
en el artículo http://enjambrebit.com.ar/blog/creando-api-con-flask, aunque
también puede servir como punto de partida para hacer una API con estas
tecnologías.

## ¿Qué incluye?

El proyecto está desarrollado con Flask, virtualenv, usa SQLAlchemy como ORM
para los modelos, implementa CORS e identificadores de registros usando UUID.

También incluye un modelo de datos ilustrativo "User", con algunas rutas
para crear, listar, modificar y eliminar registros.


## ¿Cómo iniciar el proyecto?

El primer paso es crear un entorno virtual, para que el proyecto completo
quede aislado del resto del sistema:


    ➤ virtualenv venv --no-site-packages


Luego se tiene que ingresar en el entorno virtual e instalar las dependencias:


    ➤ . venv/bin/activate        # o si se usa fish: . venv/bin/activate.fish
    ➤ make init


## Tareas con make

El resto de los comandos se pueden iniciar como tareas make, si escribís
``make`` en consola deberá aparecer el siguiente listado:

    ➤ make

    Commands for api-flask-sqlalchemy

        init         Install all dependencies.
        initdb       Creates the database.
        test         Run tests one time.
        watch        Run tests in a loop.
        run          Run the webapp.


## Tests

Para ejecutar los tests podés ejecutar:

    ➤ make test

o bien, ejecutar los tests de forma constante:


    ➤ make watch

    nosetests --with-watch tests.py --rednose --force-color
    ......
    -----------------------------------------------------------------------------
    6 tests run in 0.4 seconds (6 tests passed)



## Ejemplos de invocación a la API

Una vez iniciada la API con ``make run``, se pueden hacer consultas directamente
usando ``CURL``. Estos son algunos ejemplos:

Crear un usuario:

    curl -H "Content-Type: application/json" -X POST -d '{"firstname":"James", "lastname":"Drapper"}' http://localhost:5000/users

Obtener la lista de usuarios:

    curl -X GET http://localhost:5000/users

Borrar un usuario por ID:

    curl  -X DELETE  http://localhost:5000/users/7ce0aaf1-2215-4a8a-bc1d-9eba789b28c5


## Más información

- http://enjambrebit.com.ar/blog/creando-api-con-flask
