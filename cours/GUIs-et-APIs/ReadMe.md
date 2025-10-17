# Interfaces graphiques et APIs

Quand on programme pour soi-même, il est souvent plus simple de créer une interface en ligne de commande basique.
De plus, beaucoup de petits scripts et programmes simples ne communiquent pas avec le reste du monde, ou le font via des fichiers téléchargés manuellement.

Mais pour développer un produit logiciel, il est en général nécessaire d'avoir une interface _graphique_, et de communiquer avec des services externes via des _APIs_, pour "Application Programming Interfaces".
De plus, il est souvent nécessaire d'extraire la logique réutilisable d'une application pour pouvoir développer plusieurs interfaces, par exemple mobile et bureau, et pour réutiliser certains modules dans différentes applications.


## Objectifs

Après ce cours, vous devriez être en mesure de :
- Concevoir des interfaces utilisateur graphiques
- Organiser le code avec des design patterns
- Découpler l'UI, la logique, et les strategies réutilisables
- Interagir avec des services externes via des APIs


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

### Comment réutiliser des concepts dans plusieurs systèmes ?

Lors de la conception d'un système, le contexte est souvent le même que dans les systèmes précédents, tout comme les exigences des utilisateurs.
Par exemple, "traverser un cours d'eau" est une exigence et un contexte courants qui conduisent à la solution naturelle "construire un pont".
Si chaque ingénieur concevait le concept d'un pont à partir de zéro chaque fois que quelqu'un avait besoin de traverser un cours d'eau,
chaque pont ne serait pas très bon, car il ne bénéficierait pas des connaissances accumulées lors de la construction des ponts précédents.
Au lieu de cela, les ingénieurs disposent de plans pour différents types de ponts, les sélectionnent en fonction des spécificités du problème et proposent des améliorations lorsqu'ils en trouvent.

En génie logiciel, ces types de plans sont appelés _"design patterns"_, ou "patrons de conception" en pur français, et sont si courants qu'on en oublie parfois leur existence.
Prenons par exemple la boucle suivante :
```python
for item in items:
    # ...
```
Cette construction "for" semble tout à fait normale et standard, mais elle n'a pas toujours existé.
Par exemple, le langage Java ne l'a introduite que dans Java 1.5, en même temps que l'interface `Iterable<T>`, afin que chaque collection ne fournisse plus sa propre méthode d'itération.
Elle était autrefois connue sous le nom de "design pattern Iterator", mais elle est aujourd'hui tellement courante dans les langages de programmation modernes
que nous ne la considérons plus explicitement comme un patron de conception.

Les design patterns sont des plans, pas des algorithmes.
Une design pattern n'est pas un bout de code que vous pouvez copier-coller, mais une description générale de ce à quoi peut ressembler la solution à un problème courant.
Vous pouvez le considérer comme le nom d'un plat plutôt que sa recette.
Vous avez du poisson ? Vous pourriez préparer du poisson avec des légumes et du riz, ce qui est une combinaison saine. La sauce soja est également une bonne idée pour accompagner le plat.
La manière dont vous cuisinez le poisson ou les légumes que vous choisissez dépendent de vous.

Il existe de nombreuses patterns et encore plus de descriptions en ligne. Nous fournissons un [bref résumé](../../DesignPatterns.md) des plus courantes.

Dans ce cours, nous verrons des modèles permettant de séparer l'interface utilisateur d'un programme, la logique métier qui est au coeur du programme et les stratégies réutilisables dont le programme a besoin,
telles que le fait de réessayer lorsqu'une requête échoue.

Le problème résolu par les design patterns pour les interfaces utilisateur est courant : les ingénieurs logiciels doivent écrire du code pour des applications qui fonctionneront sur différents types de systèmes, tels que les applications de bureau et les applications mobiles.
Cependant, écrire le code une fois par plateforme ne serait pas viable : la plupart du code serait copié-collé.
Toute modification devrait être répliquée sur le code de toutes les plateformes, ce qui conduirait inévitablement à une désynchronisation d'une des copies.

Au lieu de cela, nous voulons pouvoir écrire une seule fois la logique centrale de l'application et n'écrire du code différent par plateforme que pour l'interface utilisateur.
Cela signifie également que les tests peuvent être écrits par rapport à la logique sans être liés à une interface utilisateur spécifique.
C'est une exigence pratique pour toute application de grande envergure.
Par exemple, Microsoft Office compte des dizaines de millions de lignes de code ; il serait tout à fait impossible de dupliquer ce code dans Office pour Windows, Mac, Android, le web, etc.

La logique métier est généralement appelée _"Model"_ ("modèle") et l'interface utilisateur _"View"_ ("vue").
Nous voulons éviter de les coupler, nous avons donc naturellement besoin d'un élément intermédiaire qui communique avec les deux, mais lequel ?

### Model-View-Controller (MVC)

Dans le modèle MVC, la vue et le modèle sont gérés par un _"Controller"_ ("contrôleur"), avec lequel les utilisateurs interagissent.
Un utilisateur soumet une requête au contrôleur, qui interagit avec le modèle et renvoie une vue à l'utilisateur :

<p align="center"><img alt="Schéma illustrant le modèle MVC" src="images/mvc.svg" width="50%" /></p>

Par exemple, dans un site web, le navigateur de l'utilisateur envoie une requête HTTP au contrôleur, qui finit par créer une vue à partir des données du modèle, et la vue est rendue en HTML.
La vue et le modèle sont découplés, ce qui est une bonne chose, mais il y a aussi des inconvénients.
Premièrement, les utilisateurs ne communiquent généralement pas directement avec les contrôleurs, en dehors du web.
Deuxièmement, créer une nouvelle vue à partir de zéro à chaque fois n'est pas très efficace.

### Model-View-Presenter (MVP)

Dans le modèle MVP, la vue et le modèle sont médiatisés par un _"Presenter"_ ("présentateur"), mais la vue gère directement les entrées de l'utilisateur.
Cela correspond à l'architecture de nombreuses interfaces utilisateur : les utilisateurs interagissent directement avec la vue, par exemple en touchant un bouton sur l'écran d'un smartphone.
La vue informe ensuite le présentateur de l'interaction, qui communique avec le modèle si nécessaire, puis indique à la vue ce qu'elle doit mettre à jour :

<p align="center"><img alt="Un diagramme illustrant le modèle MVP" src="images/mvp.svg" width="50%" /></p>

Cela résout deux des problèmes du modèle MVC : les utilisateurs n'ont pas besoin de connaître le module intermédiaire, ils peuvent interagir avec la vue à la place, et la vue peut être modifiée de manière incrémentale.

---
#### Exercice
Maintenant, à votre tour.
Ouvrez [le dossier d'exercices pendant le cours](exercices/cours) et créez un `Model` et une `View` pour séparer le code de l'application `weather.py`.
<details>
<summary>Exemple de solution (cliquer pour développer)</summary>
<p>

Le `FakeModel` reprend le code utilisant `random`, mais retourne juste la météo au lieu d'écrire la météo et le message "Météo actuelle" sur la console.

La `ConsoleView` utilise `print` et `input`, ainsi qu'une boucle infinie.

Consultez [la solution](exercices/solutions/cours/weather.py) pour voir les détails.

</p>
</details>
---

### Middleware

Vous avez écrit une application en utilisant une design pattern d'interface utilisateur pour séparer votre logique métier et votre interface utilisateur, mais vous recevez maintenant une demande d'un client :
les données peuvent-elles être mises en cache afin qu'une connexion Internet ne soit pas nécessaire ? De plus, lorsqu'il n'y a pas de données en cache, l'application peut-elle réessayer si elle ne parvient pas à se connecter immédiatement ?

Vous pourriez intégrer cette logique dans votre contrôleur, votre présentateur ou votre ViewModel, mais cela la lierait à une partie spécifique de votre application.
Vous pourriez l'intégrer dans un modèle, mais au prix de rendre ce module plus complexe, car il contiendrait plusieurs concepts orthogonaux.

C'est là qu'intervient le modèle _middleware_, également appelé _decorator_.
Un middleware fournit une couche qui expose la même interface que la couche inférieure, mais ajoute des fonctionnalités :

<p align="center"><img alt="Un diagramme illustrant un Middleware" src="images/middleware.svg" width="50%" /></p>

Un middleware peut "court-circuiter" une requête s'il souhaite répondre directement au lieu d'utiliser les couches inférieures.
Par exemple, si un cache contient des données récentes, il peut renvoyer ces données sans demander à la couche inférieure les données les plus récentes.

Un exemple concret de middleware est celui des [minifiltres du système de fichiers Windows](https://learn.microsoft.com/en-us/windows-hardware/drivers/ifs/filter-manager-concepts),
qui sont des middlewares pour le stockage qui effectuent des tâches telles que la détection de virus, la journalisation ou la réplication vers le cloud.
Cette conception permet aux programmes d'ajouter leur propre filtre dans la pile d'E/S Windows sans interférer avec les autres.
Les programmes tels que Google Drive n'ont pas besoin de connaître l'existence d'autres programmes tels que les antivirus.

---
#### Exercice
Reprennez votre `weather.py`, et ajoutez une fonctionnalité : si la météo est `"???"`, l'app doit réessayer.

Commencez par créer un nouveau `Model` qui prend un `Model` en paramètre de constructeur et délégue `getForecast`, puis écrivez une implémentation de `getForecast` qui réessaye si nécessaire.
<details>
<summary>Exemple de solution (cliquer pour développer)</summary>
<p>

Consultez [la solution](exercices/solutions/cours/weather-retry.py) pour voir les détails.

</p>
</details>
---

Le MVP présente certains inconvénients.
Tout d'abord, la vue contient désormais des variables, car elle est mise à jour de manière incrémentielle. Cela ajoute davantage de code à la vue, alors que l'un de nos objectifs initiaux était d'en réduire autant que possible.
Ensuite, l'interface entre la vue et le présentateur est souvent liée à des actions spécifiques que la vue peut effectuer dans un contexte donné, tel qu'une application console, et il est difficile de rendre la vue générique pour de nombreux formats.

### Model-View-ViewModel (MVVM)

Prenons un peu de recul avant de décrire le modèle suivant.
Qu'est-ce qu'une interface utilisateur, au juste ?
- Les données à afficher,
- les commandes à exécuter...

... et c'est tout ! Du moins, si on voit ça d'un très haut niveau.

L'idée clé derrière "MVVM" est que la vue doit _observer_ les changements de données à l'aide de la design pattern Observer.
Ainsi, le module intermédiaire, le "ViewModel", doit seulement être une interface utilisateur indépendante de la plateforme qui expose les données, les commandes
et une implémentation du modèle Observer pour permettre aux vues d'observer les changements.

Le résultat est un système clairement structuré, dans lequel la vue contient peu de code et est superposée au ViewModel, qui conserve l'état et utilise lui-même le modèle pour mettre à jour son état lorsque des commandes sont exécutées :

<p align="center"><img alt="Un diagramme illustrant le modèle MVVM" src="images/mvvm.svg" width="50%" /></p>

La vue observe les changements et se met à jour automatiquement. Elle peut choisir d'afficher les données comme elle le souhaite, car le ViewModel ne lui indique pas comment se mettre à jour, mais seulement ce qu'elle doit afficher.

La vue est conceptuellement une fonction du ViewModel : elle peut être entièrement calculée à partir de ce dernier à chaque fois, ou elle peut se modifier progressivement à des fins d'optimisation.
Cela est utile pour les plateformes telles que les smartphones, sur lesquelles les applications fonctionnant en arrière-plan doivent utiliser moins de mémoire :
la vue peut simplement être détruite, car elle peut être entièrement recréée à partir du ViewModel chaque fois que cela est nécessaire.
Le MVVM permet également la réutilisation du code que nous souhaitons obtenir, car différentes plateformes ont besoin de vues différentes, mais du même Model et du même ViewModel, et le ViewModel contient les variables, ce qui rend les vues plus petites.

Attention : ce n'est pas parce que vous pouvez utiliser toutes sortes de design patterns que vous devez le faire.
Si vous n'en avez pas besoin, ne le faites pas.
Sinon, vous risquez de vous retrouver avec une « implémentation d'AspectInstanceFactory qui localise l'aspect à partir de BeanFactory à l'aide d'un nom de bean configuré »,
au cas où quelqu'un souhaiterait bénéficier de cette flexibilité.
[Vraiment](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/aop/config/SimpleBeanFactoryAwareAspectInstanceFactory.html) !
