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

def qRest(q):
    x = " "
    while not q.isEmpty():
        x = x + q.dequeue()
    return x


#Rekursiv medåkning
def readformel(molecule):
    # print (molecule+':', end=" ")
    q = createQueue(molecule)
    i = 0
    if readmol(q, i):
        return True

#Skapar kö
def createQueue(molecule):
    q = LinkedQ()
    for part in molecule:
        q.enqueue(part)
    return q

#Kollar om tecken är en bokstav
def readmol(q, i):
    cL = re.compile('[A-Z]')
    l = re.compile('[A-Za-z]')
    if cL.match(q.peek()):
        obj = q.dequeue()
        if q.peek():
            if l.match(q.peek()):
                if cL.match(q.peek()):
                    if obj in realz:
                        readmol(q, i)
                    else:
                        raise Syntaxfel("Okänd atom vid radslutet"+qRest(q))
                else:
                    a = obj + q.peek()
                    if a in realz:
                        nextLetter(q, l, i)
                    else:
                        q.dequeue() #Behövs pga att det är två tecken, tex "Xx" och inte bara ett som den tidigare.
                        raise Syntaxfel("Okänd atom vid radslutet"+qRest(q))
                return nextLetter(q, l, i)
            elif q.peek() == '(':
                if obj in realz:
                    q.dequeue()
                    i += 1
                    readmol(q, i)
                else:
                    raise Syntaxfel("Okänd atom vid radslutet"+qRest(q))
            elif q.peek() == ")":
                i -= 1
                if i < 0:
                    raise Syntaxfel("Felaktig gruppstart vid radslutet"+qRest(q))
                    #if cL.match(q.peek()):
                    #   readmol(q, i)
                else:
                    q.dequeue()
                    return isNum(q, i)
            else:
                isNum(q, i)
            return True
        else:
            if i == 0:
                if obj in realz:
                    return True
                else:
                    raise Syntaxfel("Okänd atom vid radslutet"+qRest(q))
            else:
                raise Syntaxfel("Saknad högerparentes vid radslutet")

                # else:
                #   raise Syntaxfel()
                #return True
    elif q.peek() == "(":
        q.dequeue()
        i += 1
        readmol(q, i)
    elif q.peek() == ")":
        #q.dequeue()
        i -= 1
        if i < 0:
            raise Syntaxfel("Felaktig gruppstart vid radslutet"+qRest(q))
        else:
            q.dequeue()
            if q.peek() == None:
                raise Syntaxfel("Saknad siffra vid radslutet" + qRest(q))
            else:
                return isNum(q, i)
    elif q.peek() is None:
        q.dequeue()
        if i == 0:
            return True
        else:
            raise Syntaxfel("För få paranteser vid radslutet")
    else:
        nextN = re.compile('[0-9]')
        if nextN.match(q.peek()):
            raise Syntaxfel("Felaktig gruppstart vid radslutet" + qRest(q))
        elif l.match(q.peek()):
            raise Syntaxfel("Saknad stor bokstav vid radslutet"+qRest(q))
        else:
            raise TypeError("Fel tecken vid radslutet")
    return True

#Hjälpfunktion för ovan
def nextLetter(q, l, i):
    q.dequeue()
    n = re.compile('[1-9]')
    if q.peek():
        if l.match(q.peek()):
            return readmol(q, i)
        elif n.match(q.peek()):
            return isNum(q, i)
        else:
            return readmol(q, i)
    else:
        return True

#Kollar om tecken är en siffra
def isNum(q, i):
    num = q.peek()
    n = re.compile('[2-9]')
    nextN = re.compile('[0-9]')
    firstN = re.compile('[1-9]')


    if firstN.match(num):
        q.dequeue()
        if q.peek() is None:
            if n.match(num):
                if i == 0:
                    return True
                else:
                    raise Syntaxfel("För få paranteser vid radslutet")
            else:
                raise Syntaxfel("För litet tal vid radslutet" + qRest(q))
                #return False
        elif nextN.match(q.peek()):
            return nextNum(q, nextN, i)
        else:
            if n.match(num):
                return readmol(q, i)
            #return False
            else:
                raise Syntaxfel("För litet tal vid radslutet"+qRest(q))
    elif num == '0':
        q.dequeue()

        raise Syntaxfel("För litet tal vid radslutet" + qRest(q))
    else:
        #return False
        raise Syntaxfel("Saknad siffra vid radslutet"+qRest(q))

#Hjälpfunktion till ovan
def nextNum(q, nextN, i):
    q.dequeue()
    if q.peek() is None:
        return True
    elif nextN.match(q.peek()):
        nextNum(q, nextN, i)
    else:
        readmol(q, i)
    return True

realz = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']


#Huvudfunktion


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
                    readformel(molecule)
                    print("Formeln är syntaktiskt korrekt")
                    #else:
                    #   raise Syntaxfel()
                except Syntaxfel as inst:
                    print (str(inst))
            except TypeError as inst:
                print(str(inst))
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
            try:
                readformel(molecule)
                print("Formeln är syntaktiskt korrekt")
                # else:
                #    raise Syntaxfel()
            except Syntaxfel as inst:
                print (str(inst))
        except TypeError as inst:
            print(str(inst))

#Här körs programmet
if __name__ == "__main__":
    main2()