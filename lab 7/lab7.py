#Gustav Kjellberg 951028-2578
#Isak Hassbring 940204-1496

########################### Lab7 ###########################

# -----Imports-----############################
import timeit
# -----Classes-----############################

class Song:
	def __init__ (self, id1, id2, name, artist, other = None):
		self.id1 = id1
		self.id2 = id2
		self.name = name
		self.other = other
		self.artist = artist
	def __lt__ (self, other):
		self < self.other
	def getArtist (self, artist):
		return str(self.artist)
	def getDeepData (self):
		return str(self.id1 + " " + self.id2 + " " + " " + self.name + " " + self.artist)

class DictHash:
	def __init__(self, nyckel=None, data=None):
		self.nyckel = nyckel
		self.data = data
		self.dishHash = {}
	def store(self, nyckel, data):
		self.dishHash[str(nyckel)] = data
	def search(self, nyckel):
		if self.dishHash[str(nyckel)]:
			print (nyckel, " finns.")
			return True
		else:
			print (nyckel, " finns inte.")
			#return False

class HashNode(object):
	def __init__ (self, key, data, n):
		self.__nextNode = n
		self.__key = key
		self.__data = data
	def get_nextNode (self):
		return self.__nextNode
	def set_nextNode (self, n):
		self.__nextNode = n
	def getKey (self):
		return str(self.__key)
	def setKey (self, key):
		self.__key = key
	def getData (self):
		return (self.__data)
	def setData (self, data):
		self.__data = data

class LinkedList():
	def __init__ (self, root = None):
		self.root = root
		self.size = 0
	def getSize (self):
		return self.size
	def add (self, key, data):
		newNode = HashNode(key, data, self.root)
		self.root = newNode
		self.size += 1
	def find (self, key):
		cNode = self.root
		while cNode:
			if cNode.getKey() == key:
				return key
			else: 
				cNode = cNode.get_nextNode()
		return None
	def findAndUpdate (self, key, data):
		cNode = self.root
		while cNode:
			if cNode.getKey() == key:
				cNode.setData(data)
				return key
			else: 
				cNode = cNode.get_nextNode()
		return None
	def findAndGet (self, key):
		cNode = self.root
		while not(cNode.get_nextNode()):
			if cNode.getKey() == key:
				return (cNode.getData().getDeepData())
			else: 
				cNode = cNode.get_nextNode()

class Hashtabell:
	def __init__ (self, size, key=None, data=None):
		self.size = size
		self.map = [None] * self.size
	def _get_hash (self, key):
		hash = 0
		for char in str(key):
			hash += (ord(char)*ord(char)*64)//48
		return hash % self.size	
	def put (self, key, data):
		hIndex = self._get_hash(key)	
		spot = self.map[hIndex]
		if spot is None:
			self.map[hIndex] = LinkedList()
			self.map[hIndex].add(key, data)
			#print ("Printar spot", spot.findAndGet(key))
			return True 
		else:
			if spot.findAndUpdate(key, data) == key:
				return True
			self.map[hIndex].add(key, data)
			return True		
	def get (self, key):
		hIndex = self._get_hash(key)
		print(hIndex)
		print(self.map[hIndex])
		if self.map[hIndex]:
			print("\n"+"Om det här skrivs ut, är platsen inte None."+"\n")
			if self.map[hIndex].find(key) == key:
				print("Hejsan")
				return self.map[hIndex].findAndGet(key)
			else:
				print("hejsansvejsan")
				raise KeyError		

#-----Functions-----##########################

def readfile1 (filename):
	songList = []
	songDict = {}
	with open(filename, "r", encoding="utf-8") as songfile:  
		for row in songfile:  
			rowSplit = row.split("<SEP>") 
			id1 = rowSplit[0]
			id2 = rowSplit[1]
			artist = rowSplit[2]
			song = rowSplit[3]
			songObject = Song(id1, id2, song, artist)
			songDict[artist] = songObject
			songList.append(songObject)
	return songList, songDict

def readfile2 (filename):
	songList = []
	songDict = DictHash()
	with open(filename, "r", encoding="utf-8") as songfile:  
		for row in songfile:  
			rowSplit = row.split("<SEP>") 
			id1 = rowSplit[0]
			id2 = rowSplit[1]
			artist = rowSplit[2]
			song = rowSplit[3]
			songObject = Song(id1, id2, song, artist)
			songDict.store(str(artist), songObject)
			songList.append(songObject)
	return songList, songDict

def readfile3 (filename):
	songList = []
	hashtabell = Hashtabell(2000000)
	print("\n\n\n"+"Påbörjar inläsning."+"\n\n\n")
	with open(filename, "r", encoding="utf-8") as songfile:  
		for row in songfile:  
			rowSplit = row.split("<SEP>") 
			id1 = rowSplit[0]
			id2 = rowSplit[1]
			artist = rowSplit[2]
			song = rowSplit[3]
			songObject = Song(id1, id2, song, artist)
			hashtabell.put(artist, songObject)
			songList.append(songObject)
	return songList, hashtabell

def dictGetter():
	print("Startar dictGetter.","\n\n\n")
	filename = "unique_tracks.txt"
	lista, dictionary = readfile3(filename)
	print(len(lista)) #Check så allt är ok.
	return dictionary

def dictSearch (dictionary, key):
	print("\n","Nu körs sökfunktionen","\n")
	#return dictionary.search(key)
	return dictionary.get(key)

# -----Huvudprogram-----########################

x = dictGetter()
print(dictSearch(x, "Emery"))

#-----Tidtagning (Ta bort #)-----################
# dicttid = timeit.timeit(stmt=lambda: dictSearch(x, "Emery"), number=10000)
# dicttid = dicttid/10000
# print("HASH-sökningen tog", round(dicttid, 5), "sekunder")
			