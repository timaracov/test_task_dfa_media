from test_task.db.base import Session
from test_task.db.models import CompanyStats


class CompanyStatsFacade:
    def __init__(self):
        self.__data = []

    def from_spreadsheet_file(self, filename: str):
        from test_task.services import readers

        self.__data = readers.read_spreadsheet_file(filename)

    def add_to_db(self):
        if not self.__data:
            return

        with Session() as sess:
            try:
                for model in self.__prep_data_for_db(self.__data):
                    sess.add(model)
                sess.commit()
            except:
                sess.rollback()
                raise

    def get_total_qliq(self):
        with Session() as sess:
            try:
                data = (
                    sess.query(
                        CompanyStats.fact_qliq_data_1
                        + CompanyStats.fact_qliq_data_2
                        + CompanyStats.forecast_qliq_data_1
                        + CompanyStats.forecast_qliq_data_2,
                        CompanyStats.date,
                    )
                    .order_by(CompanyStats.date)
                    .all()
                )
            except:
                sess.rollback()
                raise

        return data

    def get_total_qoil(self):
        with Session() as sess:
            try:
                data = (
                    sess.query(
                        CompanyStats.fact_qoil_data_1
                        + CompanyStats.fact_qoil_data_2
                        + CompanyStats.forecast_qoil_data_1
                        + CompanyStats.forecast_qoil_data_2,
                        CompanyStats.date,
                    )
                    .order_by(CompanyStats.date)
                    .all()
                )
            except:
                sess.rollback()
                raise

        return data

    def __prep_data_for_db(self, data):
        from test_task.services import converters

        return converters.convert_company_stats_schema_to_db_models(
            converters.convert_raw_data_to_company_stats_schema(data)
        )
