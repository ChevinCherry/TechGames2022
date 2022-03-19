from flask import Flask, request
from services import getSongFromDB, writeSongToDB, deleteSongFromDB, getAllSongs, getSongsByActivity
from Song import Song

app = Flask(__name__);

baseRoute = '/songs'

listAllRoute = '/list'

playListRoute = '/playlist'

# Find a song in the DB
@app.route(baseRoute, methods = ['GET'])
def getSong():
    id = request.args.get('id')
    if id == None:
        raise Exception("No ID provided")
    try:
        song = getSongFromDB(id)
    except:
        return "Song could not be found!"
    return song.toCSV()

@app.route(baseRoute, methods = ['POST'])
def createNewSong():
    id = request.args.get('id')
    title = request.args.get('title')
    author = request.args.get('author')
    genre = request.args.get('genre')
    if id == None or title == None or author == None or genre == None:
        raise Exception("Invaid parameters for song!")
    writeSongToDB(Song(id, title, author, genre))
    return "success"

# Delete a song from the DB
@app.route(baseRoute, methods = ['DELETE'])
def deleteSong():
    id = request.args.get('id')
    if id == None:
        raise Exception("No ID provided")
    deleteSongFromDB(id)
    return "success"

@app.route(baseRoute + listAllRoute, methods = ['GET'])
def getAll():
    return getAllSongs()

@app.route(baseRoute + playListRoute, methods=['GET'])
def getPlaylistByActivity():
    activity = request.args.get('activity')
    if activity == None:
        raise Exception("No activity given")
    songs = getSongsByActivity(activity)
    return "\n".join([song.__str__() for song in songs])
    

app.run()