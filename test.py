with open("stowage.txt") as f:
  bestandsdata = f.read().split("\n")

for item in bestandsdata:
    woord1, woord2 = item.split("=")

print(woord1)
print(woord2)