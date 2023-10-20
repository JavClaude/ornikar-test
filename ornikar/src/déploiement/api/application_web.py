from fastapi import FastAPI, status

from ornikar.src.déploiement.api.payloads.predictions_payload import (
    PredictionPayload,
    PredictionsPayload,
)
from ornikar.src.déploiement.api.schemas.health_check_schema import HealthCheck
from ornikar.src.déploiement.api.schemas.predictions_schemas import (
    PredictionSchema,
    PredictionsSchema,
)
from ornikar.src.déploiement.usecases.quelle_est_la_prediction.quelle_est_ma_prediction import (
    QuelleEstLaPrediction,
)
from ornikar.src.déploiement.usecases.quelle_est_la_prediction.quelle_est_ma_prediction_query import (
    QuelleEstMaPredictionQuery,
)
from ornikar.src.déploiement.usecases.quelles_sont_les_predictions.quelles_sont_les_predictions import (
    QuellesSontLesPredictions,
)
from ornikar.src.déploiement.usecases.quelles_sont_les_predictions.quelles_sont_les_predictions_query import (
    QuellesSontLesPredictionsQuery,
)


class OrnikarAPI:
    def __init__(self):
        self.application = FastAPI()

    def construire_l_application_web(self) -> FastAPI:
        self._ajouter_la_route_health_check()
        self._ajouter_la_route_de_prediction_du_model()
        self._ajouter_la_route_de_predictions_du_model()
        return self.application

    def _ajouter_la_route_health_check(self) -> None:
        @self.application.get("/health", status_code=status.HTTP_200_OK)
        def health() -> HealthCheck:
            return HealthCheck(status="Up")

    def _ajouter_la_route_de_prediction_du_model(self) -> None:
        @self.application.post("/prediction")
        def obtenir_un_prediction(
            prediction_payload: PredictionPayload,
        ) -> PredictionSchema:
            quelle_est_la_prediction = QuelleEstLaPrediction()
            quelle_est_la_prediction_query = (
                QuelleEstMaPredictionQuery.générer_depuis_payload(prediction_payload)
            )
            return quelle_est_la_prediction.récupérer_une_prediction(
                quelle_est_la_prediction_query
            )

    def _ajouter_la_route_de_predictions_du_model(self) -> None:
        @self.application.post("/predictions")
        def obtenir_des_predictions(
            predictions_payload: PredictionsPayload,
        ) -> PredictionsSchema:
            quelles_sont_les_predictions = QuellesSontLesPredictions()
            quelles_sont_les_predictions_query = (
                QuellesSontLesPredictionsQuery.générer_depuis_payload(
                    predictions_payload
                )
            )
            return quelles_sont_les_predictions.récupérer_les_predictions(
                quelles_sont_les_predictions_query
            )
