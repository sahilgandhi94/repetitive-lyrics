import zlib

import billboard
import lyricwikia as lw

lyrics = lw.get_lyrics('Ed Sheeran', 'Perfect')

ogbytes = lyrics.encode('utf-8')
compressedbytes = zlib.compress(ogbytes)
decompressed = zlib.decompress(compressedbytes)

print(len(lyrics))
print(len(ogbytes))
print(len(compressedbytes))
print(len(decompressed))
print((len(ogbytes)-len(compressedbytes))/len(ogbytes))
print(ogbytes == decompressed)
# print(lyrics)

def getchart(date=None):
    chart = billboard.ChartData('hot-100')
    for song in chart:
        print(song.__dict__)
        # print(song.artist)
        # print(song.title)
        print('-'*15)
        break

getchart()
