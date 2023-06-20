import os, time, random
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
woordenboek = {}

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

def leeg_scherm():
    os.system('cls')

def lees_woordenlijst(bestandsnaam):
    f = open(bestandsnaam)
    for line in f:
        woord1, woord2 = line.strip('\n').split(SCHEIDER)
        woordenboek[woord1] = woord2
    f.close()
    return woordenboek

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
            voeg_woorden_toe(wrdbk, lees_woordenlijst(wrdbk))
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

def nieuwe_lijst_naam(lijst):
    return lijst.strip(EXTENSIE)

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

def print_afscheid():
    print("-"*SCHERMBREEDTE)
    print(f"|{'Doei!':^{SCHERMBREEDTE-2}}|")
    print("-"*SCHERMBREEDTE)

def print_header():
    print("-"*SCHERMBREEDTE)
    print(f"|{' ':{SCHERMBREEDTE-2}}|")

def print_footer():
    print(f"|{' ':{SCHERMBREEDTE-2}}|")
    print("-"*SCHERMBREEDTE)

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

def print_regel(inhoud=''):
    print(f"| {inhoud:<{SCHERMBREEDTE-4}} |")

def print_header_regel(inhoud=''):
    print(f"| {inhoud:^{SCHERMBREEDTE-4}} |")

def schrijf_woordenlijst(bestandsnaam, woordenlijst):
    woordenlijst = {}
    woordenlijst = lees_woordenlijst(bestandsnaam) 
    f = open(bestandsnaam, 'w')
    for key, value in woordenlijst.items():
        f.write(f"{key}{SCHEIDER}{value}\n")
    f.close()

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

def voeg_woorden_toe(woordenlijst, lijst):
    while True:
        woord1 = input("1. Wat is het Nederlandse woord? ")
        if woord1 == STOPPEN:
            break
        woord2 = input("2. Wat is het andere woord? ")
        if woord2 == STOPPEN:
            break
        print("-"*SCHERMBREEDTE)
        lijst[woord1] = woord2
    schrijf_woordenlijst(woordenlijst, lijst)

#woordenlijst word gecloned als je een woord toevoegd, verandert van lijst, en weer een woord toevoegd.

main()