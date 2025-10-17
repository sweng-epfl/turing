# Interfaces graphiques et APIs

Quand on programme pour soi-même, il est souvent plus simple de créer une interface en ligne de commande basique.
De plus, beaucoup de petits scripts et programmes simples ne communiquent pas avec le reste du monde, ou le font via des fichiers téléchargés manuellement.

Mais pour développer un produit logiciel, il est en général nécessaire d'avoir une interface _graphique_, et de communiquer avec des services externes via des _APIs_, pour "Application Programming Interfaces".
De plus, il est souvent nécessaire d'extraire la logique réutilisable d'une application pour pouvoir développer plusieurs interfaces, par exemple mobile et bureau, et pour réutiliser certains modules dans différentes applications.


## Objectifs

Après ce cours, vous devriez être en mesure de :
- Concevoir des interfaces utilisateur graphiques
- Interagir avec des services externe via des APIs
- Organiser le code avec des design patterns
- Découpler l'UI, la logique, et les strategies réutilisables


## Comment concevoir une interface graphique ?

Il y a en gros deux types de contrôles dans une interface graphique : les entrées et les sorties.
Les entrées incluent des entrées de texte, de nombres, de fichiers, et d'autres types de données, ainsi que des exécutions de fonctions via, par exemple, des boutons.
Certaines entrées sont plus spécifiques, par exemple "addresse email" et non simplement "texte".
Les sorties incluent de l'affichage de texte, d'image, de son, et d'autres types de données.

En général, tant les entrées que les sorties ont des _propriétés_ communes, telles que leur visibilité (visible, caché), leur opacité, la couleur du texte s'il y en a, la couleur de fond, et bien d'autres.
De plus, les contrôles dans une interface utilisateur fournissent des _évènements_, c'est-à-dire un moyen d'appeler des fonctions spécifiques quand quelque chose se passe, comme "clic", "double clic", ou "clic droit".

Les interfaces utilisateurs sont en général modélisées à l'aide de concepts orientés objets, soit l'héritage et la composition.
Par exemple, une classe de base représente tous les contrôles, et a des sous-classes telles que "boîte d'entrée de texte", "label", et "image".
La boîte d'entrée de texte peut elle-même avoir une sous-classe pour entrer un mot de passe, qui montre des astérisques au lieu du mot de passe que l'utilisateur écrit.
De plus, des contrôles en contiennent d'autres, comme par exemple une liste d'onglets qui chacun peut contenir d'autres contrôles.
Un onglet qui affiche une image n'_est pas_ une image, mais il _a_ une image, c'est donc de la composition et non de l'héritage.

Avant de passer à un exemple, voyons concepts généraux qui sont présents dans les interfaces graphiques quel que soit le langage ou framework.
D'abord, les marges, typiquement le "padding" qui est une marge à l'intérieur d'un contrôle parent et la marge à l'extérieur d'un contrôle enfant :

<p align="center"><img alt="Illustration des deux types de marges" src="images/marges.svg" width="50%" /></p>

Ensuite, la mise en page. Il existe énormément de types de mise en page, comme les grilles dans lesquels chaque contrôle occuppe une ou plusieurs cellules, l'entassement horizontal ou vertical, et bien d'autres :

<p align="center"><img alt="Illustration de deux types de mise en page" src="images/mise-en-page.svg" width="50%" /></p>


### Exemple en Python : `tkinter`

Le framework `tkinter` en Python est intégré à la librairie standard, raison pour laquelle nous allons l'utiliser comme exemple.
Chaque framework d'interface graphique fait certaines tâches de manière différente, mais les concepts généraux sont les mêmes.

Créez un fichier Python et commencez par importer `tkinter` :
```python
import tkinter
```

Ensuite, créez une fenêtre principale, donnez-lui un nom, et définissez sa taille :
```python
# Créee la fenêtre principale
root = tkinter.Tk()
# Optionnel : Augmente la taille des contrôles Tkinter, très petits par défaut
root.tk.call('tk', 'scaling', 2.5)
# Définit le titre et la taille de la fenêtre principale, ainsi que sa position à l'écran
root.title("Exercice")
root.geometry("500x700+200+200")
```

Vous pouvez maintenant afficher la fenêtre :
```python
# Lance la boucle principale Tkinter : affichage + attente d'entrée utilisateur
root.mainloop()
```
Cela lance la fenêtre, qui est évidemment vide.

Le reste du code de cet exemple doit apparaître **avant l'appel à `mainloop`**.

Commençons par afficher du texte à l'aide d'un `Label` :
```python
label = tkinter.Label(root, text = "Hello, World!")
label.grid(row=0, column=0)
```
Si vous lancez le code, vous devriez voir une fenêtre avec le texte "Hello, World!" en haut à gauche.
Nous avons placé le label sur la ligne 0 et colonne 0, ce qui ne change rien pour l'instant puisqu'il n'y a rien d'autre.

Ajoutons donc une entrée textuelle, le contrôle `Entry` :
```python
entry = tkinter.Entry(root)
entry.grid(row=0, column=1)
```
Si vous lancez le code, vous verrez une boîte de texte directement à droite du texte "Hello, World!", puisque l'`Entry` est sur la colonne 1 mais toujours sur la ligne 0.

Maintenant, un bouton :
```python
bt = tkinter.Button(root, text="Click", padx=60, pady=5)
bt.grid(row=1, columnspan=2, pady=20)
```
Ce bouton existe mais ne fait rien.
Remarquez que avec `columnspan=2`, notre bouton s'étend ("spans" en anglais, d'où le nom de la propriété) sur deux colonnes, et avec `pady=20`, nous ajoutons de la marge à gauche et à droite du texte à l'intérieur.

Pour ajouter une commande, on peut `bind` l'évènement `<Button-1>` à une fonction qui affiche une fenêtre avec le texte de l'entrée :
```python
import tkinter.messagebox as msg
def onclick(e):
  msg.Message().show(message=entry.get(), type=msg.OK)
bt.bind("<Button-1>", onclick)
```
Lancez le code, écrivez du texte dans l'entrée textuelle, et cliquez sur le bouton.
Vous pouvez également changer l'évènement, par exemple `<Button-2>` est le clic droit, vous pouvez trouver [des listes en ligne](https://stackoverflow.com/a/32289245/3311770) de tous les évènements.

Ajoutons un autre type d'entrée, une boîte à cocher, souvent appelée "checkbox", que `tkinter` appelle `Checkbutton` :
```python
ck = tkinter.Checkbutton(root, text="Check me")
ck.grid(row=2)
```

Il existe bien d'autres types d'entrées, comme une échelle :
```python
scale = tkinter.Scale(root, from_=0, to=100, orient="h")
scale.grid(row=3, columnspan=2)
```

Ou même un choix de fichier. Cette fois, déclarons la commande directement dans la création d'un `Button`. Notez que dans ce cas la fonction ne prend aucun paramètre :
```python
from tkinter import filedialog
def openfile():
  path = filedialog.askopenfilename(title="Choose", filetypes=(("Text", "*.txt"),("All", "*.*")))
  # ...ici on pourrait faire quelque chose avec `path`...
bt2 = tkinter.Button(root, text="File", command=openfile)
bt2.grid(row=4)
```

Il serait possible d'écrire du code pour, par exemple, détecter les changements de texte dans l'entrée textuelle via un évènement, et les répercuter ailleurs.
Heureusement, les frameworks d'interface graphique ont en général des concepts de liaison entre contrôles et variables qui le font pour nous.
`tkinter` a des classes de variables comme `StringVar`, et les contrôles prennent ces variables comme propriétés.

Par exemple, une variable textuelle et un label qui l'affiche, que nous pouvons synchroniser avec l'entrée :
```python
v = tkinter.StringVar()
vlabel = tkinter.Label(root, textvariable=v)
vlabel.grid(row=5, columnspan=2)
entry.configure(textvariable=v)
```
Relancez l'application, écrivez du texte, et vous verrez que les changements sont immédiatement répércutés sur le nouveau label.

Il existe d'autre type de variables, comme un Booléen, que nous pouvons synchroniser avec la boîte à cocher :
```python
b = tkinter.BooleanVar()
blabel = tkinter.Label(root, textvariable=b)
blabel.grid(row=2, column=1)
ck.configure(variable=b)
```

Pour certains contrôles, le fait d'avoir une variable est en fait requis pour un fonctionnement correct, comme des boutons à choix unique dit "radio button" :
```python
i = tkinter.IntVar()
rb1 = tkinter.Radiobutton(root, text="First", variable=i, value=1)
rb2 = tkinter.Radiobutton(root, text="Second", variable=i, value=2)
rb3 = tkinter.Radiobutton(root, text="Third", variable=i, value=3)
rb1.grid(row=6)
rb2.grid(row=7)
rb3.grid(row=8)
```
(Le nom "radio button" vient des anciennes radios dans les voitures, qui possédaient plusieurs boutons pour choisir des fréquences prédéfinies. Seul un bouton peut être choisi à la fois, puisque la radio ne peut capter qu'une fréquence à la fois.)


#### Exercice

Créez un formulaire ressemblant à ceci :

<p align="center"><img alt="Illustration des deux types de marges" src="images/exercice-form.png" width="50%" /></p>

Quand l'utilisateur clique sur "Confirmer", l'application doit afficher l'information dans une nouvelle fenêtre :

<p align="center"><img alt="Illustration des deux types de marges" src="images/exercice-popup.png" width="25%" /></p>

Vous pouvez également consulter la [documentation `tkinter`](https://docs.python.org/3/library/tkinter.html) pour rendre votre fenêtre plus jolie.

Une solution est disponible [ici](exercices/solutions/cours/formulaire.py).

---
