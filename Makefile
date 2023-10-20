.ONESHELL:
.EXPORT_ALL_VARIABLES:
SHELL := /bin/bash

DIR:=$(strip $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST)))))

.DEFAULT_GOAL := help

creer-venv ?= false


.PHONY: help
help: ## provides cli help for this makefile (default) 📖
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

.PHONY: `install-poetry`
install-poetry: ## Installation de poetry: 🐣
	pip install poetry

.PHONY: activer-la-creation-d-un-env-poetry
activer-la-creation-d-un-env-poetry: ## Si poetry ne détecte pas de venv, il va créer un par défaut: ✅ 🏦
	poetry config virtualenvs.create true --local

.PHONY: creer-et-activer-un-environnement-virtuel
creer-et-activer-un-environnement-virtuel: ## Creer et activer un environnement virtuel
	virtualenv .venv; \
	. .venv/bin/activate

.PHONY: desactiver-la-creation-d-un-env-poetry
desactiver-la-creation-d-un-env-poetry: ## Si poetry ne détecte pas de venv, il ne va pas en créer un par défaut: ❌ 🏦
	poetry config virtualenvs.create false --local

.PHONY: installer-les-dependances-de-run
installer-les-dependances-de-run: ## Installation des dépendances de run. param (creer-env=false|true): 💿💻
	@if [ "$(creer-env)" = "false" ]; then \
		make desactiver-la-creation-d-un-env-poetry; \
		poetry install --without dev,exploration; \
	else \
		make creer-et-activer-un-environnement-virtuel; \
		poetry install --without dev,exploration; \
	fi

.PHONY: installer-les-dependances-d-exploration
installer-les-dependances-d-exploration: ## Installation des dépendances d'exploration. param (creer-env=false|true): 💿💻
	@if [ "$(creer-env)" = "false" ]; then \
		make desactiver-la-creation-d-un-env-poetry; \
		poetry install --without dev \
	else \
		make creer-et-activer-un-environnement-virtuel; \
		poetry install --without dev \
	fi

.PHONY: installer-les-dependances-de-dev
installer-les-dependances-de-dev: ## Installation du package et des dependances de développement (linter, tests). param (creer-env=false|true): 💿💄
	@if [ "$(creer-env)" = "false" ]; then \
		make desactiver-la-creation-d-un-env-poetry; \
		poetry install --only dev; \
	else \
		make creer-et-activer-un-environnement-virtuel; \
		poetry install --only dev; \
	fi

.PHONY: `entrainer-le-modele`
entrainer-le-modele: ## Lancer un entrainement du modèle
	entrainer-un-modele --test-size $(test-size) --temps-max-pour-entrainer-le-modele $(temps-maximum)

.PHONY: demarrer-l-api
demarrer-l-api: ## Démarrer l'api de prédiction
	uvicorn ornikar.src.déploiement.api.main:serveur_applicatif --reload

.PHONY: export-des-dependances-au-format-texte
export-des-dependances-au-format-texte: ## export des dépendances au format txt: 📃💻
	poetry export -f requirements.txt --without-hashes --output requirements.txt

.PHONY: verifier-qualite-du-code
verifier-qualite-du-code: ## vérifier la qualité du code8: 🔎
	ruff ornikar

.PHONY: lint-fix
lint-fix: ## fixer les problèmes de conformité avec PEP8: ✨
	ruff ornikar --fix
	black ornikar

.PHONY: test-ornikar
test-ornikar: ## Executer les tests unitaires
	pytest ornikar