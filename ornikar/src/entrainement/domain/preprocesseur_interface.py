from abc import ABCMeta, abstractmethod
from typing import List

import pandas as pd


class PreprocessingEtFeatureEngineerInterface(metaclass=ABCMeta):
    @abstractmethod
    def preprocesser_transformer_et_splitter_la_donnee(
        self, dataframe: pd.DataFrame
    ) -> List[pd.DataFrame]:
        pass

    @abstractmethod
    def preprocesser_et_transformer_la_donnee(
        self, dataframe: pd.DataFrame
    ) -> pd.DataFrame:
        pass
