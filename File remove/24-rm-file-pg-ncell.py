from pathlib import Path

import datetime
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

import logging
logging.basicConfig(filename='debug.log', format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

file_location = config['Paths']['file_dir']

try:
    logging.info('Script Started')
    if Path(file_location).exists():
        logging.info(' %s directory',file_location)
        for f in Path(file_location).glob("*.txt"):
            if f.is_file():
                logging.info(' %s removed',f)
                f.unlink()

    logging.info('Script Ended')
except Exception as error:
    logging.error(error)
