# zak alexandre kiraly
# tp3
# 2023

import random

recommencer = True
# valeurs de début
VieP = 20
ForceA = 1

# message d'acceuil
choix = int(input('''Vous vous balladez dans une prairie lorsque vous croisez un adversaire de difficultée, que voulez-vous faire? \n
1- Combattre cet adversaire\n
2- Contourner cet adversaire et aller ouvrir une autre porte \n
3- Afficher les règles du jeu \n
4- Quitter la partie '''))

if choix = 1:
    De1 = random.randint(1, 6)
    if De1 < 5:
        print('Attaque réussie! +4pv')
        VieP +4
    else:
        print('attaque non réussie, -4pv')
        VieP -4
if choix = 2:
    print('vous fuyer. -1pv')
    VieP -1
if choix = 3:
if choix = 4: