from logging import Logger
from typing import Dict

import pandas as pd
from kink import inject
from sklearn.metrics import f1_score


class CalculerLesMetriques:
    @inject()
    def calculer_le_dictionnaire_des_metriques(
        self,
        y_train: pd.DataFrame,
        y_test: pd.DataFrame,
        predictions_sur_le_train: pd.DataFrame,
        predictions_sur_le_test: pd.DataFrame,
        logger: Logger,
    ) -> Dict[str, float]:
        metrique_sur_le_train = self._calculer_le_f1_score(
            y_train, predictions_sur_le_train
        )
        metrique_sur_le_test = self._calculer_le_f1_score(
            y_test, predictions_sur_le_test
        )

        logger.info(
            "Métriques:\n\ttrain: {}\n\ttest: {}".format(
                metrique_sur_le_train, metrique_sur_le_test
            )
        )

        return {"f1-train": metrique_sur_le_train, "f1-test": metrique_sur_le_test}

    @staticmethod
    def _calculer_le_f1_score(labels: pd.DataFrame, predictions: pd.DataFrame) -> float:
        return f1_score(labels, predictions)
