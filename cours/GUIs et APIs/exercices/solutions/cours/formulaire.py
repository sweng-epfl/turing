#!/usr/bin/env python3

import tkinter

# Crée la fenêtre principale
root = tkinter.Tk()

# Optionnel : Augmente la taille des contrôles Tkinter, très petits par défaut
root.tk.call('tk', 'scaling', 2.5)

# Définit le titre et la taille de la fenêtre principale, ainsi que sa position à l'écran
root.title("Exercice")

# Crée les labels pour prénom et nom de famille
givenlabel = tkinter.Label(root, text = "Prénom")
givenlabel.grid(row=0, column=0, padx=10)

familylabel = tkinter.Label(root, text = "Nom de famille")
familylabel.grid(row=1, column=0, padx=10)

# Crée les entrées textuelles pour prénom et nom de famille
givenentry = tkinter.Entry(root)
givenentry.grid(row=0, column=1)

familyentry = tkinter.Entry(root)
familyentry.grid(row=1, column=1)

# Crée l'échelle de l'âge et son label
agelabel = tkinter.Label(root, text="Âge")
agelabel.grid(row=0, column=2)
agescale = tkinter.Scale(root, from_=1, to=120, orient="v")
agescale.grid(row=1, column=2, rowspan=3)

# Crée le radiobutton étudiant/professeur
role = tkinter.IntVar()
role.set(0)
studradio = tkinter.Radiobutton(root, text="Étudiant", variable=role, value=0)
profradio = tkinter.Radiobutton(root, text="Professeur", variable=role, value=1)
studradio.grid(row=2, column=0)
profradio.grid(row=2, column=1)

# Crée le choix "végétarien"
veggie = tkinter.BooleanVar()
veggie.set(False)
veggiebox = tkinter.Checkbutton(root, text="Végétarien(ne)", variable=veggie)
veggiebox.grid(row=3, column=1, pady=10)

# Crée le bouton
import tkinter.messagebox as msg
def onclick():
  text = givenentry.get() + " " + familyentry.get() + ", " \
       + str(agescale.get()) + " an(s), " \
       + ("étudiant" if role.get() == 0 else "professeur") + " " \
       + ("végétarien" if veggie.get() else "")
  msg.Message().show(message=text, type=msg.OK)
bt = tkinter.Button(root, text="Confirmer", command=onclick, padx=100)
bt.grid(row=4, columnspan=3, pady=20)

# Lance la boucle principale Tkinter : affichage + attente d'entrée utilisateur
root.mainloop()
