from .base import BaseModel, base_engine
from .models import CompanyStats


def init_db():
    BaseModel.metadata.create_all(bind=base_engine)
