#Gustav Kjellberg 951028-2578
#Isak Hassbring  940204-1496
import re
import sys
from array import array


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
        if not self.isEmpty():
            return self.first.getNum()
        else:
            return None
    def isEmpty(self):
        return self.length == 0


class Syntaxfel(Exception):
    pass
atoms = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']
def qRest(q):
    x = " vid radlutet "
    while not q.isEmpty():
        x = x + q.dequeue()
    return x


#Rekursiv medåkning
def initializer(molecule):
    q = createQueue(molecule)
    letter = re.compile('[A-Za-z]')
    upperCase = re.compile('[A-Z]')
    lowerCase = re.compile('[a-z]')
    number29 = re.compile('[2-9]')
    number19 = re.compile('[1-9]')
    number09 = re.compile('[0-9]')
    if readFormel(q, letter, upperCase, lowerCase, number29, number19, number09):
        return True

#Skapar kö
def createQueue(molecule):
    q = LinkedQ()
    for part in molecule:
        q.enqueue(part)
    return q

def readFormel(q, letter, upperCase, lowerCase, number29, number19, number09):
    #om det är en boktav
    if q.peek():
        if upperCase.match(q.peek()):
            readMol(q, letter, upperCase, lowerCase, number29, number19, number09)
        #om parentes (
        elif q.peek() == '(':
            readGroup(q, letter, upperCase, lowerCase, number29, number19, number09)
        #siffra
        else:
            raise Syntaxfel("Felaktig gruppstart")
    return

def readMol(q, letter, upperCase, lowerCase, number29, number19, number09):
    firstLetter = q.dequeue()
    if upperCase.match(firstLetter):
        if q.peek():
            if letter.match(q.peek()):
                if lowerCase.match(q.peek()):
                    #atom = firstLetter + q.peek()
                    checkAtom(firstLetter + q.peek())
                    q.dequeue()
                    nextSign(q, letter, upperCase, lowerCase, number29, number19, number09)
            checkAtom(firstLetter)
            nextSign(q, letter, upperCase, lowerCase, number29, number19, number09)

        else:
            checkAtom(firstLetter)
            return
    else:
        raise Syntaxfel('Saknad stor bokstav')


def nextSign(q, letter, upperCase, lowerCase, number29, number19, number09):
    if q.peek():
        if number09.match(q.peek()):
            checkNumber(q, letter, upperCase, lowerCase, number29, number19, number09)
        readFormel(q, letter, upperCase, lowerCase, number29, number19, number09)
    else:
        return

    #om siffra kolla att den är stor nog
def checkNumber(q, letter, upperCase, lowerCase, number29, number19, number09):
    if number19.match(q.peek()):
        q.dequeue()
        numIterator(q, number09)
    else:
        raise Syntaxfel("För litet tal")
def numIterator(q, number09):
    if q.peek():
        if number09.match(q.peek()):
            q.dequeue()
            numIterator(q, number09)
        else:
            return
    else:
        return

#def readGroup(q):
    #sålänge det finns ngt i kön och ingen ) har kommit forsätt, blir kön tom skriv sknad höger
    #om det kommer ( anropa read group) igen
    #Kommer en ) returna True


def checkAtom(atom):
        if atom in atoms:
            return
        else:
            raise Syntaxfel('Okänd atom')


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
                try:
                    initializer(molecule)
                    print("Formeln är syntaktiskt korrekt")
                    #else:
                    #   raise Syntaxfel()
                except Syntaxfel as inst:
                    print (str(inst))
            except TypeError as inst:
                print(str(inst))

if __name__ == "__main__":
    main2()