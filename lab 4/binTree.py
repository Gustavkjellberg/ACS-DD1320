class Node:
	def __init__ (self, value, left=None, right=None):
		self.value = value
		self.left = None
		self.right = None

	def skriv(self, node):
		if node:
			self.skriv(node.left)
			print(node.value)
			self.skriv(node.right)
		else: 
			pass

class BinTree:
	def __init__(self, root=None):
		self.root = root

	def put(self, newVal):
		if self.root:
			self.putta(newVal, self.root)
		else:
			self.root = Node(newVal)


	def putta(self, newVal, node): # borde heta add
		#if newVal == node.value:
		#	return node
		if newVal < node.value:
			if node.left:
				self.putta(newVal, node.left)
			else:
				node.left = Node(newVal)
		if newVal > node.value:
			if node.right:
				self.putta(newVal, node.right)
			else: 
				node.right = Node(newVal)


	def __contains__(self, newVal):
		if self.root:
			return self.finns(newVal,self.root)
		else:
			return None

	def finns(self, newVal, node):
       # Skapa ett trädobjekt
		if newVal == node.value:
			return True
		elif newVal > node.value and node.right:
			return self.finns(newVal, node.right)
		elif newVal < node.value and node.left:
			return self.finns(newVal, node.left)
		else:
			return False


	def write(self):
		if self.root:
			self.skriv(self.root)
		else: 
			pass


	def __str__(self):
		return node.value 


tree = BinTree()
# tree.put("a")
# tree.put("b")
# tree.put("q")
# tree.put("d")
# print ("a" in tree)
tree.write()


