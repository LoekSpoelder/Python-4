import os, time, random
woordenboek = {}

#Dit zijn variabelen die je kan veranderen
DELETE = 'd'
EXTENSIE = '.txt'
KIES_LIJST = 'k'
MAX_WOORDLENGTE = 20
NIEUWE_LIJST = 'n'
OPSLAAN = 'w'
OVERHOREN = 'o'
SCHEIDER = '='
SCHERMBREEDTE = 50
STANDAARD_LIJST = 'NL-ENG.txt'
STOPPEN = 's'
TOEVOEGEN = 't'

#Deze functie laat je veranderen van lijst en laat je de bestanden zien die in de map zitten.
def kies_lijst(huidig):
    gekozenlijst = huidig
    loop = True
    while loop == True:
        leeg_scherm()
        stowage = os.listdir()
        stowage.remove(".git")
        stowage.remove("program.py")
        print_header()
        print_header_regel("De Huidige lijst is: " + nieuwe_lijst_naam(huidig))
        print_regel()
        print_regel("Woordenlijsten in map:")
        for thingy in range(len(stowage)):
            print_regel(stowage[thingy])
        print_regel()
        print_regel("Voer hieronder de gekozen lijstnaam in.")
        print_regel("Voer '" + STOPPEN + "' in om te stoppen.")
        print_footer()
        antwoord = input("Woordenlijst: ")
        if antwoord in stowage:
            gekozenlijst = antwoord
            loop = False
        elif antwoord == STOPPEN:
            loop = False
        else:
            print("Dat is niet een woordenlijst.")
            time.sleep(2)
    return gekozenlijst

#Deze functie maakt het terminal scherm leeg
def leeg_scherm():
    os.system('cls')

#Deze functie schrijft een bestand over naar een dictionary
def lees_woordenlijst(bestandsnaam):
    woordenboek = {}
    f = open(bestandsnaam)
    for line in f:
        woord1, woord2 = line.strip('\n').split(SCHEIDER)
        woordenboek[woord1] = woord2
    f.close()
    return woordenboek

#Deze functie activeert de andere functies, het is de main functie
def main():
    wrdbk = STANDAARD_LIJST
    while True:
        leeg_scherm()
        print_menu(nieuwe_lijst_naam(wrdbk))
        keuze = input("Uw keuze: ")
        if keuze == NIEUWE_LIJST:
            leeg_scherm()
            print_header()
            print_regel("Typ hieronder de nieuwe lijst naam in.")
            print_regel("vergeet niet de extensie .txt toe te voegen!")
            print_footer()
            naam = input()
            if naam.upper() in (name.upper() for name in os.listdir()):
                print("Die bestaat al!")
                time.sleep(2)
            elif naam == STOPPEN:
                pass
            else:
                f = open(naam, "w")
                wrdbk = naam
        elif keuze == KIES_LIJST:
            wrdbk = kies_lijst(wrdbk)
        elif keuze == TOEVOEGEN:
            voeg_woorden_toe(wrdbk)
        elif keuze == OVERHOREN:
            lees_woordenlijst(wrdbk)
            if bool(lees_woordenlijst(wrdbk)):
                overhoren(lees_woordenlijst(wrdbk), wrdbk)
            else:
                print("Je moet nog woorden toevoegen.")
                time.sleep(2)
        elif keuze == STOPPEN:
            leeg_scherm()
            print_afscheid()
            break
        else:
            print("Vul " + NIEUWE_LIJST + ", " + KIES_LIJST + ", " + TOEVOEGEN + ", " + OVERHOREN + " of " + STOPPEN + " in.")
            time.sleep(2)

#Deze functie stript de extensie van de bestandsnaam
def nieuwe_lijst_naam(lijst):
    return lijst.strip(EXTENSIE)

#Deze functie overhoort door willekeurig door de dictionairy heen te gaan en laat je het woord verwijderen als je het fout hebt
def overhoren(woordenlijst, wrdbk):
    Layer1 = True
    while Layer1 == True:
        key, value = random.choice(list(woordenlijst.items()))
        leeg_scherm()
        print_header()
        print_header_regel('Wat is de vertaling van "' + value + '".')
        print_footer()
        answer = input()
        if answer == key:
            leeg_scherm()
            print_header()
            print_header_regel("Juist, " + value + " betekent " + key + ".")
            print_footer()
            time.sleep(1)
        elif answer == STOPPEN:
            Layer1 = False
            break
        else:
            leeg_scherm()
            print_header()
            print_header_regel("Onjuist, " + value + " betekent " + key + ".")
            print_regel()
            print_regel("Vul Enter in om verder te gaan")
            print_regel("Vul " + STOPPEN + " in om te stoppen.")
            print_regel("vul " + DELETE + " in om het woord te verwijderen.")
            print_footer()
            Layer2 = True
            while Layer2 == True:
                answertwo = input()
                if answertwo == "":
                    Layer2 = False
                elif answertwo == STOPPEN:
                    Layer2 = False
                    Layer1 = False
                elif answertwo == DELETE:
                    verwijder_woord(key, woordenlijst, wrdbk)
                    Layer2 = False
                    Layer1 = False
                else:
                    print("Vul Enter, " + STOPPEN + " of " + DELETE + " in.")
                    time.sleep(2)

#Deze functie toont een afscheidsbericht
def print_afscheid():
    print("-"*SCHERMBREEDTE)
    print(f"|{'Doei!':^{SCHERMBREEDTE-2}}|")
    print("-"*SCHERMBREEDTE)

#Deze functie print een header
def print_header():
    print("-"*SCHERMBREEDTE)
    print(f"|{' ':{SCHERMBREEDTE-2}}|")

#Deze functie print een footer
def print_footer():
    print(f"|{' ':{SCHERMBREEDTE-2}}|")
    print("-"*SCHERMBREEDTE)

#Deze functie toont het menu
def print_menu(lijst_naam):
    print_header()
    print(f"|{'Menu':^{SCHERMBREEDTE-2}}|")
    print(f"|{lijst_naam:^{SCHERMBREEDTE-2}}|")
    print("|" + " "*(SCHERMBREEDTE-2) + "|")
    print(f"| {NIEUWE_LIJST + '. nieuwe woordenlijst maken':<{SCHERMBREEDTE-4}} |")
    print(f"| {KIES_LIJST + '. veranderen van woordenlijst':<{SCHERMBREEDTE-4}} |")
    print(f"| {TOEVOEGEN + '. woorden toevoegen aan een woordenlijst':<{SCHERMBREEDTE-4}} |")
    print(f"| {OVERHOREN + '. woordenlijsten overhoren':<{SCHERMBREEDTE-4}} |")
    print(f"| {STOPPEN + '. stoppen met het programma':<{SCHERMBREEDTE-4}} |")
    print_footer()

#Deze functie print een regel
def print_regel(inhoud=''):
    print(f"| {inhoud:<{SCHERMBREEDTE-4}} |")

#Deze functie print een header regel
def print_header_regel(inhoud=''):
    print(f"| {inhoud:^{SCHERMBREEDTE-4}} |")

#Deze functie shcrijft woorden over door naar elke rij te kijken en te copieren totdat hij klaar is
def schrijf_woordenlijst(bestandsnaam, woordenlijst):
    f = open(bestandsnaam, 'w')
    for key, value in woordenlijst.items():
        f.write(f"{key}{SCHEIDER}{value}\n")
    f.close()

#Deze functie verwijdert een woord in een dictionairy en wordt overgeschreven naar het bestand
def verwijder_woord(woord, woordenlijst, naam):
    leeg_scherm()
    print_header()
    print_header_regel("Weet je het zeker?")
    print_footer()
    del_loop = True
    while del_loop == True:
        answer = input()
        if answer == "ja":
            del woordenlijst[woord]
            schrijf_woordenlijst(naam, woordenlijst)
            del_loop = False
        elif answer == "nee":
            del_loop = False
            pass
        else:
            print("Vul ja of nee in.")

#Deze functie voegt woorden toe aan een dictionairy een schrijft het over naar een bestand
def voeg_woorden_toe(woordenlijst):
    woordenboek = lees_woordenlijst(woordenlijst)
    while True:
        woord1 = input("1. Wat is het Nederlandse woord? ")
        if woord1 == STOPPEN:
            break
        woord2 = input("2. Wat is het andere woord? ")
        if woord2 == STOPPEN:
            break
        print("-" * SCHERMBREEDTE)
        woordenboek[woord1] = woord2
    schrijf_woordenlijst(woordenlijst, woordenboek)

main()