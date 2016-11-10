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
def readformel(molecule):
    q = createQueue(molecule)
    if checkSyntax(q):
        return True

#Skapar kö
def createQueue(molecule):
    q = LinkedQ()
    for part in molecule:
        q.enqueue(part)
    return q

def checkSyntax(q):
    peek = q.peek()
    upperCase = re.compile('[A-Z]')
    bigNum = re.compile('[1-9]')
    if q.peek():
        if peek == "(":
            parenthesisCheck(q)
            checkSyntax(q)
        elif peek == ')':
            parenthesisCheck(q)
            checkSyntax(q)
        elif upperCase.match(q.peek()):
            readMol(q)
            checkSyntax(q)
        #elif peek == ')':
        #    raise Syntaxfel("Felaktig gruppstart")
        elif bigNum.match(q.peek()):
            numberCheck(q)
            checkSyntax(q)
        else:
            print(q.peek())
            raise Syntaxfel('Felaktigt något')
    else:
        return

def readMol(q):
    upperCase = re.compile('[A-Z]')
    lowerCase = re.compile('[a-z]')
    if upperCase.match(q.peek()):
        atom = q.dequeue()
        if q.peek():
            if upperCase.match(q.peek()):
                atomCheck(atom)
                #return checkSyntax(q)
                return
            elif lowerCase.match(q.peek()):
                atom = atom + q.peek()
                q.dequeue()
                atomCheck(atom)
                return
            else:
                atomCheck(atom)
                return
        else:
            atomCheck(atom)
            return checkSyntax(q)
    else:
        raise Syntaxfel('Saknad stor bokstav')


def readInnerMol(q):
    sign = q.peek()
    if sign != ")":
        readMol(q)
    elif sign == ")":
        return
    else:
        pass



def atomCheck(atom):
    if atom in atoms:
        return
    else:
        raise Syntaxfel('Okänd atom')


def parenthesisCheck(q):
    lowerCase = re.compile('[a-z]')
    print(q.peek())
    if q.peek() == '(':
        q.dequeue()
        readMol(q)
        insideParenthesis(q)

    elif q.peek() == ')':
        q.dequeue()
        if numberCheck(q):
            checkSyntax(q)

            #parenthesisCheck(q)
    else:
        return
    if q.isEmpty():
        raise Syntaxfel('Saknad högerparentes')


def insideParenthesis(q):
    alfa = re.compile('[A-Za-z]')
    number = re.compile('[1-9]')
    if q.peek():
        #if q.peek() != ')':
            if alfa.match(q.peek()):
                readMol(q)
                insideParenthesis(q)
            elif number.match(q.peek()):
                print(q.peek() + "HAUISDUHILSADUHILDASHILUDSA")
                numberCheck(q)
                insideParenthesis(q)
            else:
                #if q.peek() == '(':
                    #checkSyntax(q)
                 #   insideParenthesis(q)
                #else:
                parenthesisCheck(q)
        #else:
        #    numberCheck(q)
        #    parenthesisCheck(q)
    else:
        raise Syntaxfel('Saknad högerparentes')


def numberCheck(q):
    oneNum = re.compile('[2-9]')
    bigNum = re.compile('[1-9]')
    anyNum = re.compile('[0-9]')
    num = q.dequeue()
    if num:
        if bigNum.match(num):
            if q.peek():
                if anyNum.match(q.peek()):
                    q.dequeue()
                    numIterator(q)
                else:
                    if oneNum.match(num):
                        #return checkSyntax(q)
                        return
                    else:
                        raise Syntaxfel('För litet tal')
            else:
                if oneNum.match(num):
                    return
                else:
                    raise Syntaxfel('För litet tal')

        else:
             raise Syntaxfel('För litet tal')
    else:
        return
def numIterator(q):
    anyNum = re.compile('[0-9]')
    while anyNum.match(q.peek()):
        q.dequeue()
        numIterator(q)
    else:
        checkSyntax(q)


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
                readformel(molecule)
                print("Formeln är syntaktiskt korrekt")
                #else:
                #   raise Syntaxfel()
            except Syntaxfel as inst:
                print (inst)




if __name__ == "__main__":
    main2()





