# Performance

Produire des résultats corrects n'est pas le seul objectif d'un logiciel.
Les résultats doivent être produits dans un délai raisonnable, sinon les utilisateurs risquent de ne pas attendre la réponse et d'abandonner.
Accélérer les logiciels peut considérablement améliorer l'expérience utilisateur, par exemple en [produisant des jeux vidéo plus jolis](https://www.youtube.com/watch?v=Drame-4ufso).
La vitesse peut également avoir des conséquences plus directes, comme l'a découvert Google lorsqu'il a constaté qu'un délai supplémentaire de 0,5 seconde pour afficher les résultats de recherche
entraînait une perte de 20 % des revenus publicitaires (http://glinden.blogspot.com/2006/11/marissa-mayer-at-web-20.html).


## Objectifs

À l'issue de cette leçon, vous devriez être capable de :
- Définir des objectifs de performance
- Créer des benchmarks pour mesurer la performance
- Concevoir et implémenter des systèmes rapides
- Connaître des compromis de performance courants


## Comment définir les objectifs de performance ?

De nombreux facteurs doivent être pris en compte lors de la définition des objectifs.
Quelle unité utiliser ? Quelle mesure ? Quel degré de variabilité est acceptable ? Quel doit être le degré de formalité de l'objectif ? Examinons chacun de ces points tour à tour.

Selon l'opération que vous mesurez, l'unité de mesure peut varier considérablement.
La restauration des données à partir de [bandes magnétiques](https://en.wikipedia.org/wiki/Magnetic-tape_data_storage) utilisées pour le stockage à long terme peut prendre des heures si un camion doit se rendre au lieu de stockage, récupérer les bandes, les apporter au centre de données et les copier.
Dans ce cas, le fait que l'opération prenne 3 ou 10 heures a probablement de l'importance, mais le fait qu'elle dure 3 heures et 10 minutes ou 3 heures et 12 minutes n'a probablement pas d'importance.
La sauvegarde d'une base de données d'un serveur à un autre peut prendre quelques minutes.
Là encore, le fait que cela prenne 4 ou 15 minutes a de l'importance, mais le fait que cela prenne 4 minutes et 3 secondes ou 4 minutes et 10 secondes n'a probablement pas d'importance.
Nous pouvons descendre à des unités de plus en plus petites.
Le téléchargement d'un fichier volumineux vers un serveur se mesure en secondes.
Le chargement d'une page Web se mesure en millisecondes.
La requête effectuée d'un serveur à un autre au sein d'un centre de données pour servir cette page Web prend quelques microsecondes.
Les calculs sur un seul serveur prennent des nanosecondes, car les processeurs modernes effectuent des milliards d'opérations par seconde.

Si vous ne savez pas exactement combien de temps dure une nanoseconde, consultez [l'exemple intéressant de Grace Hopper](https://www.youtube.com/watch?v=gYqF6-h9Cvg) (la vidéo comporte des sous-titres en français transcrits manuellement).
Grace Hopper était une pionnière dans le domaine des langages de programmation. Avec son équipe, elle a conçu COBOL, le premier langage de programmation utilisant des commandes similaires à celles de la langue anglaise.
Comme elle [le rappelait](https://www.amazon.com/Grace-Hopper-Admiral-Computer-Contemporary/dp/089490194X) :
"J'avais un compilateur qui fonctionnait, mais personne ne voulait s'en servir. On me disait que les ordinateurs ne pouvaient faire que des calculs arithmétiques".
Heureusement, elle a ignoré les détracteurs, sinon nous ne programmerions pas dans des langages de haut niveau aujourd'hui !

Une fois que nous avons défini une unité de temps, il existe deux indicateurs clés pour mesurer les performances.
Le débit est le nombre de requêtes traitées par unité de temps, et la latence est le temps nécessaire pour traiter une requête.
Dans un système qui traite une requête à la fois, le débit est l'inverse de la latence moyenne.
Dans un système qui traite plusieurs requêtes à la fois, cette corrélation n'existe pas.
Par exemple, un coeur d'un processeur double coeur peut traiter une requête en 10 secondes tandis qu'un autre coeur a traité 3 requêtes pendant ce temps. Le débit est donc de 4 requêtes par 10 secondes, mais la latence varie selon les requêtes.
Nous ne voulons souvent prendre en compte que les requêtes réussies, car il est rarement utile de traiter rapidement une réponse d'erreur.
Le débit des requêtes réussies est appelé "goodput", combinaison de "good" (bon) et "throughput" (débit).

Il existe bien sûr d'autres mesures de performance que le temps.
La quantité de mémoire utilisée par un programme peut avoir son importance, tout comme l'espace de stockage. Par exemple, un programme qui s'exécute rapidement mais qui nécessite plus de RAM que votre ordinateur n'en dispose ne vous est d'aucune utilité,
et vous feriez mieux d'utiliser un programme plus lent qui peut réellement fonctionner sur votre machine.
L'efficacité énergétique est également un indicateur important, qui peut se traduire par l'autonomie de la batterie des appareils mobiles tels que les smartphones.
Les utilisateurs ne sont pas susceptibles de vouloir un programme légèrement plus rapide qui épuise la batterie de leur téléphone.

En théorie, nous aimerions que les performances soient les mêmes pour toutes les demandes et tous les utilisateurs, mais dans la pratique, c'est rarement le cas.
Certaines requêtes nécessitent fondamentalement plus de travail que d'autres, comme commander une pizza avec 10 garnitures par rapport à une pizza avec seulement du fromage et des tomates.
Certaines requêtes passent par des chemins de code différents parce que les ingénieurs ont fait des compromis, comme commander une pizza sans gluten qui prend plus de temps
car au lieu de disposer d'une cuisine séparée sans gluten, le restaurant doit nettoyer sa seule cuisine.
Certaines requêtes sont en concurrence avec d'autres pour obtenir des ressources, comme commander une pizza juste après qu'une grande table ait passé une commande dans un restaurant qui ne dispose que d'un seul four à pizza.

Il existe de nombreux sous-indicateurs couramment utilisés pour traiter les statistiques : moyenne, médiane, 99e centile, et même les performances pour la première demande uniquement, c'est-à-dire en incluant le temps nécessaire au démarrage du système.
Le choix de la mesure à cibler dépend de votre cas d'utilisation et doit être défini en collaboration avec les clients.
Les percentiles élevés, tels que le 99e percentile, sont pertinents pour les grands systèmes dans lesquels de nombreux composants sont impliqués dans chaque requête, comme [le décrit Google](https://research.google/pubs/pub40801/) dans son article "Tail at Scale".
Certains systèmes s'intéressent en fait au "100e centile", c'est-à-dire au pire temps d'exécution possible, car les performances peuvent être un objectif de sécurité.
Par exemple, lorsqu'un pilote d'avion donne un ordre, l'avion doit réagir rapidement.
Il serait catastrophique que l'avion exécute la commande plusieurs minutes après que le pilote l'ait donnée, même si l'exécution est sémantiquement correcte.
Pour de tels systèmes, le temps d'exécution dans le pire des cas est généralement surestimé par une analyse manuelle ou automatisée.
Certains systèmes ne tolèrent aucune variabilité, c'est-à-dire qu'ils exigent une exécution en temps constant. C'est généralement le cas des opérations cryptographiques, dont le timing ne doit révéler aucune information sur les clés secrètes ou les mots de passe.

Même si les utilisateurs peuvent vous donner leur perception subjective de ce qui est "rapide" et de ce qui est "lent", les clients ont besoin de définitions formelles à inscrire dans un contrat.
Les performances sont généralement définies en termes d'indicateurs de niveau de service ou "SLI" ("Service Level Indicator"), qui sont des mesures telles que la "latence médiane des requêtes",
les objectifs de niveau de service ou "SLO" ("Service Level Objective"), qui définissent des buts pour ces mesures, tels que "moins de 50 ms",
et les accords de niveau de service ou "SLA" ("Service Level Agreement"), qui ajoutent des conséquences aux objectifs, telles que "ou nous remboursons 20 % des dépenses du client pour le mois".
Par exemple, la chaîne de pizzerias Domino's a mené une campagne marketing affirmant que votre pizza serait gratuite si elle n'arrivait pas dans les 30 minutes suivant votre commande.
Le délai de réception de la pizza est le SLI, 30 minutes est le SLO, et l'offre d'une pizza gratuite est le SLA.
Ce SLA spécifique s'est avéré être une [mauvaise idée](https://www.nytimes.com/1993/12/22/business/domino-s-ends-fast-pizza-pledge-after-big-award-to-crash-victim.html), car il a entraîné une augmentation des accidents de voiture pour leurs chauffeurs.
Les SLA peuvent même être codifiés dans la loi, comme l'ordonnance suisse sur la Poste (https://www.fedlex.admin.ch/eli/cc/2012/586/fr#art_32) qui fixe des délais spécifiques pour les lettres et les colis, les pourcentages de livraisons qui doivent respecter ces délais
et des instructions à la Poste suisse pour mandater un observateur externe pour ces mesures.


## Comment mesurer la performance ?

Le processus de mesure des performances est appelé "benchmarking" et consiste en une forme de test des performances.
Comme les tests, les benchmarks sont généralement automatisés et posent des problèmes tels que la manière d'isoler un composant spécifique plutôt que de toujours évaluer l'ensemble du système.
Les benchmarks pour des fonctions individuelles sont généralement appelés "microbenchmarks", tandis que les benchmarks pour des systèmes entiers sont des benchmarks "de bout en bout".

En théorie, le benchmarking est un processus simple : démarrer un chronomètre, effectuer une action, arrêter le chronomètre.
Mais dans la pratique, il existe de nombreux aspects délicats. Quelle est la précision du chronomètre ? Quelle est la résolution du chronomètre ? Dans quelle mesure l'opération est-elle variable ? Combien de mesures faut-il prendre pour que les résultats soient valables ?
Faut-il écarter les valeurs aberrantes ? Quelle est la meilleure API sur chaque système d'exploitation pour chronométrer les actions ? Comment éviter les effets de démarrage ? Et les effets de mise en cache ? Les optimisations du compilateur invalident-elles le benchmark en modifiant le code ?

Vous ne devriez jamais écrire votre propre code de benchmarking. À moins que vous ne deveniez un jour un expert en benchmarking, auquel cas vous saurez que vous pouvez enfreindre cette règle.
Utilisez plutôt un framework de benchmarking existant, tel que JMH pour Java, BenchmarkDotNet pour .NET ou pytest-benchmark pour Python.

Le processus général de benchmarking est le suivant :
1. Choisissez le code que vous souhaitez benchmarker
2. Choisissez la _référence_ par rapport à laquelle vous souhaitez effectuer le benchmark, qui peut être un autre morceau de code ou un niveau de performance absolu
3. Choisissez les entrées pour votre benchmark, en fonction des entrées réalistes ou courantes pour votre logiciel
4. Écrivez et exécutez votre benchmark

Même lorsque vous utilisez un cadre de benchmarking, vous devez garder à l'esprit certains faits importants.
Tout d'abord, les optimisations ne sont pas toujours vos alliées.
Prenons l'exemple de la fonction Python suivante :
```python
lst = ...
def append():
    lst + [0]
```
Si vous évaluez la performance de `append`, vous risquez de ne rien évaluer du tout, car Python pourrait remarquer que le résultat de `+` n'est pas utilisé et, comme il n'a aucun effet secondaire, ne pas l'exécuter du tout,
comme si vous aviez écrit `def append(): pass`.
Il est possible de contourner ce problème, par exemple en renvoyant le résultat de `+`.
Mais même si vous faites cela, aviez-vous l'intention de ne comparer que `+` ? Car cette méthode crée également une liste à un élément, et le temps de cette opération sera inclus dans le résultat.
Vous préférerez donc peut-être écrire ceci à la place :
```python
lst = ...
lst2 = ...
def append():
    return lst + lst2
```

Il est facile d'écrire accidentellement un code de benchmark qui n'a aucun sens à cause d'un problème subtil.
Demandez toujours à quelqu'un de vérifier votre code de benchmark et fournissez le code chaque fois que vous communiquez les résultats.
Essayez de petites variations du code pour voir si vous obtenez de petites variations dans les résultats du benchmark.
Reproduisez les résultats précédents, si vous en avez, pour vous assurer que votre configuration globale fonctionne.

---
#### Exercice
Maintenant que vous savez comment effectuer un benchmark, ouvrez le fichier `benchmarking.py` [dans les exercices pendant le cours](exercices/cours) et suivez les instructions du ReadMe dans le dossier.

Commencez par exécuter les benchmarks. Les résultats correspondent-ils à votre intuition ?

Ensuite, ajoutez de nouvelles méthodes de benchmark pour tester les mêmes opérations, mais avec une liste chaînée, puis exécutez les benchmarks. Une fois encore, les résultats correspondent-ils à vos attentes ?

Enfin, écrivez un benchmark dans lequel la `list` intégrée à Python est clairement plus rapide.

<détails>
<summary>Exemple de solution (cliquez pour développer)</summary>
<p>

Il est normal que l'ajout d'une valeur au début d'une `list` soit beaucoup plus lent, car la liste doit être copiée dans un nouveau tableau afin d'ajouter un élément au début,
alors que la plupart des ajouts peuvent réutiliser le tableau existant qui n'est pas encore plein.

Une liste chaînée permet d'ajouter rapidement au début, car seuls quelques liens doivent être mis à jour.

Un benchmark simple qui est beaucoup plus rapide consiste à accéder à l'élément au milieu ou à la fin de la liste. C'est presque instantané avec une liste de tableaux, alors qu'il faut parcourir de nombreux noeuds avec une liste chaînée.

</p>
</details>

---

Avant d'utiliser vos nouvelles connaissances pour écrire des tonnes de benchmarks, voici quelques points importants à garder à l'esprit.

Méfiez-vous de trop vous concentrer sur des mesures intermédiaires qui peuvent être représentatives ou non de l'ensemble.
Par exemple, [des chercheurs ont découvert](https://dl.acm.org/doi/abs/10.1145/3519939.3523440) que certains ramasseurs de déchets pour Java avaient optimisé
le temps passé dans le ramasse-miettes au détriment du temps nécessaire à l'exécution globale d'une application. En essayant de minimiser à tout prix le temps de GC, certains GC ont en fait augmenté le temps d'exécution global.

Méfiez-vous du "problème des petites entrées": il est facile de passer à côté d'algorithmes peu performants en effectuant des tests de performance uniquement avec de petites entrées.
Par exemple, si vous triez une liste de 10 éléments, deux algorithmes de tri quelconques seront très proches l'un de l'autre, même si vous comparez un algorithme très inefficace
comme le "bubble sort" ou "tri à bulles" (https://fr.wikipedia.org/wiki/Tri_%C3%A0_bulles) à un algorithme très efficace comme le "quicksort" ou "tri rapide" (https://fr.wikipedia.org/wiki/Tri_rapide).

Faites attention à la charge de travail que vous utilisez, en particulier lorsque vous mesurez des frameworks conçus pour être invoqués parallèlement aux opérations des utilisateurs.
Par exemple, [des chercheurs ont découvert](https://www.usenix.org/conference/osdi20/presentation/pirelli) qu'un framework réseau pouvait atteindre un débit plus élevé qu'un autre lorsqu'il exécutait une fonction réseau "no-op" qui se contentait de transférer des paquets,
mais que le second était bien plus performant lorsqu'il exécutait une fonction réseau "réelle"qui inspectait le trafic et décidait quels paquets laisser passer.
En effet, le framework et le code de la fonction réseau se disputaient des ressources telles que les caches du processeur.

Un autre exemple intéressant de charge de travail est [ce problème dans le framework .NET](https://github.com/dotnet/runtime/issues/38660).
Un benchmark simple qui génère des chaînes de caractères et les place dans une carte montre d'excellentes performances pour le `HashMap` de Java par rapport au `Dictionary` de .NET, qui effectuent tous deux la même tâche.
Il s'avère que la raison en est que la fonction de hachage de chaîne par défaut de Java est très différente de celle de .NET, ce qui signifie que dans le cas spécifique de chaînes très similaires, `HashMap` semble plus rapide,
mais que `Dictionary` offre des performances similaires lorsqu'il utilise des chaînes aléatoires.

Enfin, n'oubliez pas qu'il n'est pas utile de comparer et d'améliorer un code qui est déjà suffisamment rapide.
Bien que les micro-benchmarks puissent être addictifs, vous devriez consacrer votre temps à des tâches qui ont un impact sur les utilisateurs finaux.
Accélérer une opération de 100 ms à 80 ms peut sembler formidable, mais si les utilisateurs se soucient uniquement que la tâche prenne moins d'une seconde, ils auraient probablement préféré que vous consacriez votre temps à ajouter des fonctionnalités ou à corriger des bogues.


## Comment concevoir des systèmes rapides ?

La conception de systèmes rapides est une forme d'ingénierie, tout comme la conception de systèmes corrects et sécurisés relève de l'ingénierie.
Il est important de ne pas aborder les performances sous l'angle de "trucs et astuces".
Connaître les techniques de manipulation de bits de bas niveau peut parfois s'avérer utile, mais c'est la conception d'un système qui a le plus grand impact sur ses performances.
L'idée de "performance = fonctionnalité" est une mauvaise approche. Il n'est pas facile d'"ajouter de la performance" à un système existant, de la même manière qu'il est difficile d'"ajouter de l'exactitude" ou d'"ajouter de la sécurité" à un système incorrect ou non sécurisé.

Vous voulez que votre système se situe à la [frontière de Pareto](https://en.wikipedia.org/wiki/Pareto_front) des mesures de performance que vous avez choisies.
Par exemple, pour un niveau de débit donné, il existe de nombreux systèmes avec des latences moyennes différentes, et vous souhaitez obtenir le meilleur.
Il est inutile d'avoir un système moins performant qu'il pourrait l'être.
D'un autre côté, il existe de nombreuses combinaisons de débit et de latence moyenne, et il n'est pas évident de déterminer laquelle constitue le bon compromis sur la frontière de Pareto.

Nous avons utilisé le "débit" et la "latence moyenne" dans l'exemple ci-dessus, mais il existe de nombreux axes différents.
Certains d'entre eux ne sont pas liés aux performances, mais à d'autres préoccupations telles que la maintenabilité et la lisibilité du code.
Il est souvent préférable d'optimiser la maintenabilité si le code n'a pas besoin d'être aussi rapide que possible, par exemple.
Et même au sein d'une mesure de performance telle que la latence, vous devrez trouver un compromis entre des statistiques telles que "le débit pour les types de requêtes X et Y" et d'autres telles que "une latence globale de 99,99%".
Comme il est difficile de visualiser l'utilisation de nombreux axes (https://en.wikipedia.org/wiki/10-cube), il est généralement préférable de se concentrer sur deux ou trois mesures spécifiques lorsqu'on traite des performances.

Nous verrons trois préoccupations générales en matière de performances : le flux de données, la spécialisation et l'utilisation efficace des outils disponibles.
Ces trois aspects tournent autour de la conception de systèmes qui ne font que le nécessaire, sans opérations supplémentaires ni abstractions trop générales, car le code le plus rapide est celui qui n'a pas besoin d'exister.

Le flux de données est le facteur le plus important dans la performance globale d'un système.
Un système qui traite les données par étapes, en les transférant d'un module à l'autre et en exécutant éventuellement plusieurs instances d'une étape en parallèle, sera beaucoup plus rapide qu'un système
qui copie les données partout, envoie les données par cycles entre les modules et ne peut pas être parallélisé en raison de dépendances complexes entre les étapes.
C'est l'une des principales raisons pour lesquelles les structures de données immutables sont considérées comme une bonne pratique d'ingénierie : vous n'avez pas besoin de les copier et vous pouvez les traiter en parallèle si nécessaire.
Il est facile d'écrire accidentellement du code qui copie des données entre les modules, ou pire, de concevoir un système tel que des copies de données sont nécessaires pour implémenter son interface publique.

Prenons l'exemple des tampons réseau.
Dans les réseaux traditionnels, l'application demande au système d'exploitation de recevoir les données. Le système d'exploitation demande alors à la carte réseau de recevoir les données.
Une fois que la carte a reçu les données, elle remplit un tampon fourni par le système d'exploitation, qui copie ensuite ce tampon dans un tampon fourni par l'application.
Si la copie du réseau vers un tampon est nécessaire pour stocker les données, la copie du tampon du système d'exploitation vers le tampon de l'application est une opération inutile.
Elle est nécessaire dans les systèmes réseau traditionnels, car l'application est autorisée à transmettre n'importe quel tampon, même ceux qui ne répondent pas aux exigences de la carte réseau, par exemple ceux qui ne sont pas assez grands.
Les nouvelles API réseau "zéro copie", telles que [DPDK](https://www.dpdk.org/), exigent en revanche que les applications allouent les tampons d'une manière spécifique.
L'application peut alors transmettre le tampon au système d'exploitation, qui demande à la carte réseau d'utiliser directement le tampon sans le copier.
En réfléchissant à cet exemple, vous remarquerez peut-être qu'il existe ici une forme de fuite d'abstraction : dans le modèle "zéro copie", l'application doit connaître les exigences de bas niveau de la carte réseau.
Il s'agit d'un compromis entre la maintenabilité et les performances, connu sous le nom de "contournement de couche".
Les machines virtuelles modernes fonctionnent de la même manière : il serait extrêmement lent pour l'hôte d'intercepter chaque instruction que le client souhaite exécuter, c'est pourquoi seules certaines instructions importantes sont interceptées
et la plupart des instructions sont exécutées directement.

La spécialisation est un autre aspect important des performances du système.
Écrire le système le plus polyvalent possible conduit généralement à de mauvaises performances sans apporter de réels avantages, car peu de systèmes ont besoin de traiter une très grande variété de demandes.
Par exemple, si vous voulez peindre un mur, vous choisirez un grand rouleau à peinture, et non un petit pinceau.
Le petit pinceau est utile pour tous les types de peinture, car vous ne pouvez pas utiliser un rouleau à peinture pour les petites tâches, mais il est extrêmement inefficace pour peindre un mur.
Pourtant, de nombreux systèmes finissent par faire l'équivalent de peindre un mur avec un petit pinceau, car ils sont "surdimensionnés" pour être extrêmement généraux sans que cela soit nécessaire.

Un exemple intéressant de généralité est l'instruction "a += b" dans différents langages de programmation, étant donné, par exemple, "a = 0, b = 42".
Dans un langage compilé comme Java, si `a` et `b` sont des `int`, cette addition est compilée en une seule instruction d'assemblage, telle que `add eax, ebx` en assemblage x86.
En effet, le compilateur sait exactement quelle opération doit être effectuée : l'addition de nombres entiers 32 bits.
En revanche, dans un langage interprété comme Python, l'interpréteur doit d'abord déterminer ce que sont `a` et `b`, trouver une méthode qui implémente `+=` ou `+`, puis l'exécuter.
Même après avoir déterminé qu'il s'agit d'entiers, Python a encore du travail à faire, car les entiers Python peuvent avoir une longueur illimitée et ne pas tenir dans un seul registre CPU.
il faut donc encore plus de code pour gérer le cas où le résultat de l'addition tient dans un registre et le cas où il ne tient pas.
Si tout ce que l'utilisateur voulait, c'était additionner deux petits nombres, l'utilisation de Python est très inefficace.

L'utilisation efficace des outils disponibles est le dernier aspect clé des performances du système que nous allons aborder.
À un niveau élevé, cela semble simple. Utilisez un marteau si vous voulez enfoncer un clou, et non le manche d'un pinceau, même s'il est techniquement possible d'utiliser un pinceau avec suffisamment de patience.
Aussi évident que cela puisse paraître, il existe de nombreux systèmes qui, par inadvertance, font l'équivalent d'enfoncer des clous avec un pinceau.

Prenons l'exemple du "problème de requête N+1", illustré par cet exemple :
```java
var cars = getAllCars(); // par exemple, "SELECT id FROM cars"
for (var car : cars) {
  var plate = getPlate(car); // par exemple, "SELECT plate FROM cars WHERE id = ..."
  // ...
}
```
Ce code effectue une requête pour lister les voitures, puis une requête pour chacune des N voitures afin d'obtenir son numéro d'immatriculation.
Il y a donc `N+1` requêtes, même si la base de données est parfaitement capable de renvoyer toutes les voitures et leurs plaques d'immatriculation en une seule requête.
Ce problème est rarement aussi évident que dans cet exemple de trois lignes. En général, un module à usage général appelle un autre module à usage général, qui peut être fusionné en un module efficace et spécialisé.

Prenons un autre exemple : vous devez écrire un système en Python.
Vous pourriez utiliser l'implémentation par défaut, appelée CPython, qui vous permet de faire tout ce que vous voulez.
Mais vous souhaiterez peut-être obtenir des performances supérieures en utilisant le compilateur "juste à temps"PyPy, qui prétend être trois fois plus rapide que CPython.
Cependant, PyPy n'est [pas 100 % compatible](https://pypy.org/compat.html) avec CPython, car certains cas particuliers ne se comportent pas de la même manière dans les deux.
Si vous tenez compte de ces cas limites lors de la conception de votre système, vous pouvez vous assurer que celui-ci est compatible avec PyPy, alors que la mise à niveau d'un système complexe utilisant des fonctionnalités Python avancées pour utiliser PyPy est beaucoup plus difficile.

Une fois que vous avez épuisé toutes les options générales pour une conception efficace du système, il est temps de faire des compromis.
Quels sont les cas les plus courants ? Quelles requêtes peuvent prendre plus de temps que d'autres ? Quels sont les indicateurs importants ?
Personne ne peut répondre à ces questions pour tous les systèmes possibles.


## Comment écrire du code rapide ?

Maintenant que nous avons discuté de la conception de systèmes rapides, voyons comment écrire du code rapide au niveau des fonctions et des classes individuelles.
Le processus général est le suivant :
1. Écrire un code correct, car un système incorrect qui produit des réponses rapides n'a aucun intérêt
2. Définissez un objectif de performance, afin de savoir quand vous arrêter
3. Trouvez le "goulot d'étranglement", c'est-à-dire la partie qui prend le plus de temps
4. Accélérez ce goulot d'étranglement
5. Répétez le processus jusqu'à ce que vous ayez atteint votre objectif

Commençons par un exemple simple pour discuter de l'amélioration de la latence et du débit : une pizzeria où les serveurs passent les commandes au cuisinier, qui prépare la pâte, ajoute les garnitures, cuit la pizza, puis la met dans une assiette et la remet au serveur.
Comme cet exemple traite une seule demande à la fois, le débit et la latence sont liés par une équation simple : "débit = 1 / latence".
Autrement dit, réduire le temps nécessaire à la préparation d'une pizza augmente directement le nombre de pizzas préparées par seconde.

Il existe plusieurs options simples pour réduire la latence dans notre exemple de pizzeria, comme former le cuisinier pour devenir plus rapide ou augmenter la température du four pour cuire les pizzas plus rapidement.
Il est également possible d'augmenter le débit de nombreuses façons, par exemple en embauchant davantage de cuisiniers ou en utilisant n'importe quelle méthode permettant de réduire la latence.
Cependant, le goulot d'étranglement de la pizzeria est probablement le four. Il faut plus de temps pour cuire une pizza que pour ajouter les garnitures ou la couper.
Il est inutile d'embaucher beaucoup plus de cuisiniers s'ils doivent tous attendre leur tour pour utiliser le four.
De manière plus générale, il est inutile de discuter des performances des parties du système qui ne constituent pas un goulot d'étranglement, car leurs performances ne sont pas essentielles.
Par exemple, s'il faut 90 secondes pour cuire une pizza, il n'est pas particulièrement utile de gagner 0,5 seconde lors de l'ajout du fromage sur la pizza, ou de gagner 10 nanosecondes dans le logiciel qui envoie la commande à la cuisine.

Cet exemple illustre la loi d'Amdahl, qui stipule que l'accélération globale obtenue en optimisant un composant est limitée par la part de ce composant dans le temps d'exécution global.
Par exemple, si une fonction prend 2 % du temps d'exécution total, il n'est pas possible d'accélérer le système de plus de 2 % en optimisant cette fonction, même si celle-ci est rendue beaucoup plus rapide.

Il est important de garder à l'esprit que les causes d'une mauvaise performance sont généralement quelques goulots d'étranglement importants dans le système, qui peuvent être détectés et corrigés à l'aide d'un profileur.
La fonction moyenne dans une base de code donnée est suffisamment rapide par rapport à ces goulots d'étranglement. Il est donc important de profiler avant d'optimiser afin de s'assurer que le temps de l'ingénieur est bien utilisé.
Par exemple, un amateur a réussi à [réduire les temps de chargement de 70 %](https://nee.lv/2021/02/28/How-I-cut-GTA-Online-loading-times-by-70/) dans un jeu en ligne en trouvant deux goulots d'étranglement et en les corrigeant.
Il s'agissait dans les deux cas d'algorithmes inefficaces qui pouvaient être remplacés par des versions plus efficaces sans compromettre la maintenabilité.

L'identification de ces goulots d'étranglement nécessite toujours des mesures. L'intuition est souvent trompeuse en matière de performances.
Voir les questions en ligne telles que [Pourquoi l'impression de 'B' est-elle nettement plus lente que l'impression de '#'?"](https://stackoverflow.com/questions/21947452/why-is-printing-b-dramatically-slower-than-printing)
ou ["Pourquoi le fait de changer 0.1f en 0 ralentit-il les performances de 10 fois ?"](https://stackoverflow.com/questions/9314534/why-does-changing-0-1f-to-0-slow-down-performance-by-10x).
Un autre exemple concret est [cette demande d'extraction .NET Runtime](https://github.com/dotnet/runtime/pull/76619) qui permet d'accélérer de 25 % la version de débuggage du runtime pour une entrée complexe,
en utilisant une méthode plus spécialisée pour écrire les messages de journalisation qui ne nécessite pas de verrouillage global.
On ne s'attendrait pas à ce qu'un runtime volumineux soit ralenti par un seul verrou utilisé dans les impressions de débuggage, mais cette pull request a eu un impact plus important que n'importe quelle modification apportée au compilateur ou à la bibliothèque standard du runtime.

Alors, comment mesurer le temps nécessaire à l'exécution des différentes parties du code ?
La réponse est le "profiling". 
Il existe deux principaux types de profiling : l'instrumentation, qui ajoute du code au système pour enregistrer le temps avant et après chaque opération,
et l'échantillonnage, qui arrête périodiquement le programme pour prélever un échantillon des opérations en cours à ce moment-là.
Un profileur par échantillonnage est moins précis, car il peut manquer certaines opérations si le programme ne les exécute jamais au moment où le profileur effectue son échantillonnage,
mais il a également beaucoup moins de surcharge qu'un profileur instrumentant.
Il existe de nombreux profileurs pour chaque plateforme, et certains IDE sont livrés avec leur propre profileur.

Discutons maintenant de quelques corrections de performances courantes :
choisir les structures de données et les algorithmes appropriés,
accélérer les cas courants et
éviter le travail inutile.

La complexité des structures de données et des algorithmes peut être exprimée à l'aide de la notation ["grand O"](https://fr.wikipedia.org/wiki/Comparaison_asymptotique),
qui définit la complexité asymptotique d'une opération.
Par exemple, l'ajout en tête d'une liste basée sur un tableau est en "O(N)", où "N" est la taille de la liste, car cela nécessite de copier tous les éléments dans un nouveau tableau,
tandis que la recherche de la valeur d'une liste basée sur un tableau à un index spécifique est en "O(1)", car elle prend un temps constant quel que soit l'index recherché.
À l'inverse, une liste chaînée a une préposition O(1) et une requête O(N).
Ainsi, selon l'opération requise dans un morceau de code, le choix entre ces deux listes peut faire une énorme différence.
De même, certains algorithmes sont tout simplement meilleurs que d'autres. Le tri à bulles est simple, mais toujours en O(N^2), tandis que le tri rapide est généralement en O(N log N),
on peut donc remplacer le premier par le second et améliorer presque toujours les performances.

On peut souvent accélérer les cas courants rencontrés par un système au détriment des cas rares.
Par exemple, si le profilage révèle que 90 % des requêtes adressées à un système concernent des données, tandis que les 10 % restants modifient des données,
le système peut être accéléré dans la pratique en choisissant des structures de données et des algorithmes qui accélèrent les requêtes de données, même si les modifications deviennent plus lentes.

Mais le code le plus rapide est celui qui n'a pas besoin d'être exécuté du tout.
Parfois, les opérations peuvent être combinées pour éviter d'effectuer un travail inutile.
Prenons par exemple le code suivant :
```python
sortedLst = sorted(lst)
return sortedLst[0]
```
Le tri est, dans le meilleur des cas, `O(N log N)`. La requête est alors, dans le meilleur des cas, `O(1)`.
Mais ce que ce code fait réellement, c'est obtenir le plus petit élément de la liste, c'est-à-dire `min(lst)`, ce qui peut être fait en `O(N)` en parcourant tous les éléments un par un
et en gardant trace du minimum.
Il est inutile de discuter du choix de l'algorithme de tri à utiliser ou du type de liste permettant une requête plus rapide lorsque ces deux opérations peuvent être remplacées par une opération plus simple.

Enfin, il est important de prendre du recul lorsqu'on est confronté à un code lent et de réfléchir à sa conception.
La plupart du temps, les gains ou pertes de performances les plus importants sont déterminés par la conception de haut niveau, comme nous l'avons vu plus haut.
On ne peut pas "optimiser" le tri à bulles ligne par ligne pour obtenir quelque chose d'aussi rapide que le tri rapide, car leurs conceptions sont fondamentalement différentes, ce qui conduit à des performances fondamentalement différentes.

---
#### Exercice
Essayez quelques profils de base. Ouvrez `profiling.py` dans [les exercices pendant le cours](exercices/cours) et suivez les instructions du ReadMe dans le dossier.

Les résultats du profilage correspondent-ils à vos attentes ?

Comment pourriez-vous l'accélérer ?

<détails>
<summary>Exemple de solution (cliquez pour développer)</summary>
<p>

Créer une chaîne caractère par caractère comme le fait le projet est extrêmement lent.
Chaque fois qu'un nouveau caractère est ajouté, Python copie la chaîne de caractères entière, car les chaînes de caractères en Python sont immuables.

Au minimum, vous pouvez garder les caratères dans une liste et ne la convertir en une chaîne de caratères qu'une seule fois, pour éviter toutes ces copies.
Idéalement, vous devriez travailler ligne par ligne plutôt que caractère par caractère.

</p>
</details>

---


## Quels sont les compromis courants en matière de performances ?

Une fois que vous avez épuisé toutes les améliorations générales en matière de performances dans la conception et la mise en oeuvre, il est temps de faire des compromis.
Nous aborderons quatre compromis importants, qui ne sont en aucun cas les seuls :
- Recalculer ou mettre en cache
- Chargement immédiat vs chargement différé
- Exécution immédiate vs différée
- Batching ou streaming


### Recalculer ou mettre en cache

Au lieu de recalculer une réponse à chaque requête, vous pouvez mettre en cache les réponses.
Cela fonctionne de la même manière que dans la vie réelle. Lorsque vous lisez un livre, vous le gardez sur une table à proximité, et vous avez probablement aussi une bibliothèque avec les livres que vous aimez.
Pour les nouveaux livres, ou pour ceux que vous avez lus il y a longtemps et que vous n'avez pas conservés, vous allez à la librairie.
Ce serait un énorme gaspillage d'acheter un livre chaque fois que vous voulez lire une partie d'un chapitre pour ensuite le jeter.
Cependant, il serait également inutile de conserver tous les livres que vous avez lus dans votre bibliothèque, car vous manqueriez rapidement d'espace.

Vous pourriez donc mettre en place une mise en cache comme dans ce pseudocode Python :
```python
cache = {}
def getContents(id):
  res = cache.get(id)
  if res is None:
      cache[id] = res = ...
  return res
```
Il est important de toujours évaluer si l'utilisation d'un cache en vaut la peine.
Pour les tâches qui impliquent uniquement des calculs et aucune entrée/sortie, il est souvent plus rapide de recalculer le résultat à chaque fois que d'accéder à la RAM qui contient un résultat précédemment calculé,
car les processeurs sont extrêmement rapides et la RAM l'est beaucoup moins en comparaison.

Si vous disposez d'un cache, vous pouvez également précharger les réponses, connu comme "prefetching", c'est-à-dire effectuer les requêtes que vous pensez que l'utilisateur fera plus tard afin que la réponse soit prête au moment où vous en aurez besoin.
Les sites web de vente en ligne qui vous indiquent "les clients qui ont acheté cet article ont également acheté..." en sont un exemple. Le site web a consacré une puissance de calcul supplémentaire à la recherche d'articles connexes, car il estime que vous êtes susceptible de vouloir ces articles.

Cependant, la mise en cache n'est pas aussi simple qu'il y paraît. Vous devez décider du nombre de réponses à conserver dans le cache, si les réponses expirent et, le cas échéant, après combien de temps, s'il faut précharger et, le cas échéant, dans quelle mesure, etc.
Par exemple, si vous concevez une application de prévisions météorologiques, vous ne souhaitez probablement pas fournir des réponses mises en cache pour "quel temps fait-il aujourd'hui" qui datent de plusieurs heures, car les prévisions auront changé.

Dans l'ensemble, par rapport au recalcul, la mise en cache réduit la latence et augmente le débit pour les requêtes courantes, mais elle augmente également l'utilisation de la mémoire et diminue la maintenabilité du code, car il y a plus de code et surtout une logique plus complexe.

### Chargement hâtif ou paresseux

Au lieu d'effectuer de manière _hâtive_ le travail qui pourrait être nécessaire, vous pouvez effectuer _avec paresse_ uniquement le travail strictement nécessaire.
Par exemple, les moteurs de recherche ne vous donnent pas une page avec tous les résultats de votre requête sur l'ensemble d'Internet, car vous trouverez très probablement ce que vous cherchez parmi les premiers résultats.
Au lieu de cela, les résultats suivants ne sont chargés que si vous en avez besoin. Le chargement différé réduit l'utilisation des ressources pour les requêtes qui s'avèrent finalement inutiles, mais nécessite plus de travail pour les requêtes qui sont réellement nécessaires mais qui n'ont pas été exécutées tôt.

Ainsi, vous pouvez utiliser une requête "recherche paginée" qui demande N éléments à partir de l'index M au lieu d'une requête "recherche tout" qui renvoie tous les éléments de la base de données.
Vous pouvez également choisir de n'initialiser un composant que lors de sa première utilisation, plutôt qu'au démarrage du programme :
```python
def doStuff():
  if not _initialized:
    init()
    _initialized = True
  ...
```

Cependant, le chargement différé ajoute une certaine complexité, car vous devez gérer des problèmes tels que la marche à suivre lorsque deux requêtes vers le même composant non initialisé se produisent en parallèle.
Est-il acceptable de l'initialiser deux fois ? Devriez-vous disposer d'un moyen de "verrouiller" l'accès afin que la deuxième requête attende que l'initialisation effectuée par la première requête soit terminée ?
En pratique, vous pouvez souvent utiliser des modules existants pour cela, tels que [`Lazy<T>`](https://learn.microsoft.com/en-us/dotnet/api/system.lazy-1) dans .NET.

Dans l'ensemble, par rapport au chargement immédiat, le chargement différé réduit la quantité de travail pour les requêtes inutiles, mais augmente la quantité de travail pour les requêtes nécessaires, et réduit une fois de plus la maintenabilité du code en raison d'une logique de plus en plus complexe.

### Exécution immédiate ou différée

Au lieu d'envoyer immédiatement une requête à un serveur lorsqu'un utilisateur clique sur un bouton et d'attendre la réponse du serveur,
vous pouvez différer la réponse en affichant un message "chargement en cours..." et en lançant une tâche en arrière-plan qui contacte le serveur et met à jour l'interface utilisateur une fois qu'elle a reçu une réponse.
Cela garantit que votre application reste réactive même si le serveur est lent à répondre.

Un autre exemple de ce phénomène se produit dans votre IDE : lorsque vous tapez le début d'une ligne, tel que "System.out.", l'IDE vous propose des entrées possibles, telles que "println", et peut même les trier en fonction de leur probabilité d'occurrence.
Cependant, si votre IDE bloquait toutes les opérations de l'interface utilisateur pendant qu'il calculait la liste des entrées suivantes, la saisie serait extrêmement lente.
Au lieu de cela, chaque lettre saisie lance une tâche en arrière-plan pour trouver ce que vous pourriez taper ensuite, et si une lettre suivante invalide le résultat de la tâche précédente, une nouvelle tâche est lancée.
Cela implique alors de gérer des tâches simultanées pour s'assurer que les résultats n'apparaissent pas dans le désordre, par exemple en proposant "println" même si vous avez tapé "fl" parce que vous vouliez "flush".

Il est également important de gérer les annulations, c'est-à-dire de ne pas continuer à effectuer des tâches qui ne sont plus nécessaires. Par exemple, si l'utilisateur demande la météo, mais quitte l'application pendant le chargement des données,
le code qui analyse la réponse du serveur n'a pas besoin d'être exécuté une fois que le serveur a répondu, car le résultat n'est plus nécessaire.

Dans l'ensemble, par rapport à l'exécution immédiate, l'exécution différée augmente la réactivité, mais augmente également la latence, car il y a plus de travail à faire, et réduit une fois de plus la maintenabilité du code.

### Batching ou streaming

Au lieu de télécharger un film entier avant de le regarder, vous pouvez le diffuser en streaming : votre appareil chargera le film par petits morceaux, et pendant que vous regardez les premiers morceaux, les suivants peuvent être téléchargés en arrière-plan.
Cela réduit considérablement la latence, mais diminue également le débit, car il y a plus de requêtes et de réponses pour la même quantité de données globales.

Par exemple, en Python, le traitement par lots consiste à renvoyer une `list` qui contient tous les éléments, tandis que le streaming consiste à renvoyer un "itérateur" qui récupère les éléments un par un.
Certains langages disposent même d'outils pour faciliter le streaming, tels que `yield return` en C# ou `yield` en Python :
```python
def get_zeroes():
  while True:
    print("Yielding")
    yield 0
```
Notez que ce flux est infini, ce qui serait impossible à réaliser avec un lot.
Si vous l'appelez de la manière suivante :
```python
for n in get_zeroes():
  print("n = ", n)
```
Le résultat sera "Yielding", puis "n = 0", puis "Yielding" à nouveau, puis "n = 0" à nouveau, et ainsi de suite indéfiniment.
La méthode `get_zeroes` ne s'exécute que jusqu'à `yield`, puis rend le contrôle à la boucle pour chaque itération.

Si vous appeliez `sum(get_zeroes())`, votre programme se bloquerait indéfiniment, car il tenterait d'additionner une séquence infinie.
Vous devez plutôt utiliser des méthodes qui s'arrêtent tôt si votre séquence est susceptible d'être infinie, par exemple, `next(x for x in stream if x > 5)`,
qui examine le premier élément du flux et, s'il est supérieur à `5`, le renvoie sans examiner le reste.
Sinon, il examine le deuxième élément, vérifie s'il est supérieur à `5`, et ainsi de suite.

Dans l'ensemble, par rapport au traitement par lots, le streaming réduit la latence, mais diminue également le débit.

---
#### Exercice
Optimisons une application pour améliorer sa réactivité. Utilisez le fichier `tradeoffs.py` dans [le projet d'exercices pendant le cours](exercices/cours), en commençant par l'exécuter.
Comme vous pouvez le constater, l'affichage des résultats prend un certain temps.
En examinant le code, vous pouvez voir qu'un lot entier de résultats est chargé en une seule fois.

Suivez les trois exercices indiqués dans les commentaires du code : diffusez les résultats, mettez-les en cache et ajoutez une prélecture.

<détails>
<summary>Exemple de solution (cliquez pour développer)</summary>
<p>

Pour le streaming, convertissez `getNews` en :
```python
for n in range(count):
    yield getNewsItem(index + n)
```

Pour ajouter un cache, créez une nouvelle fonction et utilisez-la dans `getNews`:
```python
CACHE = {}
def getNewsItemCached(idx):
  result = CACHE.get(idx)
  if result is None:
      CACHE[index] = result = getNewsItem(idx)
  return result
```

Pour le prefetching, commencez par re-définir une version de `getNews` qui charge tout, puis utilisez-la :
```python
def getNewsList(index, count):
    return list(getNews(index, count))

threading.Thread(target=getNewsList, args=[index + BATCH_SIZE, BATCH_SIZE]).start()
```

</p>
</details>


## Résumé

Dans cette leçon, vous avez appris :
- Définir les objectifs : latence, débit et variabilité
- Optimisation : conception, benchmarking, profiling
- Compromis courants : Cache, paresse, exec. différée, streaming

Vous pouvez maintenant consulter les [exercices](exercises/) !
