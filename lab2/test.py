
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
		#input("!!!" + str(self.length))
		return (self.length) == 0
	#def __repr__(self):
	#	return (Queue())
	#def __str__(self):
	#	return str(Queue)

#def inputNumbers():
#	inputString = (input("Mata in siffrorna: " ))
#	arrayString = inputString.split()

	#arrayInt = []
	#for stringObject in arrayString:
#		arrayInt.append(int(stringObject))
#	return arrayString


#Skapar ett objekt inputen från funk ovan, kör algoritmen. 
#def run():
	#arrayInt = array('i',[3,1,4,2,5]) 
	#onTable = Queue()
	#inHand = linkedQueue()

	#for i in arrayInt:
#		inHand.enqueue(i)
#	while not inHand.isEmpty():
#		x = inHand.dequeue()
#		inHand.enqueue(x)
#		y = inHand.dequeue()
#		print(y, end=",")
#	else:
#		pass
#
#run()

	   # 1 2 ska komma ut
