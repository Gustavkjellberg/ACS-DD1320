b = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']
c = []
for a in b:
    c.append("'"+a+"'")

print (b)
print (c)


#Gustav Kjellberg 951028-2578
#Isak Hassbring  940204-1496
import unittest
from linkedQ9 import *
import re
import sys
# Spec



# takes molecule-input, instantiates isMolecule
# main()


# skapar en kö av varje molecule olika delar, vi splittar således upp den i tecken för tecken och stoppar in i queue
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

global qRest
qRest = "qRest"

def qRest(q):
    x = ""
    while not q.isEmpty():
        x = x + str(q.dequeue())
    return x




#Rekursiv medåkning
def isMolecule(molecule):
    print (molecule+'\n')
    q = createQueue(molecule)
    i = 0
    if isLetter(q, i):
        return True
    else:
        raise Syntaxfel("HAlallalla")

#Skapar kö
def createQueue(molecule):
    q = LinkedQ()
    for part in molecule:
        q.enqueue(part)
    return q

#Kollar om tecken är en bokstav
def isLetter(q, i):
    obj = q.dequeue()
    cL = re.compile('[A-Z]')
    l = re.compile('[A-Za-z]')
    if cL.match(obj):
        print("**** isLetter:Har matchat stor bokstav.****"+'\n')
        if q.peek():
            if l.match(q.peek()):
                if cL.match(q.peek()):
                    if obj in realz:
                        print ("************************ "+obj+" finns bland atomerna. ************************")
                        nextLetter(q, l, i)
                    else:
                        raise Syntaxfel("Okänd atom vid radslutet"+qRest(q))
                else:
                    a = str(obj) + str(q.peek())
                    print ("************************ "+a+" finns bland atomerna.************************")
                    if a in realz:
                        nextLetter(q, l, i)
                    else:
                        raise Syntaxfel("Okänd atom vid radslutet"+qRest(q))
                return nextLetter(q, l, i)
            elif q.peek() == '(':
                q.dequeue()
                i += 1
                isLetter(q, i)
            elif q.peek() == ")":
                test = q.dequeue()
                i -= 1
                if i < 0:
                    raise Syntaxfel("Saknad högerparentes vid radslutet")
                if cL.match(q.peek()):
                    raise isLetter(q, i)
                else:
                    isNum(q, i)
                return True
            else:
                isNum(q, i)
            return True
        elif q.peek() == None:
            if i == 0:
                if obj in realz:
                    return True
                else:
                    raise Syntaxfel("Okänd atom vid radslutet"+qRest(q))
            else:
                raise Syntaxfel("För få paranteser")
        else:
            raise Syntaxfel()
        return True
    elif obj == "(":
        i += 1
        isLetter(q, i)
    elif obj == ")":
        i -= 1
        if i < 0:
            raise Syntaxfel("En parantes för mycket vid radslut " + qRest(q))
        else:
            isNum(q, i)
    elif obj == None:
        if i == 0:
            return True
        else:
            raise Syntaxfel("För få paranteser")
    else:
        raise Syntaxfel("************************ "+"Ej stor bokstav!!!"+qRest(q)+"************************ ")
    return True

#Hjälpfunktion för ovan
def nextLetter(q, l, i):
    obj = q.dequeue()
    n = re.compile('[1-9]')
    if q.peek():
        if l.match(q.peek()):
            return nextLetter(q, l, i)
        elif n.match(q.peek()):
            return isNum(q, i)
        else:
            return isLetter(q, i)
    else:
        return True

#Kollar om tecken är en siffra
def isNum(q, i):
    num = q.dequeue()
    n = re.compile('[2-9]')
    nextN = re.compile('[0-9]')
    firstN = re.compile('[1-9]')
    if firstN.match(num):
        if q.peek() == None:
            if n.match(num):
                return True
            else:
                raise Syntaxfel("För liten siffra " + qRest(q))
                #return False
        elif nextN.match(q.peek()):
            return nextNum(q, nextN, i)
        else:
            if n.match(num):
                return isLetter(q, i)
            #return False
            else:
                raise Syntaxfel()
    else:
        #return False
        raise Syntaxfel("För liten siffra " + qRest(q))

#Hjälpfunktion till ovan
def nextNum(q, nextN, i):
    num = q.dequeue()
    if q.peek() == None:
        return True
    elif nextN.match(q.peek()):
        nextNum(q, nextN, i)
    else:
        isLetter(q, i)
    return True

def inlasning():
    #molecule = input("Ange en molekyl: ")
    with open("sampleinput.txt", "r", encoding="utf-8") as sampleInput:

        a = sampleInput.readlines() # = sys.stdin: istället för = sampleInput.readlines()
        l = 0
        a2 = []
        for b in a:
            c = b[:(len(b)-1)]
            if not c == "":
                a2.append(c)


realz = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']


#Huvudfunktion
def main():
    quitSign = '#'
    #molecule = input("Ange en molekyl: ")
    with open("sampleinput.txt", "r", encoding="utf-8") as sampleInput:
        a = sampleInput.readlines() # = sys.stdin: istället för = sampleInput.readlines()
        l = 0
        a2 = []
        for b in a:
            c = b[:(len(b)-1)]
            if not c == "":
                a2.append(c)
        for molecule in a2:
            molecule.strip()
            if molecule == quitSign:
                print("TROLOLOLOLOLOL")
                break
            try:
                print ("****"+molecule+"****")
                if isMolecule(molecule):
                    print("Formeln är syntaktiskt korrekt")
                else:
                    raise Syntaxfel()
            except Syntaxfel as inst:
                print (str(inst))

#Här körs programmet
if __name__ == "__main__":
    #unittest.main()
    main()



Si(C3(COOH)2)4(H2O)7
Na2
(Na
C(Xx4)5
C(OH4)C
C(OH4C
H2O)Fe
H0
H1C
H02C
Nacl
a
(Cl)2)3
)
2
#