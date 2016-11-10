#Gustav Kjellberg 951028-2578
#Isak Hassbring 940204-1496

#Skapar ett Node objekt som bär data pekar på nästa Node.

from array import array

class Node(object):
	def __init__(self, num, parent):
		self.__num = num
		self.nextNode = None
		self.parent = parent
		#self.__prev = None
		#return self.__num

	def getNum(self):
		return (self.__num)

	def getParent(self):   #rekursion skall användas
		return(self.parent)

	def __str__(self):
		return str(self.__num)

#Skapar en queue. 
class LinkedQ(): 
	def __init__(self):
		self.first = None
		self.last = self.first
		self.length = 0
	def enqueue(self, num, parent):
		newNode = Node(num,parent)
		if self.first == None:
			self.first = newNode
			self.last = newNode
		else:
			self.last.nextNode = newNode
			#newNode.prev = self.last
			self.last = newNode

		self.length += 1
	def dequeue(self):
		if self.first == None:	
			print ("Tom")
		else:
			out = self.first
			self.first = self.first.nextNode
			#self.first.nextNode = self.first.nextNode.nextNode
			
			self.length -= 1
			return (out)

	def peek():
		if not self.isEmpty():
			return self.head.cargo
		else:
			return None
	def isEmpty(self):
		return (self.length) == 0


<Syntax> ::= hej






