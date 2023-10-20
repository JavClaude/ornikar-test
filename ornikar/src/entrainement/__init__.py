import os
from logging import Logger

from kink import di as conteneur_de_dependance

from ornikar.src.entrainement.domain.model_interface import (
    MachineLearningModelInterface,
)
from ornikar.src.entrainement.domain.artefacts_repository_interface import (
    ArtefactRepositoryInterface,
)
from ornikar.src.entrainement.domain.donnees_repository_interface import (
    DonnéesRepositoryInterface,
)
from ornikar.src.entrainement.infrastructure.model.automl_model_implementation import (
    AutoMLModelImplementation,
)
from ornikar.src.entrainement.infrastructure.model.fake_model_implementation import (
    FakeMLModelImplementation,
)
from ornikar.src.entrainement.infrastructure.artefacts.artefact_repository_local_implementation import (
    ArtefactRepositoryLocalImplementation,
)
from ornikar.src.entrainement.infrastructure.repository.donnees_repository_cloud_implementation import (
    DonnéesRepositoryCloudImplementation,
)
from ornikar.src.entrainement.infrastructure.repository.données_repository_fake_implémentation import (
    DonnéesRepositoryFakeImplémentation,
)
from ornikar.src.entrainement.infrastructure.repository.données_repository_local_implémentation import (
    DonnéesRepositoryLocalImplémentation,
)
from ornikar.src.entrainement.logger.logger import LoggerFactory

import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)
conteneur_de_dependance[Logger] = LoggerFactory.construire_le_logger()

EXECUTION_SUR_LE_CLOUD = os.environ.get("EST_EXECUTE_SUR_LE_CLOUD", "")
EXECUTION_DES_TU = os.environ.get("EST_EXECUTE_PAR_UN_TU", "")

if EXECUTION_SUR_LE_CLOUD:
    conteneur_de_dependance[
        DonnéesRepositoryInterface
    ] = DonnéesRepositoryCloudImplementation()
    conteneur_de_dependance[MachineLearningModelInterface] = AutoMLModelImplementation()
elif EXECUTION_DES_TU:
    conteneur_de_dependance[
        DonnéesRepositoryInterface
    ] = DonnéesRepositoryFakeImplémentation()
    conteneur_de_dependance[MachineLearningModelInterface] = FakeMLModelImplementation()
else:
    conteneur_de_dependance[
        DonnéesRepositoryInterface
    ] = DonnéesRepositoryLocalImplémentation()
    conteneur_de_dependance[MachineLearningModelInterface] = AutoMLModelImplementation()
    conteneur_de_dependance[
        ArtefactRepositoryInterface
    ] = ArtefactRepositoryLocalImplementation()
