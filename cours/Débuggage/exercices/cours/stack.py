# Exercice: Ajoutez du code à IntStack pour attrapper les bugs tôt et corrigez les bugs que vous trouvez.
#           Gardez à l'esprit que les utilisateurs d'IntStack doivent pouvoir tester les préconditions eux-mêmes.
#           Ajoutez des méthodes publiques ou privées si nécessaire.
#           Étape 1 : ajoutez la précondition nécessaire au constructeur. (Qu'est-il interdit/insensé ?)
#           Étape 2 : ajoutez une méthode 'def assert_invariants(self)' qui vérifie les invariants de la classe,
#                     et appelez-la (1) à la fin du constructeur, (2) au début de chaque méthode, et (3) à la fin de chaque méthode
#           Étape 3 : Corrigez les bugs !

class IntStack:
    """Une pile d'entiers, avec une taille maximale."""
    def __init__(self, max_size):
        """Crée une pile vide avec la taille maximale donnée ; il est interdit d'empiler plus d'éléments que cette taille."""
        self.top = -1
        self.values = [0] * max_size

    def pop(self):
        """Retourne et enlève de la pile l'élément sur le dessus de la pile, ou retourne None si la pile est vide."""
        value = self.values[self.top] if self.top >= 0 else None
        self.top -= 1
        return value

    def push(self, value):
        """Empile la valeur donnée."""
        self.values[self.top] = value
        self.top += 1

# exemple d'utilisation d'IntStack
def main():
    stack = IntStack(2)
    stack.push(1)
    assert stack.pop() == 1
    assert stack.pop() == None
    assert stack.pop() == None

main()
