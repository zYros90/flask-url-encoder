SHELL := /bin/bash

init:
	python -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt

tests: unit-tests integration-test

unit-tests:
	source venv/bin/activate
	python -m pytest

integration-test:
	source venv/bin/activate
	python tests_integration.py

performance-test:
	source venv/bin/activate
	python tests_performance.py

docker:
	docker build -t ${REGISTRY}:${TAG} .
