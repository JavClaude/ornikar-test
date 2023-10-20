from typing import Dict

from ornikar.src.entrainement import MachineLearningModelInterface
from ornikar.src.entrainement.domain.artefacts_repository_interface import (
    ArtefactRepositoryInterface,
)


class ArtefactRepositoryCloudImplementation(ArtefactRepositoryInterface):
    def sauvegarder_les_metriques_et_le_modele(
        self, metriques: Dict[str, float], model: MachineLearningModelInterface
    ) -> None:
        # Vertex, Cloud storage.....
        pass
