import random
from Song import Song

DBFileName = 'songs.csv'

def writeSongToDB(Song: Song):
    DB = open(DBFileName, 'a')
    DB.write(Song.toCSV() + "\n")
    DB.close()

def getSongFromDB(id: str):
    DB = open(DBFileName, 'r')
    for line in DB:
        if (line.startswith(id)):
            DB.close()
            return Song.fromCSV(line)
    DB.close()
    raise Exception("Song not found in DB!")

def deleteSongFromDB(id: str):
    DB = open(DBFileName, 'r')
    allSongs = DB.readlines()
    filteredSongs = [song for song in allSongs if not song.startswith(id)]
    DB.close()
    DB = open(DBFileName, 'w')
    for song in filteredSongs:
        DB.write(song)
    DB.close()

def getAllSongs():
    DB = open(DBFileName, 'r')
    return DB.read()

def getSongsByActivity(activity: str):
    DB = open(DBFileName, 'r')
    activityToGenre = {
        "study": ["lofi", "classical"],
        "workout": ["EDM", "rap"]
    }
    if activity not in activityToGenre:
        raise Exception("Activity not in possible Activities")
    genres = activityToGenre[activity]
    filteredSongs = []
    for line in DB:
        song = Song.fromCSV(line)
        if song.genre in genres:
            filteredSongs.append(song)
    DB.close()
    if (len(filteredSongs) < 10):
        random.shuffle(filteredSongs)
        return filteredSongs
    else:
        playlist = random.choices(filteredSongs, k=10)
        return playlist





if __name__ == "__main__":
    DB = open(DBFileName, 'w')
    DB.close()
    newSong1 = Song('1', 'Hello', 'World', 'Country')
    newSong2 = Song('2', 'Test2', 'TestAuthor', 'EDM')
    writeSongToDB(newSong1)
    writeSongToDB(newSong2)
    print([song.__str__() for song in getAllSongs()])
    deleteSongFromDB('1')
    print([song.__str__() for song in getAllSongs()])
