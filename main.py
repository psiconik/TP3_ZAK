# zak alexandre kiraly
# tp3
# 2023

import random

recommencer = True
# valeurs de début
VieP = 20
NumA = 0
NumC = 0
NumV = 0
NumD = 0
while VieP > 0:
    ForceA = random.randint(1, 5)


    # message d'acceuil
    Stats = print(f'''Adversaire : {NumA} \n Force de l’adversaire : `{ForceA} \n Niveau de vie de l’usager : {VieP} \n Combat {NumC} : {NumV} victoires vs nombre_defaites''')
    choix = int(input(f'''Vous vous balladez dans une prairie lorsque vous croisez un adversaire de difficultée {ForceA}, que voulez-vous faire? \n
    1- Combattre cet adversaire\n
    2- cet adversaire et aller ouvrir une autre porte \n
    3- Afficher les règles du jeu \n
    4- Quitter la partie \n '''))
    NumA =+ 1
    if choix == 1:
        NumC =+ 1
        if ForceA == 1:
            De1 = random.randint(1, 10)
            if De1 < 7:
                print('Attaque réussie! +4pv')
                VieP += 4
                NumV += 1
                continue
            else:
                print('attaque non réussie, -4pv')
                VieP -= 4
                NumD += 1
                continue
        if ForceA == 2:
            De1 = random.randint(1, 10)
            if De1 < 6:
                print('Attaque réussie! +4pv')
                VieP += 4
                NumV += 1
                continue
            else:
                print('attaque non réussie, -4pv')
                VieP -= 4
                NumD += 1
                continue
        if ForceA == 3:
            De1 = random.randint(1, 10)
            if De1 < 5:
                print('Attaque réussie! +4pv')
                VieP += 4
                NumV += 1
                continue
            else:
                print('attaque non réussie, -4pv')
                VieP -= 4
                NumD += 1
                continue
        if ForceA == 4:
            De1 = random.randint(1, 10)
            if De1 < 4:
                print('Attaque réussie! +4pv')
                VieP += 4
                NumV += 1
                continue
            else:
                print('attaque non réussie, -4pv')
                VieP -= 4
                NumD += 1
                continue
        if ForceA == 5:
            De1 = random.randint(1, 10)
            if De1 < 3:
                print('Attaque réussie! +4pv')
                VieP += 4
                NumV += 1
                continue
            else:
                print('attaque non réussie, -4pv')
                VieP -= 4
                NumD += 1
                continue
    if choix == 2:
        print('vous fuyer. -1pv')
        VieP -= 1
        continue
    if choix == 3:
        print('''Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire. \n 
        Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\n
        Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire. \n 
        Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire. \n
        La partie se termine lorsque les points de vie de l’usager tombent sous 0. \n
        L’usager peut combattre ou éviter chaque adversaire. \n
        Dans le cas de l’évitement, il y a une pénalité de 1 point de vie.''')
        continue
    if choix == 4:
        input('Ok, alors merci et au revoir...')
        break
    if choix == 5:
        print(f'Vous avez {VieP}pv')
        continue