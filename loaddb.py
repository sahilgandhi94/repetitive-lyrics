
import sqlite3
import traceback
from datetime import datetime

import logger
from constants import *

log = logger.getLogger('load-db')

''' Dumps the corpus into a sqlite db '''
try:        
    log.info('Connecting to db..')
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    log.info('Connectied to db!')

    log.info('Reading corpus file..')
    f = open('corpus.txt', 'r')

    lines = f.readlines()
    dump = list()
    i = 0
    for line in lines:
        title, artist, date = line.split(SEPARATOR)
        date = datetime.strptime(date.strip('\n'), '%Y-%m-%d')
        i+=1 
        dump.append((i, title, artist, date))
    log.info('Created songs dump, now adding all to db..')
    c.executemany('INSERT INTO songs VALUES (?,?,?,?)', dump)
    conn.commit()
    log.info('All songs stored successfully..')
    
except sqlite3.Error:
    log.error('Sqlite connection error: {}'.format(traceback.format_exc()))
except Exception:
    log.error('Generic error: {}'.format(traceback.format_exc()))
finally:
    f.close()
    conn.close()

