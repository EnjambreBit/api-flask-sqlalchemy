# api-flask-sqlalchemy

Un ejemplo de API desarrollada con Flask y SQLAlchemy, tal como se
describe en http://enjambrebit.com.ar/blog/creando-api-con-flask


## ¿Qué incluye?

El proyecto está desarrollado con Flask, virtualenv, usa SQLAlchemy como ORM
para los modelos, implementa CORS e identificadores de registros usando UUID.


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

Para ejecutar los tests podrías ejecutar:

    ➤ make test

o bien, ejecutar los tests de forma constante:


    ➤ make watch

    nosetests --with-watch tests.py --rednose --force-color
    ......
    -----------------------------------------------------------------------------
    6 tests run in 0.4 seconds (6 tests passed)
