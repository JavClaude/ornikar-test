from abc import abstractmethod
from typing import Dict

from ornikar.src.entrainement import MachineLearningModelInterface


class ArtefactRepositoryInterface:
    @abstractmethod
    def sauvegarder_les_metriques_et_le_modele(
        self, metriques: Dict[str, float], model: MachineLearningModelInterface
    ) -> None:
        pass
