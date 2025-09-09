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
