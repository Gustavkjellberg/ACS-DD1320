class Node:
	def __init__ (self, value, left=None, right=None):
		self.value = value
		self.left = None
		self.right = None

class BinTree:
	def __init__(self, root=None):
		self.root = root



	def put(self, newVal):
		if self.root == None:
			self.root = Node(newVal)
		else:
			self.putta(newVal, self.root)
	def putta(self, newVal, node):
		#if newVal == node.value:
		#	return node
		if newVal < node.value:
			if node.left != None:
				self.putta(newVal, node.left)
			else:
				node.left = Node(newVal)
		if newVal > node.value:
			if node.right != None:
				self.putta(newVal, node.right)
			else: 
				node.right = Node(newVal)

	def __contains__(self, newVal):
		if self.root != None:
			return self.finns(newVal,self.root)
		else:
			return None

	def finns(self, newVal, node):
       # Skapa ett trädobjekt
		if newVal == node.value:
			return True
		elif newVal > node.value and node.right != None:
			return self.finns(newVal, node.right)
		elif newVal < node.value and node.left !=None:
			return self.finns(newVal, node.left)
		else:
			return False


	def write(self):
		if self.root != None:
			self.skriv(self.root)
	def skriv(self, node):
		if node is not None:
			self.skriv(node.left)
			print(node.value)
			self.skriv(node.right)

	def __str__(self):
		return node.value 


tree = BinTree()
tree.put("b")
tree.put("a")
tree.put("d")
tree.put("c")

print ("a" in tree)
tree.write()


