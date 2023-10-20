from logging import Logger

from kink import inject

from ornikar.src.entrainement.domain.artefacts_repository_interface import (
    ArtefactRepositoryInterface,
)
from ornikar.src.entrainement.domain.metriques import CalculerLesMetriques
from ornikar.src.entrainement.domain.model_interface import (
    MachineLearningModelInterface,
)
from ornikar.src.entrainement.domain.donnees_repository_interface import (
    DonnéesRepositoryInterface,
)
from ornikar.src.entrainement.domain.preprocesseur import (
    PreprocessingEtFeatureEngineering,
)
from ornikar.src.entrainement.usecases.entrainer_un_modele_command import (
    EntrainerUnModeleCommand,
)


@inject()
class EntrainerUnModeleCommandHandler:
    def __init__(
        self,
        logger: Logger,
        model: MachineLearningModelInterface,
        donnees_repository: DonnéesRepositoryInterface,
        artefact_repository: ArtefactRepositoryInterface,
    ):
        self.logger = logger
        self.model = model
        self.donnees_repository = donnees_repository
        self.artefact_repository = artefact_repository

    def executer_le_cas_d_usage(self, commande: EntrainerUnModeleCommand) -> None:
        self.logger.info("Execution du cas d'usage, entrainer un modèle")
        données_brutes_ornikar = self.donnees_repository.récupérer_les_données_ornikar()
        preprocesseur_de_la_données = PreprocessingEtFeatureEngineering(
            commande.taille_du_test
        )
        (
            X_train,
            X_test,
            y_train,
            y_test,
        ) = preprocesseur_de_la_données.preprocesser_transformer_et_splitter_la_donnee(
            données_brutes_ornikar
        )
        self.model.fit(
            X_train, y_train, "f1", commande.temps_maximum_pour_entrainer_le_modele
        )
        calculer_les_metriques = CalculerLesMetriques()
        metriques = calculer_les_metriques.calculer_le_dictionnaire_des_metriques(
            y_train, y_test, self.model.predict(X_train), self.model.predict(X_test)
        )
        self.artefact_repository.sauvegarder_les_metriques_et_le_modele(
            metriques=metriques, model=self.model
        )
