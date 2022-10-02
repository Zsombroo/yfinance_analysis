from configparser import ConfigParser
import os
from tabnanny import check

from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
import yfinance as yf


def get_config():
    CONFIG_PATH = '/home/{username}/yfinance_analysis/db/db.conf'
    assert os.path.exists(CONFIG_PATH)

    config = ConfigParser()
    config.read(CONFIG_PATH)
    return config


def fetch_yfinance() -> None:
    ''' Fetch data from Yahoo Finance and upload it to the database
    '''
    config = get_config()
    engine = create_engine(config['DATABASE']['DBPath'], echo=True)
    Base = declarative_base()
    table = Table(config['DATABASE']['Table'], Base.metadata, autoload_with=engine)

    data = yf.download(
        tickers=config['FETCH']['Tickers'],
        period=config['FETCH']['Period'],
        interval=config['FETCH']['Interval'],
    )

    del data['Adj Close']
    del data['Volume']

    with Session(engine) as session:
        for index, row in data.iterrows():
            query = insert(table)\
                .values([index, row.Open, row.High, row.Low, row.Close])\
                .on_conflict_do_nothing()
            session.execute(query)
        session.flush()
        session.commit()


def check_data():
    config = get_config()
    engine = create_engine(config['DATABASE']['DBPath'], echo=True)
    Base = declarative_base()
    table = Table(config['DATABASE']['Table'], Base.metadata, autoload_with=engine)
    with Session(engine) as session:
        query = session.execute(table.select().where(True))
        print(len(query.all()))


if __name__ == '__main__':
    check_data()