
import os
import sqlite3
import time
import traceback

import constants
import logger

log = logger.getLogger('resetdb')

if os.path.isfile(constants.DATABASE):
    log.info('Found existing database, renaming it..')
    os.rename(constants.DATABASE, constants.DB_NAME+str(int(time.time()))+constants.EXT)

# create database
try:
    log.info('Creating new db..')
    conn = sqlite3.connect(constants.DATABASE)
    c = conn.cursor()
    c.execute(constants.CREATE_SONGS_TABLE)
    c.execute(constants.CREATE_LYRICS_TABLE)
    c.execute(constants.CREATE_REP_TABLE)
    conn.commit()
    log.info('Successfully created the db and its tables')

except sqlite3.Error:
    log.error('Sqlite connection error: {}'.format(traceback.format_exc()))
except Exception:
    log.error('Generic error: {}'.format(traceback.format_exc()))
finally:
    conn.close()
    log.info('Db connection closed')
