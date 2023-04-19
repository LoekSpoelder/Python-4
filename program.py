import os, time
DELETE = 'd'
EXTENSIE = '.txt'
KIES_LIJST = 'k'
MAX_WOORDLENGTE = 20
NIEUWE_LIJST = 'n'
OPSLAAN = 'w'
OVERHOREN = 'o'
SCHEIDER = '='
SCHERMBREEDTE = 50
STANDAARD_LIJST = 'stowage.txt'
STOPPEN = 's'
TOEVOEGEN = 't'
woordenboek = {}

def kies_lijst():
    leeg_scherm()
    stowage = os.listdir()
    stowage.remove(".git")
    stowage.remove("program.py")
    print_header()
    print_header_regel("De Huidige lijst is: " + nieuwe_lijst_naam())
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
        STANDAARD_LIJST = antwoord #defunct
    elif antwoord == STOPPEN:
        pass
    else:
        print("Dat is niet een woordenlijst.")
        kies_lijst()

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
    while True:
        leeg_scherm()
        print_menu(nieuwe_lijst_naam())
        keuze = input("Uw keuze: ")
        if keuze == NIEUWE_LIJST:
            print("")
        elif keuze == KIES_LIJST:
            kies_lijst()
        elif keuze == TOEVOEGEN:
            voeg_woorden_toe(woordenboek, STANDAARD_LIJST)
        elif keuze == OVERHOREN:
            overhoren(lees_woordenlijst(STANDAARD_LIJST))
        elif keuze == STOPPEN:
            leeg_scherm()
            print_afscheid()
            break
        else:
            print("Vul " + NIEUWE_LIJST + ", " + KIES_LIJST + ", " + TOEVOEGEN + ", " + OVERHOREN + " of " + STOPPEN + " in.")
            time.sleep(2)
            leeg_scherm()
    #Gebruikt: STANDAARD_LIJST, KIES_LIJST, OVERHOREN, TOEVOEGEN, EXTENSIE, STOPPEN
    #Parameters: Geen
    #Returnwaarde: Geen

def nieuwe_lijst_naam():
    return STANDAARD_LIJST.strip(EXTENSIE)

def overhoren(woordenlijst):
    dingle = True
    while dingle == True:
        for key, value in woordenlijst.items():
            print('Wat is de vertaling van "' + value + '".')
            answer = input()
            if answer == key:
                print("Juist, " + value + " betekent " + key + ".")
                print("-"*SCHERMBREEDTE)
            elif answer == STOPPEN:
                dingle = False
                break
            else:
                print("Onjuist, " + value + " betekent " + key + ".")
                print("-"*SCHERMBREEDTE)
    #Blijf woorden overhoren totdat de gebruiker aangeeft te willen stoppen.
    #Gebruikt: STOPPEN
    #Parameters: de woordenlijst die overhoord moet worden
    #Returnwaarde: -

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
    #Print het (keuze)menu inclusief de geselecteerde lijst
    #Gebruikt: SCHERMHOOGTE, SCHERMBREEDTE
    #Parameters: De naam van de geselecteerde woordenlijst
    #Returnwaarde: -

def print_regel(inhoud=''):
    print(f"| {inhoud:<{SCHERMBREEDTE-4}} |")

def print_header_regel(inhoud=''):
    print(f"| {inhoud:^{SCHERMBREEDTE-4}} |")

def schrijf_woordenlijst(bestandsnaam, woordenlijst):
    f = open(bestandsnaam, 'w')
    for key, value in woordenlijst.items():
        f.write(f"{key}{SCHEIDER}{value}\n")
    f.close()

def verwijder_woord(woord, woordenlijst):
    answer = input("Weet je het zeker? ")
    if answer == "ja":
        del woordenlijst[woord]
        schrijf_woordenlijst(STANDAARD_LIJST, woordenlijst)
    elif answer == "nee":
        pass
    else:
        print("Vul ja of nee in.")
        verwijder_woord("raam", lees_woordenlijst(STANDAARD_LIJST))
    #Vraagt of gebruiker zeker weet of er verwijderd moet worden.
    #Verwijdert het woord en de vertaling uit de lijst als dit zo is.
    #Gebruikt: -
    #Parameters: het woord dat verwijderd moet worden, de woordenlijst waaruit verwijderd moet worden
    #Returnwaarde: -

def voeg_woorden_toe(woordenlijst, STANDAARD_LIJST):
    lees_woordenlijst(STANDAARD_LIJST)
    while True:
        woord1 = input("1. Wat is het Nederlandse woord? ")
        if woord1 == STOPPEN:
            break
        woord2 = input("2. Wat is het Engelse woord? ")
        if woord2 == STOPPEN:
            break
        print("-"*SCHERMBREEDTE)
        woordenlijst[woord1] = woord2
    schrijf_woordenlijst(STANDAARD_LIJST, woordenlijst)
    #Vraag de gebruiker steeds om woordenparen en voeg ze toe aan de lijst.
    #Stop als de gebruiker aangeeft te willen stoppen.
    #Gebruikt: SCHEIDER, STOPPEN
    #Parameters: de woordenlijst waarin toegevoegd moet worden, de lijst_naam van deze woordenlijst
    #Returnwaarde: -

main()