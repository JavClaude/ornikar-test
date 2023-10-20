# Test technique Ornikar 🚗

Vous trouverez dans ce repository des éléments de réponses pour le test technique d'`Ornikar`

# Installation 🔧

Afin d'installer le projet et les dépendances assurez-vous d'avoir installer (a minima) la version `3.10` de python.
Dans le cas contraire, vous pouvez utiliser `pyenv` et les commandes suivantes pour l'installer.

```shell
brew install pyenv
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
pyenv install 3.10.0
pyenv global 3.10.0 
```

Installer ensuite, le gestionnaire des dépendances `poetry` en utilisant la target make `install-poetry`.

# Utilisation

## Entrainement
Une target make est à votre disposition pour démarrer un entrainement du modèle de ML: `entrainer-le-modele`. Deux paramères sont a renseignés:
    - test-size: float, taille du jeu de test
    - temps-maximum: int, temps maximum pour entrainer le modèle

```shell
make entrainer-le-modele test-size=0.40 temps-maximum=30
```

## Deploiement
Une target make est aussi à votre disposition pour démarrer l'api: `demarrer-l-api`.
Afin de démarrer l'api avec une **vraie** implémentation d'un modèle, merci d'exporter la variable d'environnement suivante:
```
export CHEMIN_VERS_LE_MODEL="<<chemin_vers_le_model.pkl>>"
make demarrer-l-api
```
Si cette variable n'est pas renseignée, alors, un interface de test sera injecté dans l'API.

## Améliorations

Créer un cas d'usage dans entraînement pour preprocesser et transformer la données:
   - Les données pourraient aussi être exportées dans un feature store
   - Appeler ce cas d'usage via un interface dans le domain `déploiement`
