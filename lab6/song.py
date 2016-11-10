# -----Class-----#

# En klass som representerar en låt. 

class Song:
    def __init__(self, id1, id2, name, artist, other=None):
        self.id1 = id1
        self.id2 = id2
        self.name = name
        # self.other = other
        self.artist = artist

    def __lt__(self, other):
        return self.artist < other

    def getArtist(self):
        return str(self.artist)

    def getSong(self):
        return str(self.name)

    def getData(self):
        return self.id1, self.id2, self.name, self.artist

    # def __str__(self):
    #   return self.id1, self.id2, self.name, self.artist
