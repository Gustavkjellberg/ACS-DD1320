import unittest
from linkedQ8 import *
import re
# Spec



# takes molecule-input, instantiates isMolecule
# main()


# skapar en kö av varje moleculeekylens olika delar, vi splittar således upp den i tecken för tecken och stoppar in i queue
# createQueue(molecule)


# uses queue func and also uses a func to check is syntax is correct, then returns true else returns false
# isMolecule(molecule)

# checks that the first part of the queue is a capital letter and saves as a variable firstLetter
# then peeks to check if next is a letter, if not calls isNumber()
# if first isn't capital letter then raise Syntaxerror
# isLetter(queue)

# called if a dequeued object isn't a letter, shall match one or more letters 1-9, else raise syntaxerror
# for every object, enqueue and check if peek() == firstLetter
# isNumber(dequedObject)

# prints queue if syntax is correct
# printQueue





class Syntaxfel(Exception):
    pass

def isMolecule(molecule):
    q = createQueue(molecule)
    if isLetter(q):
        return True
    else:
        #return False
        raise Syntaxfel()
def createQueue(molecule):
    q = LinkedQ()
    for part in molecule:
        q.enqueue(part)
    return q

def isLetter(q):
    obj = q.dequeue()
    cL = re.compile('[A-Z]')
    l = re.compile('[A-Za-z]')
    if not ((cL.match(obj)) == None):
        if l.match(q.peek()):
            return nextLetter(q, l)
        else:
            isNum(q)
        return True
    else:
        #return False
        raise Syntaxfel()

def nextLetter(q, l):
    obj = q.dequeue()
    if l.match(q.peek()):
        nextLetter(q, l)
    else:
        return isNum(q)
    return True
def isNum(q):
    num = q.dequeue()
    n = re.compile('[2-9]')
    nextN = re.compile('[0-9]')
    firstN = re.compile('[1-9]')
    if firstN.match(num):
        if q.peek() == None:
            if n.match(num):
                return True
            else:
                raise Syntaxfel()
                #return False
        elif nextN.match(q.peek()):
            nextNum(q, nextN)
        else:
            if n.match(num):
                isLetter(q)
            #return False
            else:
                raise Syntaxfel()
    else:
        #return False
        raise Syntaxfel()

def nextNum(q, nextN):
    num = q.dequeue()
    if nextN.match(num):
        if q.peek() == None:
            return True
        elif nextN.match(q.peek()):
            nextNum(q, nextN)
        else:
            isLetter(q)
    else:
        #return False
        raise Syntaxfel()





def main():
    molecule = input("Ange en molekyl: ")
    try:
        if isMolecule(molecule):
            print(molecule + " existerar")
        else:
            raise Syntaxfel()
    except Syntaxfel:
        print("Fanns ej")


class TestMethods(unittest.TestCase):

    def test_isMolecule(self):
        self.assertTrue(isMolecule('CO2'))
        #self.assertFalse(isMolecule('a'))
        with self.assertRaises(Syntaxfel):
            isMolecule('a')
    def test_isLetter(self):
        q = createQueue('CO2')
        self.assertTrue(isLetter(q))
        q = createQueue('a')
        #self.assertFalse(isletter(q))
        with self.assertRaises(Syntaxfel):
            isLetter(q)

    def test_nextLetter(self):
        q = createQueue('Cl2')
        l = re.compile('[A-Za-z]')
        self.assertTrue(nextLetter(q, l))
        q = createQueue("--")
        #self.assertFalse(nextLetter(q, l))
        with self.assertRaises(Syntaxfel):
            nextLetter(q, l)

    def test_isNum(self):
        q = createQueue('2')
        self.assertTrue(isNum(q))
        q = createQueue("--")
        #self.assertFalse(isNum(q))
        with self.assertRaises(Syntaxfel):
            isNum(q)

    def test_nextNum(self):
        q = createQueue('2')
        nextN = re.compile('[0-9]')
        self.assertTrue(nextNum(q, nextN))
        q = createQueue('-')
        #self.assertFalse(nextNum(1, nextN))
        with self.assertRaises(Syntaxfel):
            nextNum(q, nextN)


if __name__ == "__main__":
    unittest.main()
    #main()