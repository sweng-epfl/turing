# Exercice: Ajoutez du code à IntStack pour attrapper les bugs tôt et corrigez les bugs que vous trouvez.
#           Gardez à l'esprit que les utilisateurs d'IntStack doivent pouvoir tester les préconditions eux-mêmes.
#           Ajoutez des méthodes publiques ou privées si nécessaire.

from typing import Optional

class IntStack:
    """Une pile d'entiers, avec une taille maximale."""
    def __init__(self, max_size: int):
        """Crée une pile vide avec la taille maximale donnée ; il est interdit d'empiler plus d'éléments que cette taille."""
        self.top = -1
        self.values = [0] * max_size

    def pop(self) -> Optional[int]:
        """Retourne et enlève de la pile l'élément sur le dessus de la pile, ou retourne null si la pile est vide."""
        value = self.values[self.top] if self.top >= 0 else None
        self.top -= 1
        return value

    def push(self, value: int):
        """Empile la valeur donnée."""
        self.values[self.top] = value
        self.top += 1

# exemple d'utilisation d'IntStack
def use_stack(stack: IntStack):
    stack.push(1)
    stack.pop()
    stack.pop()

use_stack(IntStack(4))
