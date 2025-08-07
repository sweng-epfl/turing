# Exercice : adaptez cette classe aux changements de Joker

from joker import Joker

# Méthode principale séparée afin de pouvoir la tester
def main():
    print("Bonjour ! Combien de blagues voulez-vous ?")
    count = int(input())
    Joker().get_jokes(count)
    print("J'espère que c'était drôle !")

if __name__ == "__main__":
    main()

# Exercice optionnel si vous avez le temps / l'envie : Testez la méthode main(), c.f. app_test.py
