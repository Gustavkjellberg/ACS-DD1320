###########################################################################
# Att göra lab6:

# TIMEIT - KLAR. 
# Vad representerar parametern stmt? - Statement som man ska ta tid på. 
# Vad representerar parametern number? - Hur många exekveringar som ska göras. Det är olika lång tid på alla, sen tar man genomsnitt eller lägsta/snabbaste.
# Vad är det timeit tar tid på? - Genomsnittet av hastigheten på de exekveringar av statementet man har gjort (tex en funktion med ett visst givet insongList)
# Vad skrivs ut av ett anrop av timeit? - Den snabbaste tiden som gjordet av de försök som gjordes.

# TIDTAGNINGEN - EJ KLAR.

# A) Listan
# Söker med linjärsökning i den osorterade listan.
# Sorterar listan med lämplig sorteringsmetod.
# Söker med binärsökning i den sorterade listan. Contains?

# B) Dict
# Slår upp ett element i dictionaryn.



# BESVARA VID REDOVISNING -EJ KLAR.
# 1. berätta vilken tidskomplexitet dina algoritmer har. - KLAR
# 2. visa hur dina sök-, och sorteringsfunktioner fungerar. - EJ KLAR
# 3. motivera upplägget av dina experiment. - EJ KLAR
# 4. förklara skillnaden i tid mellan de olika momenten. - EJ KLAR

# 1. linsok KLAR
# 2. Quicksort Ej Klar
# 3. Binärsök quicksort-listan Ej klar
# 4. gör själva tids skiten Ej Klar



###########################################################################
#RESULTAT
#Antal element = 1000000
#Linjärsökningen tog 0.1736 sekunder
#Quicksort tog 22.104 sekunder
#Binärsökning tog 1.27954e-05 sekunder


###########################################################################

# -----Imports-----#
import timeit
from song import *

# -----Functions-----#

def test(x,y):
    a = x
    b = y
    return a, b



def readfile(filename):  # Skapar tomma, läser in filen i lista & dictionary och returnerar lista & dictionary.
    songList = []
    songDict = {}

    with open(filename, "r", encoding="utf-8") as songfile:  # Öppnar filen i read-mode
        for row in songfile:  # Varje rad läses in
            rowSplit = row.split("<SEP>")  # skapar mellanslag mellan låt och
            id1 = rowSplit[0]
            id2 = rowSplit[1]
            artist = rowSplit[2]
            song = rowSplit[3]
            songObject = Song(id1, id2, song, artist)

            songDict[artist] = songObject
            songList.append(songObject)

    return songList, songDict


def linsok(songList, askedArtist):  # Tidskomplexitet: O(N).
    x = False
    for obj in songList:
        if obj.getArtist() == askedArtist:
            #print (obj.getData(), "fanns i listan.")
            x = True
            break
    if x == False:

        print("hittar ej")



# -----Quicksort start----#
def partitionera(songList, v, h, pivot):
    while True:
        v = v + 1
        #while songList[v] < pivot:
        while songList[v].__lt__(pivot):
            v = v + 1
        h = h - 1
        #while h != 0 and songList[h] > pivot:
        while h != 0 and not songList[h].__lt__(pivot):
            h = h - 1
        songList[v], songList[h] = songList[h], songList[v]
        if v >= h:
            break
    songList[v], songList[h] = songList[h], songList[v]
    return v


def qsort(songList, left, right):
    pivotindex = (left + right) // 2
    songList[pivotindex], songList[right] = songList[right], songList[pivotindex]
    k = partitionera(songList, left - 1, right, songList[right].getArtist())
    #print(k)
    songList[k], songList[right] = songList[right], songList[k]
    if k - left > 1:
        qsort(songList, left, k - 1)
    if right - k > 1:
        qsort(songList, k + 1, right)


def quicksort(songList):  # Tidskomplexitet: O(n log N).
    right = len(songList) - 1
    qsort(songList, 0, right)
    return songList

# -----Quicksort slut----#


#binsearch
def binsearch(sortedList, key):
    
    left = 0
    right = len(sortedList) - 1
    found = False

    while left <= right and not found:
        midIndex = (left + right)//2
        if sortedList[midIndex].getArtist() == key:
            found = True
            #print(str(sortedList[midIndex].getData()) + " Was found")
        else:
            if key < sortedList[midIndex].getArtist():
                right = midIndex - 1
            else:
                left = midIndex + 1



def search(songDict, key):
 
    if songDict[key]:
       return True
    # found = False
    # for lookup in songDict:
    #     if lookup == key:
    #         #print (key)
    #         found = True
    #         return True
    # if found == False:
    #     print ("Hittade ej")
    #     return False
    #for elem in songDict:
     #   if elem.getArtist() == "Emery"


# -----Huvudprogram-----#
# noinspection PyNonAsciiChar



def main1():
    filename = "unique_tracks.txt"

    lista, dictionary = readfile(filename)
    n = len(lista)
    print("Antal element =", n)
    sista = lista[n - 1]
    sortedList = quicksort(lista)

    #search(dictionary, "Emery")

    searchTid = timeit.timeit(stmt = lambda: search(dictionary, "Emery"), number=100)
    searchTid = searchTid/100
    print("Search tog ", searchTid, "sekunder")
    
    linjtid = timeit.timeit(stmt=lambda: linsok(lista, "Emery"), number=100)
    linjtid = linjtid/100
    print("Linjärsökningen tog", round(linjtid, 4), "sekunder")

    quicksortTime = timeit.timeit(stmt=lambda: quicksort(sortedList), number=3)
    quicksortTime = quicksortTime/3
    print("Quicksort tog", round(quicksortTime, 4), "sekunder")
    
    binsearchTime = timeit.timeit(stmt=lambda: binsearch(sortedList, "Lena Philipsson"), number=1000)
    binsearchTime = binsearchTime/1000
    print("Binärsökning tog", round(binsearchTime, 10), "sekunder")



main1()



# TIDSKOMPLEXITET

# linsok = O(N). Linjär.
# Vi anser att tidskomplexiteten stämmer eftersom att tiden ökar likt linjärt om man söker efter en artist längre bak i listan.



# Quicksort = O(n log(n)) i bästa fall eller O(n^2) i värsta fall.
# Vi vet att partionera funktionen kommer att ha konstant komplexitet,O(n) och i värsta fall behöva göra ett byta för varje element.

# Värsta fallet sker då alla element är enskilt, större eller enskild mindre än referensobjektet(pivot). Detta kommer reultera i att quicksort få komplexiteten O(n^2).

# Bästa fallet är då alla subarrays är jämna och sorterade, vi får då komplexiteten O(n*log(n)).
# Vi ser från reultatet att medeltiden blir ca 22 sekunder vilket kan anses vara mycket, men skall man göra många sökningar i listan så kan det vara värt att använda QS
#eftersom att binärsökningen är 10^4 gånger så snabb som linjärsökningen för vårat fall.



#Binärsökning = log(n)
#vi ser att binärsökningen är effektiv för den sorterade listan.