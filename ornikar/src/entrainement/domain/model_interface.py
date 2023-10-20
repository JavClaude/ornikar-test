from abc import ABCMeta, abstractmethod

import numpy as np
import pandas as pd


class MachineLearningModelInterface(metaclass=ABCMeta):
    @abstractmethod
    def fit(
        self,
        x_train: pd.DataFrame,
        y_train: pd.DataFrame,
        metrique_a_optimiser: str,
        temps_maximum_pour_entrainer_le_modele: int,
    ) -> None:
        pass

    @abstractmethod
    def predict(self, données_sur_lesquelles_predire: pd.DataFrame) -> np.ndarray:
        pass

    @classmethod
    @abstractmethod
    def charger_le_model(
        cls, chemin_ou_est_sauvegardé_le_modele: str
    ) -> "MachineLearningModelInterface":
        pass
