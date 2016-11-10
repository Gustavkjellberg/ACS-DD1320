#Gustav Kjellberg 951028-2578
#Isak Hassbring 940204-1496
from array import array
#Bildar objekt i form utav en lista och använder sig utav de inbyggda funktoinerna append och pop. Använder sig också av det privata attributet __num.
class ArrayQFile():	
	def __init__(self, num= None):
		if num == None:
			self.__num = array('i')
		else:
			self.__num = array(num)	
	def enqueue(self, num=0):
		self.__num.append(num)
	def dequeue(self):
	 	return self.__num.pop(0)
	def isEmpty(self):
	 	 	return len(self.__num) == 0