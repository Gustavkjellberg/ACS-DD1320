#------------------------------------------------------
# IMPORTS
from binTree import *

#------------------------------------------------------
# DEFINITIONER

def finns(root, newVal):
       # Skapa ett trädobjekt
	if newVal == None:
		print("Nej")
		return False
	if newVal == root.value:
		print("JA")
		return True

	if newVal > root.value:
		return finns(root.right, newVal)
	if newVal < root.value:
		return finns(root.left, newVal)

def skriv(root):

	if root != None:
		skriv(root.left)
		print(root)
		skriv(root.right)


def run():
	tree = BinTree()
	tree.put("Hej")
	tree.put("då")
	tree.put("Isak")
	tree.put("Hassbring")

#------------------------------------------------------
# HUVUDPROGRAM

run()






#------------------------------------------------------
# KLADD


#def skriv():
#svenska = Bintree()        # Skapa ett trädobjekt
#svenska.write()                 # Skriver alla ord i bokstavsordning