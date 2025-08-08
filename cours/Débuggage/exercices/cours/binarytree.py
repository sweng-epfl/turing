# Exercise: Ce code a plusieurs bugs, trouvez-le en exécutant le code et corrigez-les à l'aide d'un debugger
#           Par exemple, utilisez la fonction python `breakpoint()` pour entrer dans le debugger `pdb`

from typing import List, Optional

class BinaryTree:
    def __init__(self, v: str, l: Optional['BinaryTree'], r: Optional['BinaryTree']):
        self.value = v
        self.left = l
        self.right = l

    @staticmethod
    def from_list(lst: List[str]) -> Optional['BinaryTree']:
        mid = len(lst) // 2
        return BinaryTree(
            lst[mid],
            BinaryTree.from_list(lst[0:mid-1]),
            BinaryTree.from_list(lst[mid:len(lst)-1])
        )

    def to_list(self) -> List[str]:
        result = []
        if self.left is not None:
            result.extend(self.left.to_list())
        result.append(self.value)
        if self.right is not None:
            result.extend(self.right.to_list())
        return result


def main():
    lst = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU"]
    tree = BinaryTree.from_list(lst)
    new_list = tree.to_list()
    print("Liste avant : " + ", ".join(lst))
    print("Liste après : " + ", ".join(new_list))


main()
