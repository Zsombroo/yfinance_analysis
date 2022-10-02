import time
import os

from configparser import ConfigParser

from db.db_interaction import *


if __name__=='__main__':
    CONFIG_PATH = '/home/{username}/yfinance_analysis/unix_service/yfinance_service.conf'
    assert os.path.exists(CONFIG_PATH)

    config = ConfigParser()
    config.read(CONFIG_PATH)

    fetch_yfinance()
    with open(str(config['DEFAULT']['RunLogPath']), 'a') as f:
        f.write(''.join([str(time.localtime()), '\n']))