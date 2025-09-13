#!/usr/bin/env python3

class UI:
  def say(self, txt):
      print(txt)

  def ask(self, txt):
      result = None
      while not result:
          print(txt)
          result = input()
      return result

ui = UI()
ui.say('Bonjour !')
name = ui.ask('Quel est votre nom ?')
ui.say('Bienvenue, ' + name + '!')
hobby = ui.ask('Quel est votre passe-temps préféré ?')
ui.say(hobby + ', quelle bonne idée !')
