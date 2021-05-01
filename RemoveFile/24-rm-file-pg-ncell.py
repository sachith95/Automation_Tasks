from pathlib import Path

import configparser
import logging

# Config parse init
config = configparser.ConfigParser()
config.read('config.ini')

# Log init
logging.basicConfig(filename='debug.log', format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

# Local Variables
file_location = config['Paths']['file_dir']
file_type = config['Types']['file_type']

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
