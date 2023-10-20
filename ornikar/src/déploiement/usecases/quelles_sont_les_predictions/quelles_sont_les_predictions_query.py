from dataclasses import dataclass
from typing import List


from ornikar.src.déploiement.api.payloads.predictions_payload import PredictionsPayload


@dataclass
class QuellesSontLesPredictionsQuery:
    has_been_proposed_formulas: List[bool]
    has_chosen_formula: List[bool]
    effective_start_date: List[str]
    submitted_at: List[str]
    product_third_party: List[str]
    product_intermediate: List[str]
    product_all_risks: List[str]
    annual_price_third_party: List[str]
    annual_price_intermediate: List[str]
    annual_price_all_risks: List[str]
    main_driver_age: List[str]
    main_driver_gender: List[str]
    main_driver_licence_age: List[str]
    main_driver_bonus: List[str]
    vehicle_age: List[str]
    vehicle_class: List[str]
    vehicle_group: List[str]
    has_secondary_driver: List[bool]

    @classmethod
    def générer_depuis_payload(cls, predictions_payload: PredictionsPayload):
        return cls(
            predictions_payload.has_been_proposed_formulas,
            predictions_payload.has_chosen_formula,
            predictions_payload.effective_start_date,
            predictions_payload.submitted_at,
            predictions_payload.product_third_party,
            predictions_payload.product_intermediate,
            predictions_payload.product_all_risks,
            predictions_payload.annual_price_third_party,
            predictions_payload.annual_price_intermediate,
            predictions_payload.annual_price_all_risks,
            predictions_payload.main_driver_age,
            predictions_payload.main_driver_gender,
            predictions_payload.main_driver_licence_age,
            predictions_payload.main_driver_bonus,
            predictions_payload.vehicle_age,
            predictions_payload.vehicle_class,
            predictions_payload.vehicle_group,
            predictions_payload.has_secondary_driver,
        )
