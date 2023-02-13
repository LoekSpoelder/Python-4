#with open("stowage.txt") as f:
#  bestandsdata = f.read().split("\n")
#for item in bestandsdata:
#  woord1, woord2 = item.split("=")
#  woordenlijst[woord1] = woord2

#f = open('stowage.txt')
#for line in f:
#  woord1, woord2 = line.strip('\n').split('=')
#  woordenlijst[woord1] = woord2
#f.close('stowage.txt')

#def lees_woordenlijst(bestandsnaam):
#  SCHEIDER = '='
#  woordenlijst = {}
#  with open(bestandsnaam) as f:
#    bestandsdata = f.read().split("\n")
#  for item in bestandsdata:
#    woord1, woord2 = item.split(SCHEIDER)
#    woordenlijst[woord1] = woord2
#  return woordenlijst
#def main():
#  lijst = lees_woordenlijst("stowage.txt")
#  print(lijst)
#main()

def schrijf_woordenlijst(bestandsnaam, woordenlijst):
  SCHEIDER = '='
  f = open("stowage.txt", 'w')
  for key, value in woordenlijst.items():
    f.write(f"{key}{SCHEIDER}{value}\n")
  f.close()
woordenlijst = { "koe": "cow", "schaap": "sheep", "varken": "pig" }
schrijf_woordenlijst("stowage.txt", woordenlijst)