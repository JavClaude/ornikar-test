import pickle
from logging import Logger

import numpy as np
import pandas as pd
from flaml import AutoML
from kink import inject

from ornikar.src.entrainement.domain.model_interface import (
    MachineLearningModelInterface,
)


@inject()
class AutoMLModelImplementation(MachineLearningModelInterface):
    def __init__(self, logger: Logger):
        self.model = AutoML()
        self.logger = logger

    def fit(
        self,
        x_train: pd.DataFrame,
        y_train: pd.DataFrame,
        metrique_a_optimiser: str,
        temps_maximum_pour_entrainer_le_modele: int,
    ) -> None:
        self.logger.info("Entrainement du modèle")
        self.model.fit(
            X_train=x_train,
            y_train=y_train,
            metric=metrique_a_optimiser,
            task="classification",
            time_budget=temps_maximum_pour_entrainer_le_modele,
            verbose=0,
            eval_method="cv",
            early_stop=True,
            seed=42,
        )
        self.logger.info("Score: {}".format(self.model.score(x_train, y_train)))
        self.logger.info(
            "Entrainement du modèle terminé:\n\tEstimator: {}\n\tParametre: {}".format(
                self.model.best_estimator, self.model.best_config
            )
        )

    def predict(self, données_sur_lesquelles_predire: pd.DataFrame) -> np.ndarray:
        return self.model.predict(données_sur_lesquelles_predire)

    @classmethod
    @inject()
    def charger_le_model(
        cls, chemin_ou_est_sauvegardé_le_modele: str, logger: Logger
    ) -> "AutoMLModelImplementation":
        logger.info(
            f"Chargement du modèle d'autoMl depuis: {chemin_ou_est_sauvegardé_le_modele}"
        )
        with open(chemin_ou_est_sauvegardé_le_modele, "rb") as model_artefact:
            auto_ml_model = pickle.load(model_artefact)
        return auto_ml_model
