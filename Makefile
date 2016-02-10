VERSION=0.0.1               # Se actualiza con make version.
NAME=api-flask-sqlalchemy   # Cambiar al nombre de la aplicación.

N=[0m
G=[01;32m
Y=[01;33m
B=[01;34m

all:
	@echo ""
	@echo "${B}Commands for ${G}${NAME} ${B}v${VERSION}"
	@echo ""
	@echo "  ${Y}For developers ${N}"
	@echo ""
	@echo "    ${G}init${N}         Install all dependencies."
	@echo "    ${G}initdb${N}       Creates the database."
	@echo "    ${G}test${N}         Run tests one time."
	@echo "    ${G}watch${N}        Run tests in a loop."
	@echo ""
	@echo "  ${Y}For ops ${N}"
	@echo ""
	@echo "    ${G}run${N}          Run the webapp."
	@echo ""

init:
	pip install -r requirements.txt

initdb:
	python initdb.py

test:
	nosetests tests.py --rednose --force-color

watch:
	nosetests --with-watch tests.py --rednose --force-color

run:
	python run.py
