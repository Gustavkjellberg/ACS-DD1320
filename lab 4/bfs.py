
#------------------------------------------------------
# IMPORTS

from binTree import *
from linkedQ import *
from parentNode import *
from klar import *

#------------------------------------------------------
# FUNCTIONS
	
class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

    def getWord(self):
    	return(self.word)
    def getParent(self):
    	return(self.parent)



def makeChildren(nod, endWord=None):
	# Undviker att startWord ter sig som ohittat när det dyker upp i itterationen första gången. 
	startWord = nod.getNum()

	if not startWord in gamla:
		gamla.put(startWord)

	# Skapar en tom lista och läser in det inmatade ordets bokstäver som element.
	letterList = []
	for letter in startWord:
		letterList.append(letter)

	# Ittererar genom alla potentiella ord som går att skapa genom att byta 1 bokstav.
	n = 0
	while n < len(letterList):
		saved_letter = letterList[n]
		for x in "abcdefghijklmnopqrstuvxyzåäö":	# alphabet
			letterList[n] = x						# x = letter in the alphabet
			w = ''.join(letterList) 					# w = possible word
			if w in svenska:
				if not w in gamla:
					print(nod.getNum())
					if w == endWord:						
						Klar()

		letterList[n] = saved_letter
		n += 1






#------------------------------------------------------
# MAIN PROGRAM


# Skapar 2 binärträd, svenska & gamla.
svenska = BinTree()
gamla = BinTree()
q = LinkedQ()


# Läser in ordlistan i binärträdet "svenska".
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
		for rad in svenskfil:
			ordet = rad.strip()						# Ett 3-ord per rad
			if not ordet in svenska:
				svenska.put(ordet)					# in i sökträdet

# Låter användaren mata in stard- och slutord.
startWord = input("Ange startord: ")
endWord = input("Ange slutord: ")

parentNode = ParentNode(startWord)

# Uppgift 1.
#makeChildren(startWord)


#Uppgift 2. För lång nu!!!

q.enqueue(parentNode.getWord(), parentNode.getParent())
while not q.isEmpty():
	#print ("Hejhopp")
	nod = q.dequeue()

	makeChildren(nod, endWord)




# Snyggare output.
print ("\n\n")



