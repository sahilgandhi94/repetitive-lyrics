
import sqlite3
import traceback

import constants
import logger
import lyricwikia as lw
# import lyrics as lw

log = logger.getLogger('fetch-lyrics')

try:
    log.info('Init fetch all lyrics..')
    log.info('Connecting to db..')
    conn = sqlite3.connect(constants.DATABASE)
    c = conn.cursor()
    log.info('Connected to db!')

    lyricsdump = list()
    lyricexceptioncount = 0
    for row in c.execute('select * from songs as s where id not in (select songid from lyrics)'):
        try:
            songid, title, artist, date = row
            lyrics = lw.get_lyrics(artist, title)
            lyricsdump.append((songid, lyrics))
        except Exception:
            lyricexceptioncount+=1
            log.error('Lyrics fetch failed for {}=={} \n{}'.format(title, artist, traceback.format_exc()))
            log.error('Lyric Exception count: {}'.format(lyricexceptioncount))
            continue
    
    if len(lyricsdump) > 0:        
        c.executemany('INSERT INTO lyrics VALUES (?,?)', lyricsdump)
        conn.commit()
        log.info('{} lyrics were dumped in db..'.format(len(lyricsdump)))
    else:
        log.info('Lyrics dump was empty..')

except sqlite3.Error:
    log.error('Sqlite connection error: {}'.format(traceback.format_exc()))
except Exception:
    log.error('Generic error: {}'.format(traceback.format_exc()))
finally:
    conn.close()
