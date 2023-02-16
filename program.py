DELETE = 'd'
EXTENSIE = '.txt'
KIES_LIJST = 'k'
MAX_WOORDLENGTE = 20
NIEUWE_LIJST = 'n'
OPSLAAN = 'w'
OVERHOREN = 'o'
SCHEIDER = '='
SCHERMBREEDTE = 50
SCHERMHOOGTE = 40
STANDAARD_LIJST = 'EN-NED'
STOPPEN = 'q'
TOEVOEGEN = 't'

def kies_lijst(lijst_naam):
    #?
    print("")

def leeg_scherm():
    #Maakt het terminalscherm leeg
    print("")

def lees_woordenlijst(bestandsnaam):
    f = open(bestandsnaam)
    for line in f:
        woord1, woord2 = line.strip('\n').split(SCHEIDER)
        woordenlijst[woord1] = woord2
    f.close()
    return woordenlijst

def main():
    choice = input("Uw keuze: ")
    if choice == EXTENSIE:
        print("")
    elif choice == KIES_LIJST:
        KIES_LIJST
    elif choice == TOEVOEGEN:
        TOEVOEGEN
    elif choice == OVERHOREN:
        overhoren()
    elif choice == STOPPEN:
        exit
    else:
        print("")

    #Gebruikt: STANDAARD_LIJST, KIES_LIJST, OVERHOREN, TOEVOEGEN, EXTENSIE, STOPPEN
    #Parameters: Geen
    #Returnwaarde: Geen

def nieuwe_lijst_naam():
    #Gebruikt: -
    #Parameters: -
    #Returnwaarde: de lijst_naam van de nieuw gekozen lijst
    print("")

def overhoren(woordenlijst):
    #Blijf woorden overhoren totdat de gebruiker aangeeft te willen stoppen.
    #Gebruikt: STOPPEN
    #Parameters: de woordenlijst die overhoord moet worden
    #Returnwaarde: -
    print("")

def print_afscheid():
    #Print een afscheidboodschap nadat het programma is afgesloten
    #Gebruikt: SCHERMHOOGTE, SCHERMBREEDTE
    #Parameters: -
    #Returnwaarde: -
    print("")

def print_header():
    print("-"*SCHERMBREEDTE)
    print(f"|{' ':{SCHERMBREEDTE-2}}|")

def print_footer():
    print(f"|{' ':{SCHERMBREEDTE-2}}|")
    print("-"*SCHERMBREEDTE)

def print_menu(lijst_naam):
    print("-"*SCHERMBREEDTE)
    print(f"|{'Menu':^{SCHERMBREEDTE-2}}|")
    print(f"|{lijst_naam:^{SCHERMBREEDTE-2}}|")
    print("|" + " "*(SCHERMBREEDTE-2) + "|")
    print(f"| {'1. nieuwe woordenlijst maken':<{SCHERMBREEDTE-4}} |")
    print(f"| {'2. veranderen van woordenlijst':<{SCHERMBREEDTE-4}} |")
    print(f"| {'3. woorden toevoegen aan een woordenlijst':<{SCHERMBREEDTE-4}} |")
    print(f"| {'4. woordenlijsten overhoren':<{SCHERMBREEDTE-4}} |")
    print(f"| {'5. stoppen met het programma':<{SCHERMBREEDTE-4}} |")
    print("-"*SCHERMBREEDTE)
    #Print het (keuze)menu inclusief de geselecteerde lijst
    #Gebruikt: SCHERMHOOGTE, SCHERMBREEDTE
    #Parameters: De naam van de geselecteerde woordenlijst
    #Returnwaarde: -

def print_regel(inhoud=''):
    #print_regel() print de inhoud links uitgelijnd uit.
    #Voor de inhoud wordt '| ' gezet en rechts uitgelijnd ' |'.
    #Bijvoorbeeld:
    #SCHERMBREEDTE = 30
    #inhoud = "Mooi zeg"
    #Uitvoer:
    #| Mooi zeg                   |
    #Gebruikt: SCHERMBREEDTE
    #Parameters: de string die geprint moet worden in de regel
    #Returnwaarde: -
    print("")

def schrijf_woordenlijst(bestandsnaam, woordenlijst):
    f = open("stowage.txt", 'w')
    for key, value in woordenlijst.items():
        f.write(f"{key}{SCHEIDER}{value}\n")
    f.close()
    woordenlijst = { "koe": "cow", "schaap": "sheep", "varken": "pig" }
    schrijf_woordenlijst("stowage.txt", woordenlijst)

def verwijder_woord(woord, woordenlijst):
    #Vraagt of gebruiker zeker weet of er verwijderd moet worden.
    #Verwijdert het woord en de vertaling uit de lijst als dit zo is.
    #Gebruikt: -
    #Parameters: het woord dat verwijderd moet worden, de woordenlijst waaruit verwijderd moet worden
    #Returnwaarde: -
    print("")

def voeg_woorden_toe(woordenlijst, lijst_naam):
    #Vraag de gebruiker steeds om woordenparen en voeg ze toe aan de lijst.
    #Stop als de gebruiker aangeeft te willen stoppen.
    #Gebruikt: SCHEIDER, STOPPEN
    #Parameters: de woordenlijst waarin toegevoegd moet worden, de lijst_naam van deze woordenlijst
    #Returnwaarde: -
    print("")
