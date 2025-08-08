import random

class Quicksort:
    @staticmethod
    def sort(elements, comparator):
        Quicksort._sort(elements, comparator, 0, len(elements))

    @staticmethod
    def _sort(elements, comparator, frm, until):
        if frm > until:
            return
        pivot = Quicksort._partition(elements, comparator, frm, until)
        Quicksort._sort(elements, comparator, frm, pivot)
        Quicksort._sort(elements, comparator, pivot, until)

    @staticmethod
    def _partition(elements, comparator, frm, until):
        p = elements[frm]
        s = until
        for i in range(until - 1, frm, -1):
            if comparator(elements[i], p) > 0:
                s -= 1
                elements[i], elements[s] = elements[s], elements[i]
        elements[frm], elements[s] = elements[s], elements[frm]
        return s - 1

def sorting():
    # Prendre 100 nombres
    numbers = list(range(100))
    random.shuffle(numbers)

    # Les trier d'après leur ordre naturel
    def natural_order(x, y):
        return (x > y) - (x < y)
    Quicksort.sort(numbers, natural_order)

    # Imprimer le résultat
    print(numbers)

sorting()
