def kies_lijst(lijst_naam):
    print("temp")

def leeg_scherm():
    Maakt het terminalscherm leeg

    Gebruikt: -
    Parameters: -
    Returnwaarde: -

def lees_woordenlijst(bestandsnaam):
    Leest de woordparen in uit het bestand genaamd 'bestandsnaam'.

    Gebruikt: SCHEIDER
    Parameter: naam van het bestand waar de woordenlijst in staat
    Returnwaarde: een dictionary met woordparen

def main():
    print("-"*50)
    print(f"|{'Menu':^48}|")
    print("|" + " "*48 + "|")
    print(f"| {'1. nieuwe woordenlijst maken':<46} |")
    print(f"| {'2. veranderen van woordenlijst':<46} |")
    print(f"| {'3. woorden toevoegen aan een woordenlijst':<46} |")
    print(f"| {'4. woordenlijsten overhoren':<46} |")
    print(f"| {'5. stoppen met het programma':<46} |")
    print("-"*50)
    choice = input("Uw keuze: ")
    if choice == "1":
        TOEVOEGEN()
    elif choice == "2":

    elif choice == "3":

    elif choice == "4":
        OVERHOREN()
    elif choice == "5":
        exit
    else:

    Gebruikt: STANDAARD_LIJST, KIES_LIJST, OVERHOREN, TOEVOEGEN, EXTENSIE, STOPPEN
    Parameters: Geen
    Returnwaarde: Geen

def nieuwe_lijst_naam():
    Gebruikt: -
    Parameters: -
    Returnwaarde: de lijst_naam van de nieuw gekozen lijst

def overhoren(woordenlijst):
    Blijf woorden overhoren totdat de gebruiker aangeeft te willen stoppen.

    Gebruikt: STOPPEN
    Parameters: de woordenlijst die overhoord moet worden
    Returnwaarde: -

def print_afscheid():
    Print een afscheidboodschap nadat het programma is afgesloten

    Gebruikt: SCHERMHOOGTE, SCHERMBREEDTE
    Parameters: -
    Returnwaarde: -

def print_footer():
    Print het volgende over de hele breedte van het scherm:
    |             |
    ===============
    Dus een volle regel met '='-tekens en een regel die begint en eindigt met een '|'.

    Gebruikt: SCHERMBREEDTE
    Parameters: -
    Returnwaarde: -

def print_header():
    Print het volgende over de hele breedte van het scherm:
    ===============
    |             |
    Dus een volle regel met '='-tekens en een regel die begint en eindigt met een '|'.

    Gebruikt: SCHERMBREEDTE
    Parameters: -
    Returnwaarde: -

def print_menu(lijst_naam):
    Print het (keuze)menu inclusief de geselecteerde lijst

    Gebruikt: SCHERMHOOGTE, SCHERMBREEDTE
    Parameters: De naam van de geselecteerde woordenlijst
    Returnwaarde: -

def print_regel(inhoud=''):
    print_regel() print de inhoud links uitgelijnd uit.
    Voor de inhoud wordt '| ' gezet en rechts uitgelijnd ' |'.
    Bijvoorbeeld:
    SCHERMBREEDTE = 30
    inhoud = "Mooi zeg"
    Uitvoer:
    | Mooi zeg                   |

    Gebruikt: SCHERMBREEDTE
    Parameters: de string die geprint moet worden in de regel
    Returnwaarde: -

def schrijf_woordenlijst(bestandsnaam, woordenlijst):
    Schrijft de woordparen weg naar het bestand genaamd 'bestandsnaam'.
    De oude inhoud van het bestand wordt overschreven!

    Gebruikt: SCHEIDER
    Parameter: naam van het bestand waar de woordenlijst in geschreven wordt, woordenlijst die weggeschreven wordt
    Returnwaarde: -

def verwijder_woord(woord, woordenlijst):
    Vraagt of gebruiker zeker weet of er verwijderd moet worden.
    Verwijdert het woord en de vertaling uit de lijst als dit zo is.

    Gebruikt: -
    Parameters: het woord dat verwijderd moet worden, de woordenlijst waaruit verwijderd moet worden
    Returnwaarde: -

def voeg_woorden_toe(woordenlijst, lijst_naam):
    Vraag de gebruiker steeds om woordenparen en voeg ze toe aan de lijst.
    Stop als de gebruiker aangeeft te willen stoppen.

    Gebruikt: SCHEIDER, STOPPEN
    Parameters: de woordenlijst waarin toegevoegd moet worden, de lijst_naam van deze woordenlijst
    Returnwaarde: -

#DATA
    DELETE = 'd'
    EXTENSIE = '.wrd'
    KIES_LIJST = 'k'
    MAX_WOORDLENGTE = 20
    NIEUWE_LIJST = 'n'
    OPSLAAN = 'w'
    OVERHOREN = 'o'
    SCHEIDER = '='
    SCHERMBREEDTE = 80
    SCHERMHOOGTE = 40
    STANDAARD_LIJST = 'EN-NED'
    STOPPEN = 'q'
    TOEVOEGEN = 't'