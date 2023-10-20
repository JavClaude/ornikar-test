import time
from logging import Logger
from dataclasses import asdict

import pandas as pd
from kink import inject

from ornikar.src.déploiement.api.schemas.predictions_schemas import (
    PredictionSchema,
    PredictionsSchema,
)
from ornikar.src.déploiement.usecases.quelles_sont_les_predictions.quelles_sont_les_predictions_query import (
    QuellesSontLesPredictionsQuery,
)
from ornikar.src.entrainement import MachineLearningModelInterface
from ornikar.src.entrainement.domain.preprocesseur_interface import (
    PreprocessingEtFeatureEngineerInterface,
)


@inject()
class QuellesSontLesPredictions:
    def __init__(
        self,
        logger: Logger,
        preprocesseur: PreprocessingEtFeatureEngineerInterface,
        model: MachineLearningModelInterface,
    ):
        self.logger = logger
        self.model = model
        self.preprocesseur = preprocesseur

    def récupérer_les_predictions(
        self, query: QuellesSontLesPredictionsQuery
    ) -> PredictionsSchema:
        temps_au_debut_de_l_execution_du_cas_d_usage = time.time()
        self.logger.info(
            f"Une query du type 'QuellesSontLesPredictions' avec les paramètres suivants: {asdict(query)} a été demandée"
        )
        query_dataframe = pd.DataFrame(asdict(query))
        predictions = self.model.predict(
            self.preprocesseur.preprocesser_et_transformer_la_donnee(query_dataframe)
        )

        predictions_schema = []
        for prediction in predictions:
            predictions_schema.append(
                PredictionSchema(va_souscrire_un_contrat=prediction)
            )

        temps_a_la_fin_de_l_execution_du_cas_d_usage = time.time()
        self.logger.info(
            "Une demande de prédiction a été traitée en: {} secondes".format(
                temps_a_la_fin_de_l_execution_du_cas_d_usage
                - temps_au_debut_de_l_execution_du_cas_d_usage
            )
        )
        return PredictionsSchema(predictions_schema=predictions_schema)
