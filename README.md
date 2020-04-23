### EN
# Context.
You are the manager of a commercial car park with
currently 27 spaces to accommodate vehicles from
mall customers.

  # Leval 1
Display "Welcome to level -1, what do you want to do?" "
Create a list called parking containing 27 spaces:
• The letter ‘D’ corresponds to an available space
• The letter ‘V’ corresponds to a space containing a
vehicle
• The letter ‘H’ corresponds to a space for people
with low mobility.
Show if location # 3 is available or unavailable
Place a car in the 1st parking space (n ° 0)
Display all parking spaces, specifying their
availabilities


  # Leval 2
  Suggest that the user enter the number 1 or 2
1. Allows him to park a car by specifying the number of
the location
2. Allows him to recover a car by specifying the number of
the location
Create a function display_parking () displaying the locations


  # Leval 3
After several months of operation, you have decided to enlarge
the parking lot by building the floor -2 and the floor -3 comprising
27 new locations respectively.
Make changes compared to the previous fiscal year to
take into account these two new floors.
Create a dictionary called unlocking codes, it will allow
set a secret code when a car is parked. If the code is
incorrect when unlocking, display “Stop! "
Unlock code format: AAAA-2222-XX


# Leval 4
Randomly define two locations on each floor being one
priority access for people with reduced mobility.
They cannot be selected except by giving a code
containing the following format HP-1111-X3:
- HP at the start + a dash + 4 digits + X3

See the regex tool (module re) : https://www.w3schools.com/python/python_regex.asp

### FR
# Contexte
Vous êtes le gérant d’un parking commercial comportant
actuellement 27 emplacements pour accueillir les véhicules des
clients du centre commercial.


  # Niveau 1
Afficher « Bienvenue au niveau -1, que souhaitez-vous faire ? »
Créer une liste nommé parking contenant 27 emplacements :
• La lettre ‘D’ correspond à un emplacement disponible
• La lettre ‘V’ correspond à un emplacement contenant un
véhicule
• La lettre ‘H’ correspond à un emplacement pour les personnes
à mobilité réduite.
Afficher si l’emplacement n°3 est disponible ou indisponible
Placer une voiture au 1er emplacement du parking (n°0)
Afficher tous les emplacements du parking en précisant leurs
disponibilités


  # Niveau 2
Proposer à l’utilisateur de d’entrer le chiffre 1 ou 2
1. Lui permet de garer une voiture en précisant le numéro de
l’emplacement
2. Lui permet de récupérer une voiture en précisant le numéro de
l’emplacement
Créer une fonction afficher_parking() affichant les emplacements


  # Niveau 3
Après plusieurs mois de fonctionnement, vous avez décidé d’agrandir
le parking en construisant l’étage -2 et l’étage -3 comportant
respectivement 27 nouveaux emplacements.
Apporter les modifications par rapport à l’exercice précédant pour
prendre compte ces deux nouveaux étages.
Créer un dictionnaire nommé codes_debloquage , il va permettre de
définir un code secret lorsqu’une voiture est garée. Si le code est
incorrect lors du déblocage, afficher « Stop ! »
Format du code de déblocage : AAAA-2222-XX


   # Niveau 4
Définir au hasard deux emplacements sur chaque étage étant un
accès prioritairement réservé aux personnes à mobilité réduite.
Ils ne pourront pas être sélectionné sauf en donnant un code
contenant le format suivant HP-1111-X3 soit :
- HP au départ + un tiret + 4 chiffres + X3

Voir l’outil regex (module re) : https://www.w3schools.com/python/python_regex.asp
