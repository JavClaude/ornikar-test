from dataclasses import dataclass

from ornikar.src.déploiement.api.payloads.predictions_payload import PredictionPayload


@dataclass
class QuelleEstMaPredictionQuery:
    has_been_proposed_formulas: bool
    has_chosen_formula: bool
    effective_start_date: str
    submitted_at: str
    product_third_party: str
    product_intermediate: str
    product_all_risks: str
    annual_price_third_party: str
    annual_price_intermediate: str
    annual_price_all_risks: str
    main_driver_age: str
    main_driver_gender: str
    main_driver_licence_age: str
    main_driver_bonus: str
    vehicle_age: str
    vehicle_class: str
    vehicle_group: str
    has_secondary_driver: bool

    @classmethod
    def générer_depuis_payload(
        cls, prediction_payload: PredictionPayload
    ) -> "QuelleEstMaPredictionQuery":
        return cls(
            prediction_payload.has_been_proposed_formulas,
            prediction_payload.has_chosen_formula,
            prediction_payload.effective_start_date,
            prediction_payload.submitted_at,
            prediction_payload.product_third_party,
            prediction_payload.product_intermediate,
            prediction_payload.product_all_risks,
            prediction_payload.annual_price_third_party,
            prediction_payload.annual_price_intermediate,
            prediction_payload.annual_price_all_risks,
            prediction_payload.main_driver_age,
            prediction_payload.main_driver_gender,
            prediction_payload.main_driver_licence_age,
            prediction_payload.main_driver_bonus,
            prediction_payload.vehicle_age,
            prediction_payload.vehicle_class,
            prediction_payload.vehicle_group,
            prediction_payload.has_secondary_driver,
        )
