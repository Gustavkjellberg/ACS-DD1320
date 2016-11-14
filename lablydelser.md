---------------------------------------------------------------Lab 1---------------------------------------------------------------
Uppgift
I Joshuas pokedex finns data om olika egenskaper hos pokémon.
Spara ner dessa data till en csv-fil (se menyn Arkiv). 
Skriv en egen klass som representerar en pokémon.
Klassen ska ha attribut för minst fem data (välj själv vad du vill ta med).
Klassen ska ha minst fem metoder, bland dem metoden __str__
Skriv en funktion som skapar ett pokémon-objekt och anropar metoderna (så att du ser att dom fungerar som dom ska).
Skriv sedan en funktion som läser in data från filen, skapar objekt, och lagrar objekten i en lista (Pythons list()). 
Lägg till en funktion för att söka efter en pokémon i listan.
Testa att programmet fungerar korrekt.





---------------------------------------------------------------Lab 2---------------------------------------------------------------
Uppgifter
ArrayQ - en kö med Pythons array

I första uppgiften ska du skriva en egen klass ArrayQ där du implementerar en kö med hjälp av pythons array.
Börja med att importera modulen array med from array import array
Bestäm vilken typ av data du vill lagra.
Skapa en array och experimentera med array-metoderna append, insert, remove och pop. Rita bilder som illustrerar vad metoderna gör. Vilka vill du använda i din enqueue respektive dequeue? 
Nu är du redo att skriva din egen klass ArrayQ.
Attribut: En array (och ev andra attribut som du vill ha med). Alla attribut ska vara privata.
Metoder:  __init__, enqueue, dequeue och isEmpty (men inga andra metoder).
Testa ArrayQ
Prova din kö med följande testprogram: 
   q = ArrayQ()
   q.enqueue(1)
   q.enqueue(2)
   x = q.dequeue()
   y = q.dequeue()
   print(x,y)   # 1 2 ska komma ut
Skriv Trollkarlsprogrammet
Skriv ett program som simulerar korttricket (se videon och exemplet överst i labben). 
Inmatningstips är att använda input() för att läsa in hela raden, split() för att dela upp den och int() för att konvertera till heltal. Experimentera sedan med olika inmatade ordningar och se om du kan lista ut i vilken ordning korten ska ligga innan man börjar trolla för att man ska få ut alla tretton i rätt ordning
Skapa en ArrayQ-modul
Gör nu så här: klipp ut klassen från ditt program och klistra in i en ny fil arrayQFile.py 
Importera klassen till huvudprogrammet med raden 
        from arrayQFile import ArrayQ 
Nu går det att använda klassen utan att den syns i programmet.
LinkedQ - en kö av noder (länkad lista)
Nu ska du istället implementera kön som en länkad lista. Då behövs två nya klasser: Node och LinkedQ.  Skriv in bägge klasserna i samma fil: linkedQFile.py. Noderna i listan är objekt som vardera innehåller två (privata) attribut: ett värde (value) och en referens till nästa objekt (next).
Själva LinkedQ-klassen ska ha två attribut: first som håller reda på den första noden i kön och last som pekar ut den sista. Använd samma gränssnitt som i uppgift 1:
enqueue(x)
x = dequeue()
isEmpty()
Det är extra knepigt att programmera enqueue(x) eftersom det blir två fall, beroende på om kön är tom eller inte. Rita upp bägge fallen (lådor med pilar) innan du skriver koden!
Trollkarlsprogrammet med LinkedQ
Ändra import-satsen i trollkarlsprogrammet så att du importerar klassen LinkedQ istället för ArrayQ. Provkör. Fungerade det? Då har du lyckats implementera den abstrakta datastrukturen kö på två olika sätt.
När allt fungerar som det ska bör du ta en extra titt på koden. Är den kommenterad och begriplig? 
Vid redovisningen ska du kunna 
Berätta vad array-metoderna append, insert, remove och pop gör, vilka du valt att använda, och varför.
Förklara varför attributen ska vara privata.
Rita upp hur dina metoder fungerar för bägge implementationerna av kön.
Fungerar de två implementationerna likadant? Förklara eventuella skillnader.





---------------------------------------------------------------Lab 3---------------------------------------------------------------
Skriv en klass för binära sökträd
Nu ska du implementera ett binärt sökträd som en klass.
Tänk dig först ett abstrakt binärt sökträd. Eftersom man med Python kan jämföra ord (bokstavsordning) så går det bra att lagra ord i sökträdet, t ex så här:
   svenska = Bintree()              # Skapa ett trädobjekt
   svenska.put("gurka")		    # Sortera in "gurka" i trädet	
   - - -
   if "gurka" in svenska:      # Kolla om "gurka" finns i trädet
      - - -
   svenska.write()                  # Skriver alla ord i bokstavsordning
Klassen Bintree ska alltså ha tre metoder:
put(x) som sorterar in x i trädet
__contains__(x) som kollar om x finns i trädet (anropas av operatorn in)
write() som skriver ut trädet i inorder
Men i filen bintreeFile.py ska du dessutom definiera tre hjälpfunktioner. När trädobjektets put("gurka") anropas skickar trädet sin rotpekare och det nya ordet till en rekursiv funktion putta som ser till att en ny nod skapas på rätt ställe. Analogt gör de övriga anropen, alltså så här. 

class Bintree:
    def __init__(self):
        self.root=None

    def put(self,newvalue):
        self.root=putta(self.root,newvalue)

    def __contains__(self,value):
        return finns(self.root,value)

    def write(self):
        skriv(self.root)
        print("\n")


Här är klassen slut men sedan kommer definitionerna av funktionerna putta, finns och skriv. Trädet ska bara lagra en upplaga av varje objekt som läggs in.
Det finns förstås också en class Node i bintreefilen som innehåller ett värde och två pekare: left och right.
Andra uppgiften: Bygg träd och skriv ut dubbletter

Nu ska du läsa in ett ord i taget från filen word3.txt och lägga in det ditt binära sökträd. Ord som förekommer flera gånger (dubbletter) ska skrivas ut. 

from bintreeFile import Bintree
svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end = " ") 
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n")


Om du gjort rätt kommer dom dubblettord som spottas ut att bilda ett viktigt budskap.
Tredje uppgiften: Två binära sökträd med ordlistor
När du nu har ett sökträd med alla svenska trebokstavsord kan du blixtsnabbt kolla om ett givet ord finns med. Du ska nu läsa filen engelska.txt ord för ord och putta in orden i ett annat sökträd. Nu vill du inte ha dubbletterna utskrivna, så kolla först if engelska.exists(...). Om ordet redan fanns gör du ingenting, men om det är nytt ska du också kolla om det råkar finnas som svenskt ord. I så fall ska det skrivas ut på skärmen.
Om du har gjort rätt kommer dom utskrivna orden att bilda ännu ett hemligt budskap!



---------------------------------------------------------------Lab 4---------------------------------------------------------------
Breddenförstsökning
Hur ska vi använda breddenförstsökning i problemet?
Problemträdets urmoder/stamfar söt har barnen  nöt, sot, söm med flera, 
barnbarnen döm, som, not osv.
Enligt kedjan söt->söm->döm->dum->dur->sur är
sur barnbarnbarnbarnbarn till söt, men sur finns kanske redan tidigare i
problemträdet? För att finna den första förekomsten gör man en
breddenförstsökning enligt följande.
Lägg urmodern/stamfadern som första och enda post i en kö.
Upprepa sedan följande så länge det finns poster kvar i kön:
Plocka ut den första ur kön,
skapa alla barn till den
och lägg in dom sist i kön.
Första förekomsten av det sökta ordet ger kortaste lösningen.
Man kan spara in både tid och utrymme om man undviker att skapa barn som är
kopior av tidigare släktingar (t ex nöts barn söt), så
kallade dumbarn.
Första versionen
Låt filen bfs.py utgå från förra labben, som ju har
två binärträd. Nu kallar vi dom svenska (ordlistan) och gamla (dumbarnen).
Huvudprogrammet ska läsa in ordlistan, fråga efter startord och slutord,
och göra anropet makechildren(startord).
Funktionen makechildren ska systematiskt gå igenom alla sätt att byta ut en bokstav
i startordet (aöt, böt, ..., söö), kolla att det nya ordet finns i
ordlistan men inte finns i gamla och i så fall skriva ut det nya ordet på
skärmen och lägga in det i gamla.
Provkör! Om du gjort rätt ska söt få 10 barn.
Andra versionen
För fortsatt genomgång av söts barnbarn osv behövs den köklass LinkedQ som du skrev i kortkonstlabben. Importera den och skapa kön q. I stället för att skriva ut barnen på skärmen ska nu makechildren lägga in dom i kön. Huvudprogrammet lägger in startordet i kön och går sedan i en slinga 

while not q.isEmpty():
    nod = q.dequeue()
    makechildren(nod)


När makechildren() stöter på slutordet gör den utskriften
    print("Det finns en väg till", slutord)
eller talar om att ingen väg fanns. Provkör med lite olika start- och slutord, bland annat blå - röd, ful - fin och ute - hit.




---------------------------------------------------------------Lab 5---------------------------------------------------------------
Förbättra söt-sur
Det tråkiga med programmet från förra labben är att det bara talar om att det finns en lösning. För att programmet ska kunna skriva ut alla ord på vägen mellan söt och sur måste varje ord kunna peka på sin förälder. Det är alltså inte typen String du ska arbeta med utan en ParentNode som ser ut så här. 

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent


Huvudprogrammet ska skapa ett sådant objekt och lägga in startordet (som word-attribut). Det som sätts in i kön och plockas ut ur kön är nu inte längre ord utan ParentNode, och det betyder att du måste ändra i funktionen makechildren.
När makechildren finner slutordet vill den skriva ut hela kedjan genom ett anrop writechain(child). Metoden writechain() ska skrivas rekursivt, så att man får ut kedjan med slutordet sist.
Om kön töms utan att någon lösning påträffats bör programmet meddela att det är omöjligt. Och när en lösning skrivits ut bör programmet avbryta körningen. Ett sätt att göra det är sys.exit() om man importerar modulen sys. Ett annat sätt är definiera en egen Exception:
class SolutionFound(Exception):
    pass
och göra raise SolutionFound när lösningen hittats.





---------------------------------------------------------------Lab 6---------------------------------------------------------------
Sökning och sortering
I denna labb ska du arbeta med större datamängder. Filen /info/tilda/unique_tracks.txt (84MB) är hämtad från Million Song Dataset. Den innehåller data om en miljon låtar. Varje rad i filen har formatet:
     trackid<SEP>låtid<SEP>artistnamn<SEP>låttitel
Lista med objekt
Skriv en klass som representerar en låt enligt ovan. Förutom de vanliga metoderna ska du också implementera __lt__(self, other) som kan jämföra om objektet self är mindre än objektet other, med avseende på artistnamn.
Läs in låtarna från filen, skapa ett objekt för varje rad och spara objekten både
i en lista
i en dictionary (med artistnamn som nyckel)
Testa att inläsningen har fungerat.
Modulen timeit
Läs i dokumentationen för Pythons modul timeit och svara på följande frågor:
Vad representerar parametern stmt?
Vad representerar parametern number?
Vad är det timeit tar tid på?
Vad skrivs ut av ett anrop av timeit?
Tidtagningen
Nu ska du skriva ett program som gör följande, och tar tid på varje del:
Söker med linjärsökning i den osorterade listan.
Sorterar listan med lämplig sorteringsmetod.
Söker med binärsökning i den sorterade listan.
Slår upp ett element i dictionaryn.
Som hjälp för att komma igång har du följande exempel (kursiverade funktioner behöver du skriva själv). När man tar tid på en funktion som har parametrar får man använda lambda.
def main():

    filename = "/info/tilda/unique_tracks.txt"

    lista, dictionary = readfile(filename)
    n = len(lista)
    print("Antal element =", n)

    sista = lista[n-1]
    testartist = sista.artist

    linjtid = timeit.timeit(stmt = lambda: linsok(lista, testartist), number = 10000)
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")
Du får gärna använda kod (för sortering och sökning) från föreläsningar, kursboken eller andra källor, men var noga med att ange var koden kommer från.
Analys
Skriv upp tidskomplexiteten för de algoritmer du tagit tid på ovan. Stämmer dina resultat med teorin? Skriv en kommentar sist i ditt program där du analyserar dina resultat.förklara skillnaden i tid mellan de olika momenten.





---------------------------------------------------------------Lab 7---------------------------------------------------------------
1. Hashning med Pythons inbyggda dictionary
Minns du hur du i labb 2 gjorde en enklel kö med Pythons array? Nu ska du göra en egen hashtabell med Pythons dictionary!
Skriv en klass DictHash som använder dictionary. Den ska ha metoderna
store(nyckel, data)
x = search(nyckel)
Prova din dictionary med datafilen från förra labben. Tar det lika lång tid att köra?
Vill du kunna skriva d[nyckel] istället för d.search(nyckel)? Definiera då metoden __getitem__()
2. En egen implementation av hashtabellen
Nu ska du även göra hashningen själv, i din nya klass Hashtabell. Krav:
Definiera en klass HashNode för hashtabellens noder. Noderna måste innehålla både nyckel och värde.
Hashtabellen ska vara lagom stor
Du måste skriva en egen hashfunktion, som ger en bra fördelning över tabellen
Någon krockhantering måste ingå, t ex krocklistor eller probning
Du ska använda KeyError för att tala om att en nyckel inte finns
Testkörning 1
Prova med datafilen från förra labben.
Testkörning 2
Programmet hashtest.py innehåller data om alla atomer (namn och atomvikt). Lista ut vad det gör och hur det anropar hashtabellen. Modifiera det sedan för att kontrollera om din hashtabell fungerar.





---------------------------------------------------------------Lab 8---------------------------------------------------------------
Molekyler
Du ska implementera en syntax (se Föreläsning 10) för enkla molekyler, till exempel H2 eller Cr12. Körexempel (du behöver inte skriva detta interaktiva program):
Ge en molekyl: H2
Formeln är syntaktiskt korrekt
Ge en molekyl: cr12
Saknad stor bokstav
Ge en molekyl: Cr0
För litet tal vid radslutet
Ge en molekyl: Pb1
För litet tal vid radslutet
Ge en molekyl: Mn4
Formeln är syntaktiskt korrekt
Syntaxen besår av dessa fem regler:
      <molekyl> ::= <atom> | <atom><num>
      <atom>  ::= <LETTER> | <LETTER><letter>
      <LETTER>::= A | B | C | ... | Z
      <letter>::= a | b | c | ... | z
      <num>   ::= 2 | 3 | 4 | ...
Du ska inte kontrollera att bokstäverna bildar en verkligt atomnamn (det kommer i nästa labb), inte heller ska du undersöka om molekylen är rimlig kemiskt sett.
Skriv en spec med namnen på de funktioner du behöver och en kommentar för varje funktion som beskriver vad funktionen ska göra.
Gör en kopia av din LinkedQueue från labb 2, och lägg till metoden peek() som tittar på nästa värde i kön utan att plocka ut det.
Gör ett eget särfall Syntaxfel som är subklass (ärver från) Exception.
Skriv ett testprogram med unittest som ska kontrollera att funktionerna fungerar som avsett. Se exempel från syntaxföreläsningen.
Skriv själva funktionerna och provkör.
Du behöver inte skriva programmet i körexemplet ovan, det räcker med ett testprogram med unittest.




---------------------------------------------------------------Lab 9---------------------------------------------------------------
Formelkoll
Ditt program ska läsa formeln tecken för tecken och med rekursiv medåkning kolla syntaxen. Rekursiv medåkning innebär att huvudprogrammet först gör anropet readformel(), varefter readformel() anropar readmol() som anropar readgroup() och sedan eventuellt sej själv (men inte om inmatningen är slut eller om den just kommit tillbaka från ett parentesuttryck).
Funktionen readgroup() anropar antingen readatom() eller läser en parentes och anropar readmol() etc - allt enligt grammatiken. När ett syntaxbrott upptäcks genereras en exception (raise Syntaxfel("Saknad högerparentes")) som fångas i huvudprogrammet och där skrivs hela resten av indataraden ut.
Man måste ofta tjuvtitta på nästa tecken i kön (med peek()) för att veta vilken gren man ska följa i syntaxträdet.




---------------------------------------------------------------Lab 10---------------------------------------------------------------
Uppgift
Det här programmet ska fullborda det som den föregående labben har påbörjat. Det gör formelkoll som tidigare och ritar sedan upp molekylen. På skärmen kan det se ut så här (användarens inmatning i fetstil):
   Molekyl: Si(C3(COOH)2)4(H2O)7
   Molekyl:
och i molekylfönstret ritar programmet ut formelstrukturen: molekylträd
Låt ditt program bygga ett molekylträd
Du ska komplettera formelkollsprogrammet till att samtidigt bygga ett träd som ser ut som ovan. Varje ruta motsvaras av ett objekt:
class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None
Funktionen readgroup skapar först en sådan tomruta med
   rutan = Ruta() 
och anropar readatom och readnum för att kunna sätta in rätt värden på atom och num. Om det är en parentesgrupp ska readgroups anrop till readmol returnera en delmolekyl som sätts under rutan.down.
När readgroup är klar returnerar den rutan till anropet
    mol = readgroup()
som görs allra först i readmol. Vad som ska göras med mol.next får du själv tänka ut. Slutligen returnerar readmol den färdiga strukturen till readformel som returnerar den till huvudprogrammets anrop
    mol = readformel()
där mol pekar högst upp till vänster på syntaxträdet.
Rita molekylträdet
Huvudprogrammet ska nu rita upp den färdiga molekylen. Använd molgrafik.py. Skapa ett objekt av klassen Molgrafik:
   mg = Molgrafik()
Sedan ska
   mg.show(mol)
rita upp molekylbilden i ett eget fönster. Bilden ritas förstås rekursivt, och du ska formulera den rekursiva tanke som används. Om du inte kommer på den själv kanske det hjälper att kolla molgrafikkoden. Om programmet avslutas direkt hinner man inte se grafiken blinka förbi. Se därför till att ha en slinga för inmatning av flera formler.
Molekylvikten
Molekylvikten ska beräknas rekursivt med anropet weight(mol). Formulera först en mycket rekursiv tanke för vikten och programmera den sedan! Låt programmet skriva ut vikten av molekylen i terminalfönstret.
