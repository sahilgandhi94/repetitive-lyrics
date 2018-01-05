
from datetime import datetime, timedelta

import billboard
import logger

SEPARATOR = ':-:'
DATE_LIMIT = datetime.strptime('2017-01-01', '%Y-%m-%d')
CHART_NAME = 'billboard-200'

CORPUS = dict()
log = logger.getLogger('billboard-charts')

def getchart(name, date):
    ''' Fetches the given chart for the given date and stores in CORPUS '''
    str_date = str(date.date())
    chart = billboard.ChartData(name, date=str_date, fetch=True)
    log.debug("Fetched {} songs".format(len(chart)))
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
    log.info("Fetching data for: {}".format(date.date()))
    getchart(CHART_NAME, date)
    log.info("Size of corpus:    {}".format(len(CORPUS)))
    date = date - timedelta(days=7)
storecorpus()
log.info('Successfully created corpus.txt file')
