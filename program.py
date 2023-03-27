import os, time
DELETE = 'd'
EXTENSIE = '.txt'
KIES_LIJST = '2'
MAX_WOORDLENGTE = 20
NIEUWE_LIJST = '1'
OPSLAAN = 'w'
OVERHOREN = '4'
SCHEIDER = '='
SCHERMBREEDTE = 50
STANDAARD_LIJST = 'stowage.txt'
STOPPEN = '5'
TOEVOEGEN = '3'
woordenlijst = {}

def kies_lijst(lijst_naam):
    #?
    print("")

def leeg_scherm():
    os.system('cls')

def lees_woordenlijst(bestandsnaam):
    f = open(bestandsnaam)
    for line in f:
        woord1, woord2 = line.strip('\n').split(SCHEIDER)
        woordenlijst[woord1] = woord2
    f.close()
    return woordenlijst

def main():
    print_menu(STANDAARD_LIJST.strip(EXTENSIE))
    keuze = input("Uw keuze: ")
    if keuze == NIEUWE_LIJST:
        print("")
    elif keuze == KIES_LIJST:
        KIES_LIJST
    elif keuze == TOEVOEGEN:
        TOEVOEGEN
    elif keuze == OVERHOREN:
        overhoren(lees_woordenlijst(STANDAARD_LIJST))
    elif keuze == STOPPEN:
        leeg_scherm()
        print_afscheid()
        exit
    else:
        print("Vul " + NIEUWE_LIJST + ", " + KIES_LIJST + ", " + TOEVOEGEN + ", " + OVERHOREN + " of " + STOPPEN + " in.")
        time.sleep(2)
        leeg_scherm()
        main()
    #Gebruikt: STANDAARD_LIJST, KIES_LIJST, OVERHOREN, TOEVOEGEN, EXTENSIE, STOPPEN
    #Parameters: Geen
    #Returnwaarde: Geen

def nieuwe_lijst_naam():
    #Gebruikt: -
    #Parameters: -
    #Returnwaarde: de lijst_naam van de nieuw gekozen lijst
    print("")

def overhoren(woordenlijst):
    for key, value in woordenlijst.items():
        print('Wat is de vertaling van "' + value + '".')
        answer = input()
        if answer == key:
            print("Juist, " + value + " betekent " + key + ".")
            print("-"*SCHERMBREEDTE)
        elif answer == STOPPEN:
            leeg_scherm()
            main()
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

def schrijf_woordenlijst(bestandsnaam, woordenlijst):
    f = open(STANDAARD_LIJST, 'w')
    for key, value in woordenlijst.items():
        f.write(f"{key}{SCHEIDER}{value}\n")
    f.close()

def verwijder_woord(woord, woordenlijst):
    #Vraagt of gebruiker zeker weet of er verwijderd moet worden.
    #Verwijdert het woord en de vertaling uit de lijst als dit zo is.
    #Gebruikt: -
    #Parameters: het woord dat verwijderd moet worden, de woordenlijst waaruit verwijderd moet worden
    #Returnwaarde: -
    print("")

def voeg_woorden_toe(woordenlijst, lijst_naam):
    woordenlijst = { "koe": "cow", "schaap": "sheep", "varken": "pig" }
    schrijf_woordenlijst("stowage.txt", woordenlijst)
    #Vraag de gebruiker steeds om woordenparen en voeg ze toe aan de lijst.
    #Stop als de gebruiker aangeeft te willen stoppen.
    #Gebruikt: SCHEIDER, STOPPEN
    #Parameters: de woordenlijst waarin toegevoegd moet worden, de lijst_naam van deze woordenlijst
    #Returnwaarde: -
    print("")

main()