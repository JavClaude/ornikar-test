import os
from logging import Logger

from kink import di as conteneur_de_dépendances

from ornikar.src.déploiement.logger.logger import LoggerFactory
from ornikar.src.entrainement import (
    MachineLearningModelInterface,
    AutoMLModelImplementation, FakeMLModelImplementation,
)
from ornikar.src.entrainement.domain.preprocesseur import (
    PreprocessingEtFeatureEngineering,
)
from ornikar.src.entrainement.domain.preprocesseur_interface import (
    PreprocessingEtFeatureEngineerInterface,
)

CHEMIN_VERS_LE_MODELE = os.environ.get("CHEMIN_VERS_LE_MODEL", "")

if CHEMIN_VERS_LE_MODELE:
    conteneur_de_dépendances[MachineLearningModelInterface] = AutoMLModelImplementation.charger_le_model(CHEMIN_VERS_LE_MODELE)
else:
    conteneur_de_dépendances[MachineLearningModelInterface] = FakeMLModelImplementation.charger_le_model(CHEMIN_VERS_LE_MODELE)


conteneur_de_dépendances[Logger] = LoggerFactory.construire_le_logger()

conteneur_de_dépendances[PreprocessingEtFeatureEngineerInterface] = PreprocessingEtFeatureEngineering(None)
