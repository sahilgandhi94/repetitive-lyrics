import logging
from datetime import datetime, timedelta

import billboard

SEPARATOR = '<|=|>'
DATE_LIMIT = datetime.strptime('1958-01-01', '%Y-%m-%d')
CHART_NAME = 'billboard-200'

CORPUS = dict()

# logging setup
logger = logging.getLogger('billboard-charts')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('logs.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

def getchart(name, date):
    ''' Fetches the given chart for the given date and stores in CORPUS '''
    str_date = str(date.date())
    chart = billboard.ChartData(name, date=str_date, fetch=True)
    logger.info("Fetched {} songs".format(len(chart)))
    for song in chart:
        CORPUS.update({song.title+SEPARATOR+song.artist: str_date})


def storecorpus():
    f = open('corpus.txt', 'w')
    for key, value in CORPUS.items():
        print(key+SEPARATOR+value)
        f.write(key+SEPARATOR+value+'\n')
    f.close()

date = datetime.now()
while date >= DATE_LIMIT:
    logger.info("Fetching data for: {}".format(date.date()))
    getchart(CHART_NAME, date)
    logger.info("Size of corpus:    {}".format(len(CORPUS)))
    date = date - timedelta(days=7)
storecorpus()
logger.info('Successfully created corpus.txt file')
