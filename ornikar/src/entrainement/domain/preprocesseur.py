from logging import Logger
from typing import List

import pandas as pd
from kink import inject
from sklearn.model_selection import train_test_split

from ornikar.src.entrainement.domain.preprocesseur_interface import (
    PreprocessingEtFeatureEngineerInterface,
)

NOM_DE_LA_COLONNE_CIBLE = "has_subscribed"

NOMBRE_DE_JOURS_DANS_UNE_SEMAINE = 7


@inject()
class PreprocessingEtFeatureEngineering(PreprocessingEtFeatureEngineerInterface):
    def __init__(self, taille_du_test: float, logger: Logger) -> None:
        self.taille_du_test = taille_du_test
        self.logger = logger

    def preprocesser_transformer_et_splitter_la_donnee(
        self, dataframe: pd.DataFrame
    ) -> List[pd.DataFrame]:
        self.logger.info("Execution du preprocessing")
        dataframe = self._calculer_la_difference_en_nombre_de_semaine_entre_la_date_de_completion_du_devis_et_la_date_de_debut_souhaitee_du_contrat(
            dataframe
        )
        dataframe = self._supprimer_les_colonnes_inutiles(dataframe)
        return self._splitter_les_données_en_train_et_test(
            dataframe, self.taille_du_test
        )

    def preprocesser_et_transformer_la_donnee(
        self, dataframe: pd.DataFrame
    ) -> pd.DataFrame:
        return self._calculer_la_difference_en_nombre_de_semaine_entre_la_date_de_completion_du_devis_et_la_date_de_debut_souhaitee_du_contrat(
            dataframe
        )

    def _supprimer_les_colonnes_inutiles(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        colonne_a_supprimer = [
            "lead_id",
            "long_quote_id",
            "policy_subscribed_at",
            "payment_frequency",
            "contract_id",
            "submitted_at",
            "has_subscribed_online",  # A souscrit quoi en ligne ? S'il a deja souscrit, ce n'est pas un lead ?,
            "provider",  # Seulement un souscripteur venait du provider B, pas d'intérêt dans cette variable,
            "effective_start_date",
            "chosen_product",
            "chosen_formula",
            "last_utm_source",
            "vehicle_region",
            "rbs_result",
        ]

        self.logger.info("Suppression des colonnes: {}".format(colonne_a_supprimer))
        return dataframe.drop(columns=colonne_a_supprimer)

    @staticmethod
    def _calculer_la_difference_en_nombre_de_semaine_entre_la_date_de_completion_du_devis_et_la_date_de_debut_souhaitee_du_contrat(
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        dataframe["différence_en_nombre_de_semaine"] = dataframe[
            "effective_start_date"
        ].apply(lambda date: pd.to_datetime(date)) - dataframe["submitted_at"].apply(
            lambda date_au_format_str: pd.to_datetime(
                pd.to_datetime(date_au_format_str).tz_localize(None).date()
            )
        )
        dataframe["différence_en_nombre_de_semaine"] = (
            dataframe["différence_en_nombre_de_semaine"].dt.days
            / NOMBRE_DE_JOURS_DANS_UNE_SEMAINE
        )
        return dataframe

    @staticmethod
    def _splitter_les_données_en_train_et_test(
        dataframe: pd.DataFrame, taille_du_test: float
    ) -> List[pd.DataFrame]:
        return train_test_split(
            dataframe.drop(columns=[NOM_DE_LA_COLONNE_CIBLE]),
            dataframe[NOM_DE_LA_COLONNE_CIBLE],
            stratify=dataframe[NOM_DE_LA_COLONNE_CIBLE],
            test_size=taille_du_test,
            random_state=42,
        )
