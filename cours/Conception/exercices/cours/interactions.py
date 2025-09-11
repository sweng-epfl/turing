#!/usr/bin/env python3

# Exercice 1 : Déplacez le code interagissant avec l'utilisateur
#              dans une nouvelle classe appelée UI.
#              Après vos modifications, le code hors de la classe
#              ne devrait plus avoir de `print`/`input`,
#              et n'avoir besoin que de créer un objet UI()
#              et d'appeler des méthodes dessus pour définir des variables,
#              elle-mêmes passées à des méthodes appelées sur l'UI.

print('Bonjour !')

name = None
while not name:
    print('Quel est votre nom ?')
    name = input()

print('Bienvenue, ' + name + '!')


hobby = None
while not hobby:
    print('Quel est votre passe-temps préféré ?')
    hobby = input()

print(hobby + ', quelle bonne idée !')





# Exercice 2 : Ajoutez un paramètre de constructeur à votre classe UI
#              pour qu'elle fonctionne en mode "silencieux",
#              c'est-à-dire aucun "print" sur la console
#              (typiquement une option offerte par les programmes qui peuvent être utilisé dans des scripts)
