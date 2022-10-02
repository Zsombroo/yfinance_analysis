from configparser import ConfigParser
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import DateTime


Base = declarative_base()


def get_config():
    CONFIG_PATH = '/home/{username}/yfinance_analysis/db/db.conf'
    assert os.path.exists(CONFIG_PATH)

    config = ConfigParser()
    config.read(CONFIG_PATH)
    return config


class Value(Base):
    __tablename__ = 'eur_huf'
    Datetime = Column(DateTime, primary_key=True)
    Open = Column(Float)
    High = Column(Float)
    Low = Column(Float)
    Close = Column(Float)

if __name__=='__main__':
    config = get_config()
    engine = create_engine(config['DATABASE']['DBPath'], echo=True)
    Base.metadata.create_all(engine)
