#!/usr/bin/env python

import random

class Presenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def onInput(self):
        self.view.show("Météo actuelle : " + self.model.getForecast())

    def run(self):
        self.view.show("Bonjour!")
        self.view.run(self)

class FakeModel:
    def getForecast(self):
        weather = random.randrange(0, 4)
        if weather == 0:
            return "Ensoleillé"
        elif weather == 1:
            return "Pluvieux"
        else:
            return "???"

class ConsoleView:
    def show(self, text):
        print(text)

    def run(self, presenter):
        while True:
            input("Appuyez sur Entrée pour vérifier la météo (ou Ctrl+C pour quitter)")
            presenter.onInput()

Presenter(FakeModel(), ConsoleView()).run()
