from dataclasses import dataclass


@dataclass
class CompanyStatsDTO:
    name: str

    fact_qliq_data_1: int
    fact_qliq_data_2: int

    fact_qoil_data_1: int
    fact_qoil_data_2: int

    forecast_qliq_data_1: int
    forecast_qliq_data_2: int

    forecast_qoil_data_1: int
    forecast_qoil_data_2: int
