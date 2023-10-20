import time
from logging import Logger
from dataclasses import asdict

import pandas as pd
from kink import inject

from ornikar.src.déploiement.api.schemas.predictions_schemas import PredictionSchema
from ornikar.src.déploiement.usecases.quelle_est_la_prediction.quelle_est_ma_prediction_query import (
    QuelleEstMaPredictionQuery,
)
from ornikar.src.entrainement import MachineLearningModelInterface
from ornikar.src.entrainement.domain.preprocesseur_interface import (
    PreprocessingEtFeatureEngineerInterface,
)


@inject()
class QuelleEstLaPrediction:
    def __init__(
        self,
        logger: Logger,
        preprocesseur: PreprocessingEtFeatureEngineerInterface,
        model: MachineLearningModelInterface,
    ):
        self.logger = logger
        self.model = model
        self.preprocesseur = preprocesseur

    def récupérer_une_prediction(
        self, query: QuelleEstMaPredictionQuery
    ) -> PredictionSchema:
        temps_au_debut_de_l_execution_du_cas_d_usage = time.time()
        self.logger.info(
            f"Une query du type 'QuelleEstLaPrediction' avec les paramètres suivants: {asdict(query)} a été demandée"
        )
        query_dataframe = pd.DataFrame(asdict(query), index=[0])
        prediction = self.model.predict(
            self.preprocesseur.preprocesser_et_transformer_la_donnee(query_dataframe)
        )
        temps_a_la_fin_de_l_execution_du_cas_d_usage = time.time()
        self.logger.info(
            "Une demande de prédiction a été traitée en: {} secondes".format(
                temps_a_la_fin_de_l_execution_du_cas_d_usage
                - temps_au_debut_de_l_execution_du_cas_d_usage
            )
        )
        return PredictionSchema(va_souscrire_un_contrat=prediction[0])
