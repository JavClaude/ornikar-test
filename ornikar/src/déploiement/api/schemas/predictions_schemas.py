from typing import List

from pydantic import BaseModel


class PredictionSchema(BaseModel):
    va_souscrire_un_contrat: bool


class PredictionsSchema(BaseModel):
    predictions_schema: List[PredictionSchema]
