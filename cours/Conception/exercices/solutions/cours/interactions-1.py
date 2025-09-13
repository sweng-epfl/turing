#!/usr/bin/env python3

class UI:
  def __init__(self, silent):
      self.silent = silent

  def say(self, text):
      if not self.silent:
          print(text)

  def ask(self, text):
      result = None
      while not result:
          self.say(text)
          result = input()
      return result

ui = UI(silent=False)
ui.say('Bonjour !')
name = ui.ask('Quel est votre nom ?')
ui.say('Bienvenue, ' + name + '!')
hobby = ui.ask('Quel est votre passe-temps préféré ?')
ui.say(hobby + ', quelle bonne idée !')
