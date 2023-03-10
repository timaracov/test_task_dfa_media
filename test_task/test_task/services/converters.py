from test_task.schema import CompanyStatsDTO
from test_task.db.models import CompanyStats


def convert_raw_data_to_company_stats_schema(data: list[tuple]):
    result_schemas = []
    for line in data:
        result_schemas.append(CompanyStatsDTO(*line[1:]))  # exclude id column

    return result_schemas


def convert_company_stats_schema_to_db_models(
    schemas: list[CompanyStatsDTO],
) -> list[CompanyStats]:
    result_models = []
    for schema in schemas:
        result_models.append(CompanyStats(**schema.__dict__))
    return result_models
