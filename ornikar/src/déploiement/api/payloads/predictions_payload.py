from typing import List

from pydantic import BaseModel, Field


class PredictionPayload(BaseModel):
    has_been_proposed_formulas: bool = Field(True)
    has_chosen_formula: bool = Field(False)
    effective_start_date: str = Field("2021-09-01")
    submitted_at: str = Field("2021-09-01 12:29:25 UTC")
    product_third_party: str = Field("third_party_product_24")
    product_intermediate: str = Field("intermdiate_product_23")
    product_all_risks: str = Field("all_risks_product_20")
    annual_price_third_party: str = Field("high")
    annual_price_intermediate: str = Field("high")
    annual_price_all_risks: str = Field("medium")
    main_driver_age: str = Field("18-20")
    main_driver_gender: str = Field("M")
    main_driver_licence_age: str = Field("00")
    main_driver_bonus: str = Field("100")
    vehicle_age: str = Field("15-19")
    vehicle_class: str = Field("I-K")
    vehicle_group: str = Field("29-30")
    has_secondary_driver: bool = Field(False)


class PredictionsPayload(BaseModel):
    has_been_proposed_formulas: List[bool] = Field([True, False])
    has_chosen_formula: List[bool] = Field([False, True])
    effective_start_date: List[str] = Field(["2021-09-01", "2021-09-01"])
    submitted_at: List[str] = Field(
        ["2021-09-01 12:29:25 UTC", "2021-09-01 12:29:25 UTC"]
    )
    product_third_party: List[str] = Field(
        ["third_party_product_24", "third_party_product_24"]
    )
    product_intermediate: List[str] = Field(
        ["intermdiate_product_23", "intermdiate_product_23"]
    )
    product_all_risks: List[str] = Field(
        ["all_risks_product_20", "all_risks_product_20"]
    )
    annual_price_third_party: List[str] = Field(["high", "low"])
    annual_price_intermediate: List[str] = Field(["high", "medium"])
    annual_price_all_risks: List[str] = Field(["medium", "low"])
    main_driver_age: List[str] = Field(["18-20", "18-20"])
    main_driver_gender: List[str] = Field(["M", "M"])
    main_driver_licence_age: List[str] = Field(["00", "00"])
    main_driver_bonus: List[str] = Field(["100", "100"])
    vehicle_age: List[str] = Field(["15-19", "15-19"])
    vehicle_class: List[str] = Field(["I-K", "I-K"])
    vehicle_group: List[str] = Field(["29-30", "29-30"])
    has_secondary_driver: List[bool] = Field([False, False])
