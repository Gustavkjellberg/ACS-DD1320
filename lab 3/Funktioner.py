from binTree import *

"""def putta(newVal, tree):
	#tree = BinTree()        # Skapa ett trädobjekt
	#newVal = "Hej"
	if tree.root == None:
		print(newVal)
		return newVal
	if newVal == tree.root:
		return root
	if newVal < tree.root:
		print("MINDRE ÄN")
		return putta(root.left, newVal)
	if newVal > tree.root:
		print("STÖRRE ÄN")
		return putta(root.right, newVal)
            # Sortera in "gurka" i trädet """

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

#putta("hej")

run()



	#if "gurka" in svenska:     # Kolla om "gurka" finns i trädet
	#    print ("JA")
	 #   return True            # Behövs den??
	#else:
	#    print ("NEJ")
	 #   return False           # Behövs den??

#def skriv():
#svenska = Bintree()        # Skapa ett trädobjekt
#svenska.write()                 # Skriver alla ord i bokstavsordning