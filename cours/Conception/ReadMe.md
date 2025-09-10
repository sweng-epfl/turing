# Conception

Imaginez que, pour afficher "Hello, World !" à l'écran, vous deviez apprendre comment tout fonctionne.
Vous devriez tout apprendre sur les voyants LED au niveau de la physique théorique.
Vous devriez ensuite lire des milliers de pages de fiches techniques sur les processeurs pour savoir quel code écrire en assembleur et comment communiquer avec des périphériques externes.

Au lieu de cela, vous pouvez écrire `print("Hello, World!")` dans un langage tel que Scala ou Python, et le tour est joué.
Le runtime du langage fait tout le travail à votre place, avec l'aide de votre système d'exploitation, qui contient lui-même des pilotes pour le matériel.
Même ces pilotes ne connaissent pas les voyants LED, car l'écran lui-même expose une interface pour afficher les données que les pilotes utilisent.
Python lui-même n'est pas non plus un monolithe : il contient des sous-modules tels qu'un tokenizer, un parseur et un interpréteur.

Malheureusement, il n'est pas facile d'écrire de grandes bases de code de manière claire, et c'est là que la conception entre en jeu.


## Objectifs

À l'issue de ce cours, vous devriez être capable de :
- Écrire du code orienté objet
- Choisir entre héritage et composition
- Appliquer la modularité et l'abstraction en pratique


## Comment encapsuler du code derrière une interface ?

Il ne s'agit ici pas d'interface utilisateur, mais bien d'interface machine : comment est-ce que des parties différentes de votre code peuvent se parler,
sans avoir besoin de connaître tous les détails ?

Avec des fonctions, vous pouvez faire des groupes, mais cela devient vite beaucoup :
```python
def animal_describe(kind): ...
def animal_draw(kind, canvas): ...
def animal_name(kind): ...
def str_replace(s, old, new): ...
def str_capitalize(s): ...
```
Ces fonctions pourraient se partager des variables globales. Par exemple, une méthode `animal_pet` pourrait augmenter une valeur stockée dans une table globale définissant à quel point chaque animal est content.
Cette table pourrait ensuite être lue par la fonction qui décrit un animal.

Mais il est facile de modifier une variable globale de manière non prévue par l'auteur des autres fonctions, ce qui rend le code complexe à modifier.
De plus, avec un éditeur de code, si vous écrivez `animal_` et que votre éditeur vous propose les 50 fonctions et variables commençant par ce nom,
comment sauriez-vous lesquels vous devez utiliser et lesquels sont des détails d'implémentation ?

À la place, on utilise des **objets** en déclarant une classe :
```python
class Animal:
  def describe(self): ...
  def draw(self, canvas): ...
  def name(self): ...
```
On voit déjà qu'au lieu d'avoir des fonctions potentiellement éparses parmi le code source, elles sont toutes au même endroit,
avec `self` indiquant l'"instance" de la classe sur laquelle elles opérent.

De plus, vous pouvez associer des champs à chaque instance afin de conserver un état lié à une instance,
qui est typiquement initialisé dans un _constructeur_:
```python
class Animal:
  def __init__(self, kind):
    self.kind = kind
```
La méthode spéciale `__init__` est celle appelée lorsque vous créez une instance de la classe en utilisant son nom, et ici elle définit le champ `kind` de l'instance :
```python
a = Animal("Chat")
print(a.kind) # Chat
```

Une partie de l'état d'une classe est souvent _privé_, c'est-à-dire que seule la classe peut l'utiliser, ce qui est la base de l'encapsulation.
Par exemple, pour garder une trace de si un animal est content, vous pouvez initialiser un champ privé dans le constructeur :
```python
class Animal:
  def __init__(self, kind):
    self.kind = kind
    self._happy = True
```
Ce champ `_happy` peut ensuite être modifié dans des méthodes telles que "donner à manger à l'animal", "caresser l'animal", "emmener l'animal chez le vétérinaire"...

Comme il commence par un souligné `_`, la convention en Python est que personne ne doit l'utiliser hors de la classe.
Vous pouvez l'utiliser quand même si vous le voulez, mais c'est une mauvaise idée, et la présence d'un souligné `_` vous indique immédiatement que vous faites quelque chose de bizarre.

De même, vous pouvez déclarer des méthodes privées :
```python
class Animal:
  def _increase_happiness(self):
    ...
```

Dans d'autres langages de programmation, comme Java ou C#, le compilateur peut garantir que certains champs sont privés :
```csharp
class Animal {
  private string _happy = true;
}

(new Animal())._happy // erreur, impossible de compiler ce code !
```

Nous avons vu comment déclarer une méthode pour un type de données, mais parfois vous avez besoin de plusieurs fonctions selon le type exact :
```python
def cat_describe(): ...
def dog_describe(): ...
def giraffe_describe(): ...
```
Ceci se fait en programmation orientée objet grâce à l'**héritage** :
```python
class Animal: ...

class Cat(Animal): ...

class Dog(Animal): ...
```
On dit ici qu'un `Cat` _est un_ `Animal`. La "sous-classe" `Cat` hérite des méthodes de la "super-classe" `Animal` et peut redéfinir certaines méthodes :
```python
class Animal:
  def describe(self): return "Un animal"
  def happy(self): return self._happy

class Cat(Animal):
  def describe(self): return "Un chat"
```

Les appels de méthodes sont _dynamiques_, c'est-à-dire qu'ils dépendent du type exact de l'instance sur laquelle ils sont appelés :
```python
def example(a: Animal):
  print(a.describe())

example(Cat()) # "Un chat"
```
Dans cet exemple, même si nous avons donné le type `Animal` au paramètre `a`, puisque nous passons un `Cat`, c'est la méthode `Cat.describe` qui est appelée.

Si besoin, vous pouvez appeler la méthode de la super-classe spécifiquement avec la syntaxe `super().`:
```python
class Dog(Animal):
  def describe(self):
    return "Un chien est " + super().describe()

example(Dog()) # "Un chien est Un animal"
```

Notez qu'en Python, contrairement aux des langages statiquement typés, il n'y a pas besoin d'avoir une super-classe commune pour utiliser deux classes de la même manière.
Si un objet marche comme un canard et fait coin-coin comme un canard, c'est un canard, ce qui donne le nom "duck typing" en anglais.
Par exemple :
```python
class Duck:
  def quack(self): print("Quack")

class Sheep:
  def quack(self): print("Baaa???")
```
Un `Duck` peut `quack`, mais un `Sheep` a apparemment aussi appris à `quack`, donc toute méthode s'attendant à un `Duck` peut aussi utiliser un `Sheep`.
Ce qui ne veut pas forcément dire que c'est une bonne idée !

#### Exercice, partie 1
Ouvrez le fichier [`interactions.py`](./cours/exercices/interactions.py).

Comme indiqué en commentaire, déplacez le code interagissant avec l’utilisateur dans une nouvelle `class UI`.

<details>
<summary>Solution (cliquez pour développer)</summary>
<p>

Par exemple :

```python
class UI:
    def show(self, text):
        print(text)

    def input(self, prompt):
        result = None
        while not result:
            print(prompt)
            result = input()
        return result
```

Le reste du code devient maintenant beaucoup plus clair :
```python
ui = UI()
ui.show('Bonjour !')
name = ui.input('Quel est votre nom ?')
ui.show('Bienvenue, ' + name + '!')
hobby = ui.input('Quel est votre passe-temps préféré ?')
ui.show(hobby + ', quelle bonne idée !')
```

</p>
</details>

#### Exercice, partie 2
Gardez votre solution de la partie 1, et ouvrez le fichier [`interactions-tkinter.py`](./cours/exercices/interactions-tkinter.py).

Les fonctions dans ce fichier permettent d'afficher du texte et de demander du texte à l'utilisateur à l'aide de `tkinter`, sorte de boîte à outils graphique pour des interfaces utilisateur basiques en Python.

Écrivez une classe `GraphicalUI` avec la même interface que `UI`, donc les mêmes noms de méthodes, pour que vous puissiez réutiliser la logique de la partie 1 tout en changeant la manière dont le code interagit avec l'utilisateur.

---

Enfin, avant de passer à la suite, une astuce Python : si vous avez besoin d'une classe juste pour grouper des valeurs, comme par exemple un nom et un age appartenant à une personne,
vous pouvez utiliser `dataclass` pour ne pas avoir à écrire le constructeur `__init__` à la main :
```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p = Person("Alice", 7)
print(p.name)
```
Nous ne parlerons pas plus de `dataclass`, mais c'est bon à savoir.


## Comment utiliser les objets en pratique ?

Nous venons de voir comment écrire des classes et utiliser l'héritage et les attributs en Python, mais qu'en est-il de la pratique ? Comment choisir ce qui doit être public ou privé, ce qui doit hériter d'une autre classe... ?

Déjà, concernant la distinction public/privé, préférez les méthodes privées et attributs privés par défaut.
Il est facile de changer dans la direction "privé => public", car personne d'autre ne peut utiliser les choses privées, donc donner au reste du code la possibilité d'utiliser quelque chose qui était auparavant privé ne pose pas de problème.
Mais l'inverse n'est pas vrai : changer dans la direction "public => privé" peut causer beaucoup de problèmes, car tout le code qui utilisait ce qui était avant public et est maintenant privé ne fonctionne plus.
Si vous vous rendez compte qu'une méthode n'aurait pas du être publique car elle permet de casser l'encapsulation fournie par sa classe, par exemple, vous devez changer tout le code hors de la classe qui l'utilise.
Dans le cas où votre code est utilisé par d'autres, par exemple si vous avez publié votre code sur un dépôt de paquets afin que d'autres puissent l'utiliser, les utilisateurs ne seront pas content que leur code ne marche plus avec votre nouvelle version qui rend une méthode privée alors qu'elle était publique.

Notons aussi que le fait qu'une classe a des méthodes publiques et privées ne signifie pas qu'on peut toujours la remplacer par une implémentation différente qui fournisse "la même chose", à cause des performances.
Par exemple, une carte de la Terre implémentée avec la [projection de Mercator](https://fr.wikipedia.org/wiki/Projection_de_Mercator) peut très facilement fournir l'opération "quel angle dois-je utiliser pour naviguer entre deux points",
car conserver les angles est justement le but de cette projection.
Vous pourriez changer l'implémentation de la carte pour utiliser une autre projection, mais si calculer un angle est beaucoup plus lent avec votre projection différente, l'implémentation ne sera pas forcément utilisable en pratique avec le niveau de performance attendu.

#### Exercice
Vous implémentez un réseau social et avez besoin de stocker des images.
Pour l'instant, vous stockez ces images sur le disque local de votre machine.

Lesquelles de ces méthodes devraient être préfixées d'un `_` pour indiquer qu'elles sont privées ?
```python
class PictureStorageOnDisk:
  def get_picture(self, id): ...
  def get_file_name(self, id): ...
  def get_all_pictures(self): ...
```

<details>
<summary>Solution (cliquez pour développer)</summary>
<p>

`get_picture` est le but principal de la classe donc doit rester public.

`get_file_name` est un détail d'implémentation. Si vous stockiez les fichiers dans une base de données, ou sur un site externe, le concept même de "nom de fichier" n'aurait pas de sens, cette méthode doit donc être privée.

`get_all_pictures` est discutable. Cela est potentiellement utile pour le reste de l'application, mais selon la manière dont les images sont stockées, cette opération pourrait être extrêmement inefficace, par exemple en téléchargeant des milliers d'images.
Il vaut mieux la laisser en privé jusqu'à ce qu'il y ait un vrai besoin.

</p>
</details>

---

Il est facile de céder à la tentation du "juste au cas où..." et de rendre ses interfaces extrêmement générales.
Le stockage d'images de l'exercice que vous venez de faire pourrait être un stockage de "données" prenant non seulement leur identifiant mais aussi leur type, un Booléen indiquant si un cache local doit être utilisé, et bien d'autres paramètres.
En interne, c'est peut-être comme cela que ce stockage sera implémenté. Mais il vaut mieux garder une interface publique spécifique, qui facilite l'utilisation de la classe.

Un autre choix que vous devez faire en écrivant des classes concerne l'héritage.
Un chat "est un" animal, un participant à un évènement "est une" personne, un sponsor de cet évènement "est une" société.
Par contre, un chat "a une" tête, un participant "a une" adresse email, un sponsor "a un" compte bancaire.

Il est donc normal d'écrire `class Chat(Animal)`, mais pas `class Chat(Tête)`. Ce n'est pas parce qu'on peut utiliser la tête d'un chat pour le caresser qu'un chat est plus généralement une tête.
L'exemple du sponsor est flagrant : oui, un sponsor vous fournit de l'argent pour votre évènement, mais vous ne pouvez pas créer un compte chez votre sponsor pour y verser ou y retirer de l'argent à votre guise !

Gardez à l'esprit le [principe de substitution de Liskov](https://fr.wikipedia.org/wiki/Principe_de_substitution_de_Liskov), nommé d'après [Barbara Liskov](https://fr.wikipedia.org/wiki/Barbara_Liskov),
informaticienne et pionnière de l'abstraction et de l'encapsulation dans les langages de programmation.
Si `X` est un `Y`, alors partout où l'on peut utiliser un `Y`, on peut également utiliser un `X`.
On peut donc utiliser un `Chat` partout où l'on peut utiliser un `Animal` en général. Mais on ne peut pas utiliser un `Participant` partout où l'on peut utiliser une `AdresseEmail`. Les participants ne veulent peut-être même pas que vous connaissiez leur adresse !

Un exemple connu est celui de la classe `Stack` en Java, qui est censé représenter une "pile" où l'on peut déposer des objets en mode "premier arrivé, dernier sorti". Si vous déposez `1, 2, 3`, vous retirez `3, 2, 1` dans l'ordre.
En interne, cette classe pourrait utiliser une représentation similaire à celle d'une "liste" comme la `list` en Python.
Mais comme Java est un des premiers langages orientés objet à être devenu populaire, sa librairie standard contient des erreurs de débutant.
Dans ce cas-ci, `Stack` _hérite_ de la classe pour les listes au lieu d'en _contenir_  une. Donc n'importe qui peut ajouter ou supprimer des objets à n'importe quel index de la pile, ce qui détruit l'encapsulation.

Enfin, gardez à l'esprit que les "types de données" en théorie ne correspondent pas forcément aux types que vous pouvez utiliser en pratique.
Par exemple, un `âge` peut être un `int` en Python, mais cela ne veut pas pour autant dire que `-500` est un âge !
Quand vous réfléchissez au types de vos données, souvenez-vous que vous pouvez être plus précis dans la documentation et avec du code qui vérifie les valeurs que les types généraux que vous avez à disposition.
Certains langages vous permettent d'ailleurs d'être plus précis que Python et de définir vous-même des types comme "les entiers de 0 à 9 inclus".

Les types de données sont parfois définis en fonction d'autres types. "Une liste", implicitement, c'est une liste de quelque chose, par exemple une `list[int]`, une `list[str]`, ou même une `list[list[int]]`.
Cela mène à une intersection intéressante avec l'héritage.
Sachant qu'un `Chat` est un `Animal`, est-ce qu'une `Image[Chat]` est une `Image[Animal]` ? Oui, clairement.
Est-ce que de la `NourriturePour[Chat]` est plus généralement de la `NourriturePour[Animal]` ? Non ! Tous les animaux ne peuvent pas manger tout ce que les chats peuvent manger.
Par contre, si vous avez de la `NourriturePour[Animal]` en général, c'est de la `NourriturePour[Chat]` puisque si quelque chose convient à tous les animaux, cela convient clairement aux chats.

Et nos listes ? Est-ce qu'une `list[Chat]` est une `list[Animal]` ?
Si c'était le cas, on pourrait écrire du code comme cela :
```python
def add_tiger(lst: list[Animal]): ...

lst = [giraffe1, giraffe2]
add_tiger(lst) # oups, on ajoute un tigre dans une liste de girafes, pauvres girafes
```
Est-ce donc l'inverse ? Une `list[Animal]` est-elle une `list[Chat]` ? Non plus, si on retire un élément de la liste, c'est un `Animal` mais pas forcément un `Chat`. Il n'y a donc aucune relation d'héritage entre `list[Chat]` et `list[Animal]`.

Formellement, on parle de "variance" :
- La **covariance**, c'est l'usage en sortie : une image de chat est une image d'animal
- La **contravariance**, c'est l'usage en entrée : la nourriture pour animal est de la nourriture pour chat
- L'**invariance**, c'est ni l'un ni l'autre : une liste de chats et une liste d'animaux ne peuvent pas être utilisées l'une pour l'autre
