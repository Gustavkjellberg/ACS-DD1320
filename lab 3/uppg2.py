from binTree import *
svenska = BinTree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
	for rad in svenskfil:
		ordet = rad.strip()				# Ett trebokstavsord per rad
		if ordet in svenska:
			print(ordet, end = " ") 
		else:
			svenska.put(ordet)             # in i sökträdet
print("\n")




engelska = BinTree()
usedWords = BinTree()
with open("engelska.txt", "r", encoding = "utf-8") as engelskafil:
	for row in engelskafil:
		row = row.split()
		for word in row:
			if  not word in engelska:
				if word in svenska:
					if not word in usedWords:
						usedWords.put(word)
						print(word, end = " ")
				else:
					#print(word)
					engelska.put(word)
print("\n")
