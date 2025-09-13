#!/usr/bin/env python3
import tkinter as tk
import tkinter.messagebox as msg

class GraphicalUI:
  def say(self, text):
      msg.Message().show(message=text, type=msg.OK)

  def ask(self, text):
      window = tk.Tk()
      tk.Label(window, text=text).grid(row=0)
      e = tk.Entry(window)
      e.grid(row=0, column=1)
      tk.Button(window, text='OK', command=lambda: window.quit() if e.get() else None).grid(row=1)
      tk.mainloop()
      result = e.get()
      window.destroy()
      return result

ui = GraphicalUI()
ui.say('Bonjour !')
name = ui.ask('Quel est votre nom ?')
ui.say('Bienvenue, ' + name + '!')
hobby = ui.ask('Quel est votre passe-temps préféré ?')
ui.say(hobby + ', quelle bonne idée !')
