# Exercices pendant le cours

Créez un fichier avec vos tests, p.ex., `my_tests.py`, qui commencera par :

```python
import unittest

# idéalement avec un meilleur nom que "MyTests" :-)
class MyTests(unittest.TestCase):
    # Le nom des méthodes doit commencer par "test_"
    def test_example(self):
        self.assertEqual(2, 1 + 1)

    def test_example_raises(self):
        with self.assertRaises(ZeroDivisionError):
            y = 1 / 0
```

Enfin, lancez les tests :

    python3 -m unittest my_tests.py

Vous pouvez aussi lancer les tests depuis un IDE, souvent via un clic droit sur le fichier de tests ou sur une fonction de test.


Pour la couverture de code, installez Coverage :

    python3 -m pip install coverage

Puis utilisez-le en remplaçant `python3` par `coverage run` pour lancer les tests :

    coverage run -m unittest my_tests.py

Enfin, affichez les résultats (en filtrant pour ne voir que les fichiers dans ce dossier, pas dans la librairie standard Python) :

    coverage report --include=./*

Vous pouvez remplacer `report` par `html` pour générer un fichier HTML avec le code source annoté.

Pour la couverture de branches, ajoutez ` --branch` après `run`.

Là aussi un IDE vous permet normalement d'exécuter les tests avec couverture et de visualiser le résultat directement sur le code.
