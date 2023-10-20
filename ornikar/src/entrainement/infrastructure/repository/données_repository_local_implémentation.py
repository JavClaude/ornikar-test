import pandas as pd

from ornikar.src.entrainement.domain.donnees_repository_interface import (
    DonnéesRepositoryInterface,
)

POSITION_INDEX_COLONNE = 0


class DonnéesRepositoryLocalImplémentation(DonnéesRepositoryInterface):
    def récupérer_les_données_ornikar(self) -> pd.DataFrame:
        return pd.read_csv(
            "donnees_brutes/long_quotes.csv", index_col=POSITION_INDEX_COLONNE
        )
