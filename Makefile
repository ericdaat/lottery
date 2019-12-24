venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate

build:
	docker-compose build;

tests:
	. venv/bin/activate; \
	pytest tests;


start:
	docker-compose up -d;

start-debug: venv
	docker-compose up -d postgres metabase;
	. venv/bin/activate; \
	FLASK_APP="application" \
	FLASK_DEBUG=True \
	DATABASE_URL=postgresql://user:password@localhost/webstats \
	flask run;

docs:
	cd docs; \
	make clean; \
	find source/*.rst ! -name 'index.rst' -type f -exec rm -f {} +; \
	sphinx-apidoc ../application -o source -M; \
	sphinx-build source build; \
	echo "done";
