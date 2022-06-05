#!/usr/bin/env make

.DEFAULT_GOAL     := help
.DEFAULT_SHELL    := /bin/bash

POETRY_VERSION    ?= 1.1.13
PACKAGE_NAME      := tenacity-poc

.PHONY: help
help: ## Shows this pretty help screen
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make <target>\n\nTargets:\n"} /^[a-z0-9//_ -]+:.*?##/ { printf " %-15s %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

.PHONY: setup
setup: ## Setup the project for a given python version
	@pip install --quiet poetry==$(POETRY_VERSION)
	@poetry config virtualenvs.create true
	@poetry config virtualenvs.in-project true
	@poetry install

.PHONY: clean
clean: ## Python clean artifacts
	@rm -fr dist/{*.tar.gz,*.whl} server/__pycache__ client/__pycache__

.PHONY: build
build: clean ## Python package build
	@poetry build --verbose

.PHONY: server
server:
	@python -m server &

.PHONY: client
	@python -m client
