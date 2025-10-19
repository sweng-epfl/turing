#!/usr/bin/env python3

import json
import urllib.request

url = "https://api.open-meteo.com/v1/forecast?latitude=46.516&longitude=6.6328&current=precipitation"

with urllib.request.urlopen(url) as response:
    result = response.read().decode("utf-8")
    # Partie 1 : Affichez la précipitation actuelle.
    #            Vous pouvez transformer `result` en un objet via la fonction `json.loads`.
    print("Précipitation : ")
    # Partie 2 : Affichez en plus la température à 2 mètres du sol.
    #            Pour cela, il vous faut modifier la requête selon la documentation : https://open-meteo.com/en/docs#api_documentation
