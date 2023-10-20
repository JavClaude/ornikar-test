from abc import ABCMeta, abstractmethod

import pandas as pd


class DonnéesRepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def récupérer_les_données_ornikar(self) -> pd.DataFrame:
        pass
