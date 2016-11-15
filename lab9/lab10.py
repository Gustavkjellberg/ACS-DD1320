#Gustav Kjellberg 951028-2578
#Isak Hassbring  940204-1496
import re
import sys
import unittest
from molgrafik import *
from array import array

#Ingen parantes
#def weight(mol):
 #   if ingen parentes
  #  hashtabell.get(mol)
   #      else if parentes:
    #    gånga samma


class HashNode(object):
    def __init__ (self, key, data, n):
        self.__nextNode = n
        self.__key = key
        self.__data = data
    def get_nextNode (self):
        return self.__nextNode
    def set_nextNode (self, n):
        self.__nextNode = n
    def getKey (self):
        return str(self.__key)
    def setKey (self, key):
        self.__key = key
    def getData (self):
        return (self.__data)
    def setData (self, data):
        self.__data = data

class LinkedList():
    def __init__ (self, root = None):
        self.root = root
        self.size = 0
    def getSize (self):
        return self.size
    def add (self, key, data):
        newNode = HashNode(key, data, self.root)
        self.root = newNode
        self.size += 1
    def find (self, key):
        cNode = self.root
        while cNode:
            if cNode.getKey() == key:
                return key
            else:
                cNode = cNode.get_nextNode()
        return None
    def findAndUpdate (self, key, data):
        cNode = self.root
        while cNode:
            if cNode.getKey() == key:
                cNode.setData(data)
                return key
            else:
                cNode = cNode.get_nextNode()
        return None
    def findAndGet (self, key):
        cNode = self.root
        while cNode:
            if cNode.getKey() == key:
                return (cNode.getData().getDeepData())
            else:
                cNode = cNode.get_nextNode()
        return None

class Hashtabell:
    def __init__ (self, size, key=None, data=None):
        self.size = size
        self.map = [None] * self.size
    def _get_hash (self, key):
        hash = 0
        for char in str(key):
            hash += (ord(char)*ord(char)*64)//48
        return hash % self.size
    def put (self, key, data):
        hIndex = self._get_hash(key)
        spot = self.map[hIndex]
        if spot is None:
            self.map[hIndex] = LinkedList()
            self.map[hIndex].add(key, data)
            #print ("Printar spot", spot.findAndGet(key))
            return True
        else:
            if spot.findAndUpdate(key, data) == key:
                return True
            self.map[hIndex].add(key, data)
            return True
    def get (self, key):
        hIndex = self._get_hash(key)
        # print(hIndex)
        # print(self.map[hIndex])
        if self.map[hIndex]:
            if self.map[hIndex].find(key) == key:
                x = self.map[hIndex].findAndGet(key)
                if x:
                    return x
            else:
                raise KeyError
        raise KeyError

class Atom:
    def __init__(self, namn, vikt):
        self.namn = namn
        self.vikt = vikt
    def getKey (self):
        return str(self.namn)
    def setKey (self, key):
        self.namn = namn
    def getDeepData (self):
        return (self.vikt)
    def setData (self, data):
        self.vikt = vikt

    def __str__(self):
        return "{" + self.namn + " " +  str(self.vikt) + "}"

def skapaAtomlista(): #Returnerar en lista med atomernas namn och vikt
    data = "H  1.00794;\
He 4.002602;\
Li 6.941;\
Be 9.012182;\
B  10.811;\
C  12.0107;\
N  14.0067;\
O  15.9994;\
F  18.9984032;\
Ne 20.1797;\
Na 22.98976928;\
Mg 24.3050;\
Al 26.9815386;\
Si 28.0855;\
P  30.973762;\
S  32.065;\
Cl 35.453;\
K  39.0983;\
Ar 39.948;\
Ca 40.078;\
Sc 44.955912;\
Ti 47.867;\
V  50.9415;\
Cr 51.9961;\
Mn 54.938045;\
Fe 55.845;\
Ni 58.6934;\
Co 58.933195;\
Cu 63.546;\
Zn 65.38;\
Ga 69.723;\
Ge 72.64;\
As 74.92160;\
Se 78.96;\
Br 79.904;\
Kr 83.798;\
Rb 85.4678;\
Sr 87.62;\
Y  88.90585;\
Zr 91.224;\
Nb 92.90638;\
Mo 95.96;\
Tc 98;\
Ru 101.07;\
Rh 102.90550;\
Pd 106.42;\
Ag 107.8682;\
Cd 112.411;\
In 114.818;\
Sn 118.710;\
Sb 121.760;\
I  126.90447;\
Te 127.60;\
Xe 131.293;\
Cs 132.9054519;\
Ba 137.327;\
La 138.90547;\
Ce 140.116;\
Pr 140.90765;\
Nd 144.242;\
Pm 145;\
Sm 150.36;\
Eu 151.964;\
Gd 157.25;\
Tb 158.92535;\
Dy 162.500;\
Ho 164.93032;\
Er 167.259;\
Tm 168.93421;\
Yb 173.054;\
Lu 174.9668;\
Hf 178.49;\
Ta 180.94788;\
W  183.84;\
Re 186.207;\
Os 190.23;\
Ir 192.217;\
Pt 195.084;\
Au 196.966569;\
Hg 200.59;\
Tl 204.3833;\
Pb 207.2;\
Bi 208.98040;\
Po 209;\
At 210;\
Rn 222;\
Fr 223;\
Ra 226;\
Ac 227;\
Pa 231.03588;\
Th 232.03806;\
Np 237;\
U  238.02891;\
Am 243;\
Pu 244;\
Cm 247;\
Bk 247;\
Cf 251;\
Es 252;\
Fm 257;\
Md 258;\
No 259;\
Lr 262;\
Rf 265;\
Db 268;\
Hs 270;\
Sg 271;\
Bh 272;\
Mt 276;\
Rg 280;\
Ds 281;\
Cn 285"
    atomlista = data.split(";")
    return atomlista

def lagraHashtabell(atomlista): # Lagrar atomlistans element i en hashtabell
    antalElement = len(atomlista)
    hashtabell = Hashtabell(antalElement)
    for element in atomlista:
        namn, vikt = element.split()
        nyAtom = Atom(namn, float(vikt))
        hashtabell.put(namn, nyAtom)
    return hashtabell

atomlista = skapaAtomlista()
hashtabell = lagraHashtabell(atomlista)


class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent
    def getParent(self):
        return self.parent
    def getWord(self):
        return self.word


class Node(object):
    def __init__(self, num, nextNode=None):
        self.__num = num
        self.nextNode = nextNode
    #self.__prev = None
    #return self.__num

    def getNum(self):
        return str(self.__num)
    def __str__(self):
        return str(self.__num)

#Skapar en queue.
class LinkedQ:
    def __init__(self):
        self.first = None
        self.last = self.first
        self.length = 0

    def enqueue(self, num):
        newNode = Node(num)
        if self.first is None:
            self.first = newNode
            self.last = newNode
        else:
            self.last.nextNode = newNode
            self.last = newNode
        self.length += 1

    def dequeue(self):
        if self.first:
            out = self.first.getNum()
            self.first = self.first.nextNode
            self.length -= 1
            return out
    def peek(self):
        # type: () -> object
        if not self.isEmpty():
            return self.first.getNum()
        else:
            return None
    def isEmpty(self):
        return self.length == 0


class Syntaxfel(Exception):
    pass



def qRest(q):
    x = ' vid radslutet'
    if not q.isEmpty():
        x = x + ' '
    while not q.isEmpty():
        x = x + q.dequeue()
    return x

#Skapar kö
def createQueue(molecule):
    q = LinkedQ()
    for part in molecule:
        q.enqueue(part)
    return q

def checkAtom(atom, q):
    atoms = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']
    if atom in atoms:
        return
    else:
        raise Syntaxfel('Okänd atom' + qRest(q))


def checkNumber(q, letter, upperCase, lowerCase, number29, number19, number09, weight):
    num = q.dequeue()
    if number19.match(num):
        if q.peek():
            if number09.match(q.peek()):
                num =  numIterator(q, number09, num)
                return num
            else:
                if number29.match(num):
                    return num
        else:
            if number29.match(num):
                return num
    raise Syntaxfel("För litet tal" + qRest(q))

def nextSignInside(q, letter, upperCase, lowerCase, number29, number19, number09, weight):
    if q.peek():
        if number09.match(q.peek()):
            num = checkNumber(q, letter, upperCase, lowerCase, number29, number19, number09, weight)
            return num
    return readGroup(q, letter, upperCase, lowerCase, number29, number19, number09, weight)
    #return

def nextSign(q, letter, upperCase, lowerCase, number29, number19, number09, weight):
    if q.peek():
        if number09.match(q.peek()):
            num = checkNumber(q, letter, upperCase, lowerCase, number29, number19, number09, weight)
            return num
            #return readFormel(q, letter, upperCase, lowerCase, number29, number19, number09, weight)
    else:
        return None

def readFormel(q, letter, upperCase, lowerCase, number29, number19, number09, weight):
    #om det är en boktav
    ruta = Ruta()
    if q.peek():
        if letter.match(q.peek()):
            x, y = readMol(q, letter, upperCase, lowerCase, number29, number19, number09, weight)
            ruta.atom = x
            weight += hashtabell.get(ruta.atom)
            if y:
                ruta.num = int(y)
                weight= weight*int(y)
            if q.peek() == None:
                return ruta, weight
            ruta.next, weight = readFormel(q, letter, upperCase, lowerCase, number29, number19, number09, weight)
        #elif q.peek() == ')':
         #   print('')

        elif q.peek() == '(':
            openingP = q.dequeue()
            if q.peek() == ')':
                #return readGroup(q, letter, upperCase, lowerCase, number29, number19, number09)
                readFormel(q, letter, upperCase, lowerCase, number29, number19, number09, weight)
            else:
                ruta.down, numP, inW = readGroup(q, letter, upperCase, lowerCase, number29, number19, number09, 0)
                weight += inW
                if numP:
                    ruta.num = int(numP)
                if q.peek():
                    ruta.next, weight = readFormel(q, letter, upperCase, lowerCase, number29, number19, number09, weight)
                return ruta, weight
        else:
            raise Syntaxfel('Felaktig gruppstart' + qRest(q))
    return ruta, weight

def readMol(q, letter, upperCase, lowerCase, number29, number19, number09, weight):
    if upperCase.match(q.peek()):
        firstLetter = q.dequeue()
        if q.peek():
            if letter.match(q.peek()):
                if lowerCase.match(q.peek()):
                    sndLetter = q.dequeue()
                    checkAtom(firstLetter + sndLetter, q)

                    y = nextSign(q, letter, upperCase, lowerCase, number29, number19, number09, weight)
                    return firstLetter+sndLetter, y
            checkAtom(firstLetter, q)
            y = nextSign(q, letter, upperCase, lowerCase, number29, number19, number09, weight)
            return firstLetter, y
        else:
            checkAtom(firstLetter, q)
            #readFormel(q, letter, upperCase, lowerCase, number29, number19, number09)
            return firstLetter, None
    else:
        raise Syntaxfel('Saknad stor bokstav' + qRest(q))


def readMolInside(q, letter, upperCase, lowerCase, number29, number19, number09, weight):
    if upperCase.match(q.peek()):
        firstLetter = q.dequeue()
        if q.peek():
            if letter.match(q.peek()):
                if lowerCase.match(q.peek()):
                    sndLetter = q.dequeue()
                    checkAtom(firstLetter + sndLetter, q)
                    mol = firstLetter+ sndLetter
                    if q.peek():
                        if number09.match(q.peek()):
                            y = checkNumber(q, letter, upperCase, lowerCase, number29, number19, number09, weight)
                        else:
                            y = None
                    else:
                        y = None
                    #y = nextSignInside(q, letter, upperCase, lowerCase, number29, number19, number09)
                    return mol, y
            checkAtom(firstLetter, q)
            #y = nextSignInside(q, letter, upperCase, lowerCase, number29, number19, number09)
            if number09.match(q.peek()):
                y = checkNumber(q, letter, upperCase, lowerCase, number29, number19, number09, weight)
            else:
                y = None
            return firstLetter, y
        else:
            checkAtom(firstLetter, q)
            if number09.match(q.peek()):
                y = checkNumber(q, letter, upperCase, lowerCase, number29, number19, number09, weight)
            else:
                y = None
            #y = nextSignInside(q, letter, upperCase, lowerCase, number29, number19, number09)
            return firstLetter, y
    else:
        raise Syntaxfel('Saknad stor bokstav' + qRest(q))





def numIterator(q, number09, num):
    if q.peek():

        if number09.match(q.peek()):
            num += q.dequeue()
            numIterator(q, number09, num)
    return num


    #om siffra kolla att den är stor nog




def checkNumberAfterP(q, letter, upperCase, lowerCase, number29, number19, number09, weight):
    if q.peek():
        if number09.match(q.peek()):
            return checkNumber(q, letter, upperCase, lowerCase, number29, number19, number09, weight)
    raise Syntaxfel('Saknad siffra' + qRest(q))

def readGroup(q, letter, upperCase, lowerCase, number29, number19, number09, weight):
    #sålänge det finns ngt i kön och ingen ) har kommit forsätt, blir kön tom skriv sknad höger
    #om det kommer ( anropa read group) igen
    #Kommer en ) returna True
    ruta= Ruta()
    while q.peek() is not None:
        if q.peek() == "(":
            q.dequeue()
            if upperCase.match(q.peek()):
                #readGroup(q, letter, upperCase, lowerCase, number29, number19, number09)
                ruta.down, num, inW = readGroup(q, letter, upperCase, lowerCase, number29, number19, number09, 0)
                weight += inW
                if num:
                    ruta.num = int(num)
                skit, num, weight = readGroup(q, letter, upperCase, lowerCase, number29, number19, number09, weight)
                return ruta, num, weight
            else:
                if q.peek() == ')':
                    num = checkNumberAfterP(q, letter, upperCase, lowerCase, number29, number19, number09, weight)
                    return ruta, num, weight
                else:
                    weight += hashtabell.get()
                    ruta.next = readFormel(q, letter, upperCase, lowerCase, number29, number19, number09, weight)
        elif q.peek() == ")":

            q.dequeue()
            #if q.peek():
            #return checkNumberAfterP(q, letter, upperCase, lowerCase, number29, number19, number09)
            num =  checkNumberAfterP(q, letter, upperCase, lowerCase, number29, number19, number09, weight)
            return ruta, num, weight*float(num)

            #else:
            #   return
            #readGroup(q, letter, upperCase, lowerCase, number29, number19, number09)
        #elif upperCase.match(q.peek()):
        else:
            mol, num = readMolInside(q, letter, upperCase, lowerCase, number29, number19, number09, weight)
            ruta.atom = mol
            weight += hashtabell.get(ruta.atom)
            if num:
                ruta.num = int(num)
                weight = weight*float(num)
            if q.peek():

                if not q.peek() == ")":
                    ruta.next, num, weight = readGroup(q, letter, upperCase, lowerCase, number29, number19, number09, weight)
                    return ruta, num, weight
                else:
                    mol, num, weight = readGroup(q, letter, upperCase, lowerCase, number29, number19, number09, weight)
            return ruta, num, weight


    if q.isEmpty():
        raise Syntaxfel("Saknad högerparentes" + qRest(q))

#def weight(mol):
 #   vikt = 0




#Rekursiv medåkning
def initializer(molecule):
    # type: (object) -> object
    q = createQueue(molecule)
    letter = re.compile('[A-Za-z]')
    upperCase = re.compile('[A-Z]')
    lowerCase = re.compile('[a-z]')
    number29 = re.compile('[2-9]')
    number19 = re.compile('[1-9]')
    number09 = re.compile('[0-9]')
    weight = 0
    ruta, weight = readFormel(q, letter, upperCase, lowerCase, number29, number19, number09, weight)
    print(weight)
    return ruta



class TestMethods(unittest.TestCase):
    def test_main3(self):
        self.assertEqual(main3('Na'), 'Formeln är syntaktiskt korrekt')
        self.assertEqual(main3('H2O'), 'Formeln är syntaktiskt korrekt')
        self.assertEqual(main3('Si(C3(COOH)2)4(H2O)7'), 'Formeln är syntaktiskt korrekt')
        self.assertEqual(main3('Na332'), 'Formeln är syntaktiskt korrekt')
        self.assertEqual(main3('C(Xx4)5'), 'Okänd atom vid radslutet 4)5')
        self.assertEqual(main3('C(OH4)C'), 'Saknad siffra vid radslutet C')
        self.assertEqual(main3('C(OH4C'), 'Saknad högerparentes vid radslutet')
        self.assertEqual(main3('H2O)Fe'), 'Felaktig gruppstart vid radslutet )Fe')
        self.assertEqual(main3('H0'), 'För litet tal vid radslutet')
        self.assertEqual(main3('H1C'), 'För litet tal vid radslutet C')
        self.assertEqual(main3('H02C'), 'För litet tal vid radslutet 2C')
        self.assertEqual(main3('Nacl'), 'Saknad stor bokstav vid radslutet cl')
        self.assertEqual(main3('a'), 'Saknad stor bokstav vid radslutet a')
        self.assertEqual(main3('(Cl)2)3'), 'Felaktig gruppstart vid radslutet )3')
        self.assertEqual(main3(')'), 'Felaktig gruppstart vid radslutet )')
        self.assertEqual(main3('2'), 'Felaktig gruppstart vid radslutet 2')



def weight(molecule):

    try:
        x = initializer(molecule)
        print("Formeln är syntaktiskt korrekt")
        return x

    except Syntaxfel as inst:
        return (str(inst))

def main2():
    quitSign = '#'
    with open("sampleinput.txt", "r", encoding="utf-8") as sampleInput:
        a = sampleInput.readlines() # = sys.stdin: istället för = sampleInput.readlines()
        a2 = []
        for b in a:
            c = b[:(len(b)-1)]
            if not c == "":
                a2.append(str(c))
        for molecule in a2:
            molecule.strip()
            if molecule == quitSign:
                break
            try:
                initializer(molecule)
                print("Formeln är syntaktiskt korrekt")
                #else:
                #   raise Syntaxfel()
            except Syntaxfel as inst:
                print (str(inst))


def main():
    #quitSign = '#'
    #with open("sampleinput.txt", "r", encoding="utf-8") as sampleInput:
    #a = sampleInput.readlines() # = sys.stdin: istället för = sampleInput.readlines()
    a = sys.stdin
    a2 = []
    for b in a:
        c = b[:(len(b)-1)]
        if not c == "":
            a2.append(c)
    for molecule in a2:
        molecule.strip()
        if molecule == '#':
            break
        try:
            initializer(molecule)
            print("Formeln är syntaktiskt korrekt")
        except Syntaxfel as inst:
            print (str(inst))


#Här körs programmet
if __name__ == "__main__":
    #i = 1

    ruta = weight('Si(C3(COOH)2)4(H2O)7')
    #parser = main3("Na")
    mg = Molgrafik()
    mg.show(ruta)


    #nextRuta = ruta.next
    #nextRuta = Ruta(elem)
    #ruta = nextRuta



    #rutan2 = Ruta()
    #rutan2.name = "hej"


    #ruta.next = Ruta(rutan2)


    hej = input("Hejsan")



    #unittest.main()
