from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from test_task.settings import AppSettings

base_engine = create_engine(AppSettings.DB_URI)
Session = sessionmaker(bind=base_engine)
BaseModel = declarative_base()
