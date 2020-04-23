import random
# affichage du message de bienvenue
print("Bienvenue sur la machine à sous Fruitiiii")
# liste stockant le nom de chaque fruit
fruits = ["ananas", "cerise", "orange", "pasteque", "pomme_doré"]

# choix au hasard 
hasard = random.choices(fruits, k=3)

print(hasard)