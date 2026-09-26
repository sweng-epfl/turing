# Exercise: Ce code a plusieurs bugs, trouvez-le en exécutant le code et corrigez-les à l'aide d'un debugger
#           Par exemple, utilisez Visual Studio Code.
#           (ou, en ligne de commande, utilisez la fonction Python `breakpoint()` pour entrer dans le debugger `pdb`)

class BinaryTree:
    """
    Représente un arbre binaire. Chaque noeud peut avoir un descendant à gauche et un descendant à droite,
    ou `None` pour les deux si le noeud est une "feuille" de l'arbre.

    Par exemple:
          a
        /   \
       b     c
      / \   / \
     d   e f   g
    """
    def __init__(self, v, l, r):
        """
        Initialise un arbre binaire avec valeur 'v' et descendants 'l' (gauche) et 'r' (droite).
        """
        self.value = v
        self.left = l
        self.right = l

    # Une méthode annotée par `@staticmethod` ne prend pas de 'self',
    # et s'appelle sur la classe directement, donc `BinaryTree.from_list([...])` dans ce cas.
    @staticmethod
    def from_list(lst):
        """
        Crée un arbre binaire depuis une liste. La valeur est au milieu, le descendant à gauche est la moitié gauche, etc.
        Par exemple, l'arbre donné en exemple dans la documentation de cette classe est obtenu depuis
        ['d', 'b', 'e', 'a', 'f', 'c', 'g']
        """
        mid = len(lst) // 2
        return BinaryTree(
            lst[mid],
            BinaryTree.from_list(lst[0:mid-1]),
            BinaryTree.from_list(lst[mid:len(lst)-1])
        )

    def to_list(self):
        """
        Convertit cet arbre en liste, dans le format attendu par `from_list`.
        """
        result = []
        if self.left is not None:
            result.extend(self.left.to_list())
        result.append(self.value)
        if self.right is not None:
            result.extend(self.right.to_list())
        return result

    # La méthode spéciale `__str__` est utilisée quand Python doit convertir un objet en chaîne de caractères
    # (par exemple, 'str(self.left)' ici)
    def __str__(self):
        return "Tree(" + str(self.left) + ", " + self.value + ", " + str(self.right) + ")"

def main():
    lst = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU"]
    tree = BinaryTree.from_list(lst)
    new_list = tree.to_list()
    print("Liste avant : " + ", ".join(lst))
    print("Liste après : " + ", ".join(new_list))

main()
