# Exercices pendant le cours

Créez un fichier avec vos tests, p.ex., `my_tests.py`, qui commencera par :

```python
import unittest

import fonctions # ou un autre fichier à tester, qui soit **dans le même dossier** que ce fichier de tests

# idéalement avec un meilleur nom que "MyTests" :-)
class MyTests(unittest.TestCase):
    # Le nom des méthodes doit commencer par "test_"
    def test_example(self):
        self.assertEqual(1, fonctions.fibonacci(1))

    def test_example_raises(self):
        with self.assertRaises(ZeroDivisionError):
            y = 1 / 0
```

Pour voir plus de méthodes de test, consultez [la documentation de `unittest`](https://docs.python.org/3/library/unittest.html).

Enfin, lancez les tests :

    python3 -m unittest my_tests.py

Vous pouvez aussi lancer les tests depuis un IDE, souvent via un clic droit sur le fichier de tests ou sur une fonction de test.


# Couverture de code (plus tard)

Pour la couverture de code, installez Coverage :

    python3 -m pip install coverage
    # Si cela affiche une erreur "error: externally-managed-environment",
    # soit installez via le gestionnaire de packages de votre OS,
    # soit "python3 -m pip install --break-system-packages coverage"

Puis utilisez-le en remplaçant `python3` par `coverage run` pour lancer les tests :

    python3 -m coverage run -m unittest my_tests.py

Enfin, affichez les résultats (en filtrant pour ne voir que les fichiers dans ce dossier, pas dans la librairie standard Python) :

    python3 -m coverage report --include=./*

Vous pouvez remplacer `report` par `html` pour générer un fichier HTML avec le code source annoté.

Pour la couverture de branches, ajoutez ` --branch` après `run`.

Là aussi un IDE vous permet normalement d'exécuter les tests avec couverture et de visualiser le résultat directement sur le code.
