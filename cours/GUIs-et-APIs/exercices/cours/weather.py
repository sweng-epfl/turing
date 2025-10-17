#!/usr/bin/env python

# Exercice : Convertissez cette application pour utiliser le pattern MVP, donc :
#            un "model" qui contient la logique, une "view" dédiée à l'affichage et aux interactions utilisateur, et un "presenter" qui médie

import random

# Ancienne application (supprimez le code une fois que vous l'avez déplacé là où il faut) :
print("Bonjour!")
while True:
    input("Appuyez sur Entrée pour vérifier la météo (ou Ctrl+C pour quitter)")
    weather = random.randrange(0, 4)
    if weather == 0:
        print("Météo actuelle : Ensoleillé")
    elif weather == 1:
        print("Météo actuelle : Pluvieux")
    else:
        print("Météo actuelle : ???")


# Nouvelle application :

# On commence par le médiateur : le "presenter", qui lie le "model" et la "view"
class Presenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def onInput(self):
        """Méthode à appeler quand la View reçoit une entrée, lui demandant d'afficher la météo."""
        self.view.show("Météo actuelle : " + self.model.getForecast())

    def run(self):
        """Méthode à appeler pour démarrer l'application."""
        self.view.show("Bonjour!")
        self.view.run(self)

# Partie 1 : définissez le model, pour qu'il soit utilisable par le Presenter et qu'il ait le même comportement que l'ancienne app, soit une fausse météo
class FakeModel:
    pass

# Partie 2 : définissez la view, même objectif, soit une ligne de commande
class ConsoleView:
    pass

# On lance l'application en créant un Presenter avec nos implémentations de Model et View
Presenter(FakeModel(), ConsoleView()).run()
