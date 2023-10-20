import datetime
import os
import pickle
from logging import Logger
from typing import Dict
import json

from kink import inject

from ornikar.src.entrainement import MachineLearningModelInterface
from ornikar.src.entrainement.domain.artefacts_repository_interface import (
    ArtefactRepositoryInterface,
)


@inject()
class ArtefactRepositoryLocalImplementation(ArtefactRepositoryInterface):
    def __init__(self, logger: Logger):
        self.logger = logger
        self.dossier_parent_ou_sauvegarder_les_artefacts = "artefacts_ml"
        self.date_et_heure = datetime.datetime.today().strftime("%Y-%m-%d-%H-%M-%S")
        self.dossier_ou_sauvegarder_les_artefacts = os.path.join(
            self.dossier_parent_ou_sauvegarder_les_artefacts, self.date_et_heure
        )

    def sauvegarder_les_metriques_et_le_modele(
        self, metriques: Dict[str, float], model: MachineLearningModelInterface
    ) -> None:
        self.logger.info("Sauvegarde des artefacts ML")
        self._creer_un_dossier_pour_sauvegarder_les_artefacts()
        self._sauvegarder_les_metriques(
            metriques, self.dossier_ou_sauvegarder_les_artefacts
        )
        self._sauvegarder_le_modele(model, self.dossier_ou_sauvegarder_les_artefacts)

    @staticmethod
    def _sauvegarder_le_modele(
        model: MachineLearningModelInterface, chemin_ou_sauvegarder: str
    ) -> None:
        with open(os.path.join(chemin_ou_sauvegarder, "model.pkl"), "wb") as model_file:
            pickle.dump(model, model_file)

    @staticmethod
    def _sauvegarder_les_metriques(
        metriques: Dict[str, float], chemin_ou_sauvegarder: str
    ) -> None:
        with open(
            os.path.join(chemin_ou_sauvegarder, "metriques.json"), "w"
        ) as metrique_file:
            json.dump(metriques, metrique_file)

    def _creer_un_dossier_pour_sauvegarder_les_artefacts(self):
        if not os.path.exists(self.dossier_parent_ou_sauvegarder_les_artefacts):
            os.mkdir(self.dossier_parent_ou_sauvegarder_les_artefacts)

        nom_du_dossier_a_créer = os.path.join(
            self.dossier_parent_ou_sauvegarder_les_artefacts, self.date_et_heure
        )
        self.logger.info(
            "Création du dossier: {} pour sauvegarder des artefacts".format(
                nom_du_dossier_a_créer
            )
        )
        os.mkdir(self.dossier_ou_sauvegarder_les_artefacts)
