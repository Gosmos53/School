from random import randint

# vad datorn ska göra 
val = ["sten","sax","påse"]
dator = val[randint(0,2)]



# allt som den skriver ut ibörjan
print("välkommen till mitt spel\n")
print("du kan välja mellan: sten, sax eller påse\n")
print("lycka till!\n")

# detta gör att spelaren kan skriva 
spelare = input("ditt val:").lower()

# att den ska skriva ut vad datorn har valt
print("datorn valde:" + dator)


# reglerna 
if spelare == dator:
    print("ovagjort") 
elif spelare == "sax" and dator == "sten":
    print("datorn vinner")
elif spelare == "påse" and dator == "sax":
    print("datron vinner")
elif spelare == "sten" and dator == "påse":
    print("datorn vinner")
elif spelare == "sten" and dator == "sax":
    print("spelare vinner")
elif spelare == "sax" and dator == "påse":
    print("spelaren vinner")
elif spelare == "påse" and dator == "sten":
    print("spelare vinner") 


