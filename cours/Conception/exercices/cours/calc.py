#!/usr/bin/env python3

# Exercice : Ce code n'est pas très modulaire et mélange plein de concepts, ce qui le rend difficile à comprendre et à maintenir.
#            Modularisez-le, sans changer ce que l'utilisateur voit/fait.
#            Par exemple, commençez par écrire le code de haut niveau "idéal", puis implémentez chaque fonction nécessaire.
# ("Notation polonaise inverse" = "les opérateurs à la fin", p.ex. "2 1 +" pour 2+1, "2 3 4 * +" pour 2+(3*4) --> jamais besoin de parenthèses, mais plus difficile à lire)

while True:
    text = input("Calcul à faire ? (en notation polonaise inverse; ou 'sortir') ")
    if text == "sortir": break
    parts = text.split(" ")
    lst = []
    for p in parts:
        if p == '':
            continue
        elif p == '+':
            lst.append(lst.pop() + lst.pop())
        elif p == '-':
            r = lst.pop()
            l = lst.pop()
            lst.append(l - r)
        elif p == '*':
            lst.append(lst.pop() * lst.pop())
        elif p == '/':
            r = lst.pop()
            l = lst.pop()
            lst.append(l / r)
        else:
            try:
                n = int(p)
                lst.append(n)
            except ValueError:
                print("Erreur, je ne sais pas quoi faire avec : " + p)
                continue

    if len(lst) == 1:
        print(lst.pop())
    else:
        print("Calcul invalide")
