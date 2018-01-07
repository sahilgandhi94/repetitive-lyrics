import sqlite3
import traceback
import zlib
from datetime import datetime

import constants
import logger

log = logger.getLogger('compute-rep')

try:        
    log.info('Connecting to db..')
    conn = sqlite3.connect(constants.DATABASE)
    c = conn.cursor()
    log.info('Connected to db!')
    exceptioncount = 0
    repdump = list()
    for row in c.execute('select * from lyrics'):
        try:
            songid, lyrics = row
            ogbytes = lyrics.encode('utf-8')
            compressedbytes = zlib.compress(ogbytes)
            per = round((len(ogbytes)-len(compressedbytes))/len(ogbytes), 5)
            repdump.append((songid, len(ogbytes), len(compressedbytes), per))
        except Exception:
            exceptioncount+=1
            log.error('Rep compression exception \n{}'.format(traceback.format_exc()))
            log.error('Rep Exception count: {}'.format(exceptioncount))
            continue
    
    log.info('Dumping {} rep data to db..'.format(len(repdump)))
    c.executemany('insert into rep values (?,?,?,?)', repdump)
    conn.commit()
    log.info('Finished dumping rep data to db..')
    
except sqlite3.Error:
    log.error('Sqlite connection error: {}'.format(traceback.format_exc()))
except Exception:
    log.error('Generic error: {}'.format(traceback.format_exc()))
finally:
    conn.close()
