#Gustav Kjellberg 951028-2578
#Isak Hassbring 940204-1496

from array import array

from arrayQFile import *
from linkedQFile import *
#Tar en input i form av en string, splittar på mellanslag och gör om varje element till Integer och appendar till listan attayInt
def inputNumbers():
	inputString = (input("Mata in siffrorna: " ))
	arrayString = inputString.split()
	arrayInt = []
	for stringObject in arrayString:
		arrayInt.append(int(stringObject))
	return arrayInt


#Skapar ett objekt inputen från funk ovan, kör algoritmen. 
def run(arrayInt):
	arrayInt = array('i',arrayInt) 
	#inHand = ArrayQFile()
	inHand = linkedQueue()

	for i in arrayInt:
		inHand.enqueue(i)
	while not inHand.isEmpty():
		x = inHand.dequeue()
		inHand.enqueue(x)
		y = inHand.dequeue()
		print(y, end=",")
	else:
		pass





# ordning: 7 1 12 2 8 3 11 4 9 5 13 6 10 