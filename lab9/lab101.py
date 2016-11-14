#Gustav Kjellberg 951028-2578
#Isak Hassbring  940204-1496
import re
import sys
import unittest
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
        q.dequeue()
        raise Syntaxfel('Okänd atom' + qRest(q))


def checkNumber(q, letter, upperCase, lowerCase, number29, number19, number09):
    num = q.dequeue()
    if number19.match(num):
        if q.peek():
            if number09.match(q.peek()):
                return numIterator(q, number09)
            else:
                if number29.match(num):
                    return
        else:
            if number29.match(num):
                return
    raise Syntaxfel("För litet tal" + qRest(q))

def nextSignInside(q, letter, upperCase, lowerCase, number29, number19, number09):
    if q.peek():
        if number09.match(q.peek()):
            checkNumber(q, letter, upperCase, lowerCase, number29, number19, number09)
    return readGroup(q, letter, upperCase, lowerCase, number29, number19, number09)

def nextSign(q, letter, upperCase, lowerCase, number29, number19, number09):
    if q.peek():
        if number09.match(q.peek()):
            checkNumber(q, letter, upperCase, lowerCase, number29, number19, number09)
        return readFormel(q, letter, upperCase, lowerCase, number29, number19, number09)
    else:
        return

def readFormel(q, letter, upperCase, lowerCase, number29, number19, number09):
    #om det är en boktav
    if q.peek():
        if letter.match(q.peek()):
            readMol(q, letter, upperCase, lowerCase, number29, number19, number09)
            return readFormel(q, letter, upperCase, lowerCase, number29, number19, number09)
        #om parentes (
        elif q.peek() == '(':
            q.dequeue()
            if q.peek() == ')':
                readFormel(q, letter, upperCase, lowerCase, number29, number19, number09)
            else:
                readGroup(q, letter, upperCase, lowerCase, number29, number19, number09)
                return readFormel(q, letter, upperCase, lowerCase, number29, number19, number09)
        else:
            raise Syntaxfel('Felaktig gruppstart' + qRest(q))
    return

def readMol(q, letter, upperCase, lowerCase, number29, number19, number09):
    if upperCase.match(q.peek()):
        firstLetter = q.dequeue()
        if q.peek():
            if letter.match(q.peek()):
                if lowerCase.match(q.peek()):
                    checkAtom(firstLetter + q.peek(), q)
                    q.dequeue()
                    nextSign(q, letter, upperCase, lowerCase, number29, number19, number09)
            checkAtom(firstLetter, q)
            nextSign(q, letter, upperCase, lowerCase, number29, number19, number09)

        else:
            checkAtom(firstLetter, q)
            readFormel(q, letter, upperCase, lowerCase, number29, number19, number09)
    else:
        raise Syntaxfel('Saknad stor bokstav' + qRest(q))


def readMolInside(q, letter, upperCase, lowerCase, number29, number19, number09):
    if upperCase.match(q.peek()):
        firstLetter = q.dequeue()
        if q.peek():
            if letter.match(q.peek()):
                if lowerCase.match(q.peek()):
                    checkAtom(firstLetter + q.peek(), q)
                    q.dequeue()
                    return nextSignInside(q, letter, upperCase, lowerCase, number29, number19, number09)
            checkAtom(firstLetter, q)
            return nextSignInside(q, letter, upperCase, lowerCase, number29, number19, number09)
        else:
            checkAtom(firstLetter, q)
            return nextSignInside(q, letter, upperCase, lowerCase, number29, number19, number09)
    else:
        raise Syntaxfel('Saknad stor bokstav' + qRest(q))





def numIterator(q, number09):
    if q.peek():
        if number09.match(q.peek()):
            q.dequeue()
            numIterator(q, number09)
        else:
            return
    else:
        return


    #om siffra kolla att den är stor nog




def checkNumberAfterP(q, letter, upperCase, lowerCase, number29, number19, number09):
    if number09.match(q.peek()):
        return checkNumber(q, letter, upperCase, lowerCase, number29, number19, number09)
    else:
        raise Syntaxfel('Saknad siffra' + qRest(q))

def readGroup(q, letter, upperCase, lowerCase, number29, number19, number09):
    #sålänge det finns ngt i kön och ingen ) har kommit forsätt, blir kön tom skriv sknad höger
    #om det kommer ( anropa read group) igen
    #Kommer en ) returna True
    while q.peek() is not None:
        if q.peek() == "(":
            q.dequeue()
            if upperCase.match(q.peek()):
                #readGroup(q, letter, upperCase, lowerCase, number29, number19, number09)
                readMolInside(q, letter, upperCase, lowerCase, number29, number19, number09)
                return readGroup(q, letter, upperCase, lowerCase, number29, number19, number09)
            else:
                readFormel(q, letter, upperCase, lowerCase, number29, number19, number09)
        elif q.peek() == ")":
            q.dequeue()
            if q.peek():
                return checkNumberAfterP(q, letter, upperCase, lowerCase, number29, number19, number09)
            else:
                return
            #readGroup(q, letter, upperCase, lowerCase, number29, number19, number09)
        #elif upperCase.match(q.peek()):
        else:
            return readMolInside(q, letter, upperCase, lowerCase, number29, number19, number09)
    if q.isEmpty():
        raise Syntaxfel("Saknad högerparentes" + qRest(q))



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
    if readFormel(q, letter, upperCase, lowerCase, number29, number19, number09):
        return True



class TestStringMethods(unittest.TestCase):
    def test_main(self):
        inp = "Na"
        #self.assertEqual(main3("Na"), "print")
        self.assertEqual(main3('inp'), 'Formeln är syntaktiskt korrekt')




def main3(inp):
    try:
        initializer(inp)
        print("Formeln är syntaktiskt korrekt")
    except(Syntaxfel) as inst:
        print (inst)

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
    main2()
    #unittest.main()
