class Song:
    def __init__(self, id: str, name: str, author: str, genre: str):
        self.id = id
        self.name = name
        self.author = author
        self.genre = genre

    def fromCSV(csvString):
        fields = csvString.split(',')
        id = fields[0]
        name = fields[1]
        author = fields[2]
        genre = fields[3].strip()
        return Song(id, name, author, genre)
    
    def toCSV(self):
        return ",".join([self.id, self.name, self.author, self.genre])
    
    def __str__(self):
        return self.toCSV()