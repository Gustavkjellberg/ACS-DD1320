#Gustav Kjellberg 951028-2578
#Isak Hassbring 940204-1496

#Skapar ett Node objekt som bär data pekar på nästa Node.

from array import array

class Node(object):
	def __init__(self, num, nextNode=None):
		self.__num = num
		self.nextNode = nextNode
		#self.__prev = None
		#return self.__num

	def getNum(self):
		return (self.__num)
	def __str__(self):
		return str(self.__num)

#Skapar en queue. 
class linkedQueue(): 
	def __init__(self):
		self.first = None
		self.last = self.first
		self.length = 0
	def enqueue(self, num):
		newNode = Node(num)
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
			return str(out)
	def isEmpty(self):
		return (self.length) == 0





