import pandas as pd

from ornikar.src.entrainement.domain.donnees_repository_interface import (
    DonnéesRepositoryInterface,
)

POSITION_INDEX_COLONNE = 0


class DonnéesRepositoryFakeImplémentation(DonnéesRepositoryInterface):
    def récupérer_les_données_ornikar(self) -> pd.DataFrame:
        return pd.read_json(
            """{"long_quote_id": {"70": -7688437865327979005, "569": -8120234105282979695, "460": -887161821350947888, "618": 7319385412406047764},
             "lead_id": {"70": 342186110025012641, "569": 7110297380935034227, "460": 4358159438772750290, "618": 7809957895787116834},
             "last_utm_source": {"70": null, "569": null, "460": null, "618": null},
             "has_been_proposed_formulas": {"70": false, "569": true, "460": true, "618": true},
             "has_chosen_formula": {"70": false, "569": false, "460": false, "618": false},
             "has_subscribed_online": {"70": false, "569": false, "460": false, "618": false},
             "submitted_at": {"70": "2021-09-01 11:19:51 UTC", "569": "2021-09-01 08:51:55 UTC", "460": "2021-09-01 19:34:40 UTC",
             "618": "2021-09-01 17:56:23 UTC"},
             "effective_start_date": {"70": "2021-09-01", "569": "2021-09-02", "460": "2021-09-07", "618": "2021-09-08"},
             "rbs_result": {"70": null, "569": null, "460": null, "618": null},
             "provider": {"70": null, "569": "provider_A", "460": "provider_A", "618": "provider_A"},
             "product_third_party": {"70": null, "569": "third_party_product_4", "460": "third_party_product_4", "618": "third_party_product_4"},
             "product_intermediate": {"70": null, "569": "intermdiate_product_5", "460": "intermdiate_product_5", "618": "intermdiate_product_5"},
             "product_all_risks": {"70": null, "569": "all_risks_product_5", "460": "all_risks_product_5", "618": "all_risks_product_5"},
             "annual_price_third_party": {"70": null, "569": "high", "460": "low", "618": "medium"},
             "annual_price_intermediate": {"70": null, "569": "high", "460": "low", "618": "medium"},
             "annual_price_all_risks": {"70": null, "569": "high", "460": "low", "618": "low"},
             "chosen_formula": {"70": null, "569": null, "460": null, "618": null},
             "chosen_product": {"70": null, "569": null, "460": null, "618": null},
             "policy_subscribed_at": {"70": null, "569": null, "460": null, "618": null},
             "contract_id": {"70": null, "569": null, "460": null, "618": null},
             "payment_frequency": {"70": null, "569": null, "460": null, "618": null},
             "main_driver_age": {"70": "25-29", "569": "18-20", "460": "18-20", "618": "25-29"},
             "main_driver_gender": {"70": "M", "569": "M", "460": "F", "618": "M"},
             "main_driver_licence_age": {"70": 10.5, "569": 0.0, "460": 1.0, "618": 10.5},
             "main_driver_bonus": {"70": "100", "569": "100", "460": "100", "618": "100"},
             "vehicle_age": {"70": "15-19", "569": "06-09", "460": "10-14", "618": "15-19"},
             "vehicle_class": {"70": "O-R", "569": "I-K", "460": "F-H", "618": "F-H"},
             "vehicle_group": {"70": "35+", "569": "29-30", "460": "27-28", "618": "29-30"},
             "vehicle_region": {"70": "Ile-De-France", "569": "Provence-Alpes-Cote D\'azur", "460": "Pays De La Loire", "618": "Haute-Normandie"},
             "has_secondary_driver": {"70": false, "569": false, "460": false, "618": false},
             "has_subscribed": {"70": false, "569": false, "460": false, "618": false},
             "diff\\u00e9rence_en_nombre_de_semaine": {"70": 0.0, "569": 0.1428571429, "460": 0.8571428571, "618": 1.0}}""",
        )
