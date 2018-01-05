from datetime import datetime

# billboard fetch
SEPARATOR = '<|=|>'
DATE_LIMIT = datetime.strptime('1958-01-01', '%Y-%m-%d')
CHART_NAME = 'billboard-200'


# reset db
DB_NAME = 'data'
EXT = '.db'
DATABASE = DB_NAME+EXT

CREATE_SONGS_TABLE = '''
create table songs (
    id integer primary key AUTOINCREMENT,
    title text not null,
    artist text not null,
    date datetime not null
)
'''

CREATE_LYRICS_TABLE = '''
create table lyrics (
    id integer primary key AUTOINCREMENT,
    songid integer not null,
    lyrics text not null,
    foreign key(songid) references song(id)
)
'''

CREATE_REP_TABLE = '''
create table rep (
    id integer primary key AUTOINCREMENT,
    songid integer not null,
    totalbytes integer not null,
    compressedbytes integer not null,
    rep_per integer not null,
    foreign key(songid) references song(id)
)
'''
