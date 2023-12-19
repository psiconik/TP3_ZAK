# zak alexandre kiraly
# tp3
# 2023

import random
import time

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
    Stats = print(f'''Adversaire : {NumA} \nNiveau de vie de l’usager : {VieP} \nCombat {NumC} \n{NumV} victoires vs {NumD} defaites\n''')
    time.sleep(1)
    choix = int(input(f'''Vous vous balladez dans un château hanté lorsque vous croisez un adversaire de difficultée {ForceA}, que voulez-vous faire? \n
    1- Combattre cet adversaire\n
    2- fuir et aller dans une autre salle\n
    3- Afficher les règles du jeu \n
    4- Quitter la partie \n '''))
    NumA =+ 1
    if choix == 1:
        NumC =+ 1
        De1 = random.randint(1, 6)
        print(f'''votre lancer de dé = {De1}''')
        time.sleep(2)
        if De1 >= ForceA:
            print('''donc vous gagnez le combat, +4pv\n\n-------------------------------------------------------------------''')
            VieP += 4
            NumV += 1
            time.sleep(3)
        if De1 < ForceA:
            print('''donc vous perdez le combat, -4pv\n\n-------------------------------------------------------------------''')
            VieP -= 4
            NumD += 1
            time.sleep(2)
    if choix == 2:
        print('vous fuyer. -1pv')
        VieP -= 1
        time.sleep(2)
        #continue
    if choix == 3:
        print('''Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire. \n 
        Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\n
        Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire. \n 
        Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire. \n
        La partie se termine lorsque les points de vie de l’usager tombent sous 0. \n
        L’usager peut combattre ou éviter chaque adversaire. \n
        Dans le cas de l’évitement, il y a une pénalité de 1 point de vie.''')
        time.sleep(6)
        #continue
    if choix == 4:
        input('Ok, alors merci et au revoir...')
        time.sleep(1)
        break