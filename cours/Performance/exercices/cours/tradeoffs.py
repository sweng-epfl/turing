# Cette app présente l'actualité (fictive).
# L'utilisateur peut lire les titres des articles depuis n'importe quel index parmi une liste.
# L'app affiche un batch de titres depuis l'index choisi par l'utilisateur.
# Cependant, chaque titre prend un petit moment à être chargé.

# Exercice 1: Actuellement, l'app obtient un batch entier à la fois, puis affiche tout.
#             Mais cela veut dire attendre le chargement du dernier objet avant que l'utilisateur ne voir une réaction.
#             Changez `getNews` pour utiliser du streaming.
# Indice : au lieu de `return ...`, utilisez `yield` pour chaque objet

# Exercice 2: Actuellement, si l'utilisateur demande les mêmes titres plusieurs fois, ils sont re-"téléchargés".
#             Changez `getNews` pour ajouter un cache pour chaque titre individuel.
#             Pour cet exercice, ne prêtez pas attention à la taille ou l'expiration du cache.

# Exercice 3: Actuellement, si l'utilsateur se comporte de manière "attendue" et lit les articles en commençant à 0,
#             chaque batch doit attendre que l'utilisateur le demande.
#             Ajoutez du prefetching pour qu'une fois qu'un batch est affiché, le prochain commence à être chargà.
# Indice : `threading.Thread(target=nom_de_la_fonction, args=[arguments]).start()` pour lancer une tâche en arrière-plan

import time
import threading
import sys

BATCH_SIZE = 5

# Ne modifiez pas cette méthode.
def getInputIndex():
    while True:
        print("Index à partir duquel obtenir les articles (0-100), ou 'quitter': ")
        text = input()
        if text == "quitter":
            sys.exit(0)
        try:
            result = int(text)
            if 0 <= result <= 100:
                return result
        except:
            pass # redemander un input

# Ne modifiez pas cette méthode.
def getNewsItem(index: int):
    # Faisons semblant de faire une opération longue, p.ex., téléchargement
    # Dans une vraie app, on ferait par exemple une requête HTTP
    time.sleep(1)

    # généré avec ChatGPT (un peu moins marrant que les équivalents en anglais...)
    NEWS_TITLES = [
        "Il découvre qu’il est allergique au travail après seulement deux jours d’essai",
        "Un homme termine enfin un tube de colle sans se coller les doigts",
        "Cette femme affirme communiquer avec ses plantes, mais elles ne répondent plus depuis qu’elle a oublié l’arrosage",
        "Il tente de battre le record du monde de procrastination mais oublie de s’inscrire",
        "Un chat découvre par hasard qu’il est en fait un chien adopté par erreur",
        "Elle pense que le Wi-Fi a un goût, son entourage s’inquiète",
        "Ce couple simule encore la passion après 12 ans de mariage pour ne pas vexer les voisins",
        "Netflix lance une série sur un mec qui ne regarde plus Netflix",
        "Un ado croit qu’un téléphone fixe est une antiquité à manivelle",
        "L’homme qui prononçait 'quinoa' correctement dès la première fois enfin retrouvé",
        "Ce boulanger affirme que son pain est 'artisanal' car il porte un tablier vintage",
        "Il rate un entretien d’embauche en tentant de draguer la plante verte",
        "Un pigeon menace de porter plainte pour atteinte à la vie privée après avoir été pris en photo sans consentement",
        "Un influenceur teste la vie sans Internet, il tient 37 secondes",
        "La science confirme : 87% des objets perdus réapparaissent dès que vous n’en avez plus besoin",
        "Cette femme continue d’envoyer des 'Coucou ça va ?' à son ex par pur professionnalisme",
        "Un enfant de 4 ans prouve qu’il sait mieux utiliser une télécommande que ses parents",
        "Il se perd dans IKEA et fonde une nouvelle civilisation dans le rayon des canapés",
        "Une application pour traduire les miaulements de chats déclenche une guerre civile entre félins",
        "Il pensait avoir trouvé un raccourci, il arrive finalement 3 jours en avance dans une autre dimension"
    ]

    return NEWS_TITLES[index % len(NEWS_TITLES)]


def getNews(index: int, count: int):
    result = []
    for n in range(count):
        # Dans une vraie app, on pourrait faire une requête plus efficace, p.ex., demander au serveur plusieurs articles en une seule requête
        result.append(getNewsItem(index + n))
    return result


while True:
    index = getInputIndex()
    for news in getNews(index, BATCH_SIZE):
        print(news)
