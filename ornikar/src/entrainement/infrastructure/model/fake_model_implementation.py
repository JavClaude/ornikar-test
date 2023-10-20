import pickle
from logging import Logger

import numpy as np
import pandas as pd
from kink import inject

from ornikar.src.entrainement.domain.model_interface import (
    MachineLearningModelInterface,
)


class FakeMLModelImplementation(MachineLearningModelInterface):
    def fit(
        self,
        x_train: pd.DataFrame,
        y_train: pd.DataFrame,
        metrique_a_optimiser: str,
        temps_maximum_pour_entrainer_le_modele: int,
    ) -> None:
        pass

    def predict(self, données_sur_lesquelles_predire: pd.DataFrame) -> np.ndarray:
        # On renvoie True ou False car les données sont encodées comme ça
        return np.random.choice([True, False], size=len(données_sur_lesquelles_predire))

    @classmethod
    @inject()
    def charger_le_model(
        cls, chemin_ou_est_sauvegardé_le_modele: str, logger: Logger
    ) -> "FakeMLModelImplementation":
        logger.info("Chargement du faux modele")
        return FakeMLModelImplementation()
