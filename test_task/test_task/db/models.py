import datetime as dt

import sqlalchemy as sa

from .base import BaseModel


class CompanyStats(BaseModel):
    __tablename__ = "company_stats"
    __table_args__ = {"extend_existing": True}

    id = sa.Column(sa.Integer, primary_key=True, unique=True, autoincrement=True)
    name = sa.Column(sa.String(100))

    fact_qliq_data_1 = sa.Column(sa.Integer)
    fact_qliq_data_2 = sa.Column(sa.Integer)

    fact_qoil_data_1 = sa.Column(sa.Integer)
    fact_qoil_data_2 = sa.Column(sa.Integer)

    forecast_qliq_data_1 = sa.Column(sa.Integer)
    forecast_qliq_data_2 = sa.Column(sa.Integer)

    forecast_qoil_data_1 = sa.Column(sa.Integer)
    forecast_qoil_data_2 = sa.Column(sa.Integer)

    date = sa.Column(sa.DateTime, default=dt.datetime.now)
