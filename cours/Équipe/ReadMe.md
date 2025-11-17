# Travail en équipe

Travailler seul signifie généralement concevoir une petite application, telle qu'une calculatrice.
Pour concevoir des systèmes plus importants, il faut des équipes, composées non seulement d'ingénieurs, mais aussi de designers, de gestionnaires, de représentants de la clientèle, etc.
Il existe différents types de tâches à accomplir, qui doivent être divisées et attribuées à différentes personnes : définition des exigences, conception, mise en oeuvre, vérification, maintenance, etc.
Bien qu'il soit théoriquement possible de permettre à n'importe qui de modifier le code à tout moment, cela conduirait rapidement au chaos.
De plus, vous souhaitez peut-être rendre votre projet « open source » et accepter des contributions extérieures.

Ce cours porte entièrement sur le travail d'équipe : qui fait quoi, quand et pourquoi ?


## Objectifs

Après ce cours, vous devriez être en mesure de :
- Organiser le développement logiciel en équipe
- Comparer les méthodes de développement
- Utiliser les revues de code constructivement
- Comprendre le développement open source


## Quelles sont les sources courantes de friction en équipe ?

La _friction_ est une cause fréquente de retards et d'annulations de projets.
Les membres d'une équipe qui sont capables d'obtenir des résultats individuellement échouent à le faire en équipe, car ils ne s'organisent pas efficacement.

N'oubliez pas qu'il n'y a pas de gagnants dans une équipe perdante.
Il n'est pas utile de faire un travail « parfait » de manière isolée s'il ne s'intègre pas au reste du travail de l'équipe ou s'il y a d'autres tâches plus importantes à accomplir, comme aider un coéquipier.
Un problème lié à la relation client n'est jamais dû à un seul membre de l'équipe, car cela implique que les personnes qui ont révisé le travail ont également commis des erreurs en ne détectant pas le problème.
C'est l'équipe contre le problème, et non une personne contre le reste de l'équipe.
Bien sûr, si la même personne continue à commettre les mêmes erreurs, l'équipe doit avoir une discussion.

Une cause particulièrement fréquente de retard est le phénomène « encore une petite chose... ».
Un membre de l'équipe, chargé d'une tâche importante, ajoute sans cesse de nouvelles sous-tâches afin que le résultat global soit « meilleur » pris isolément.
Mais comme la tâche est en retard, le résultat est en fait pire, car le reste de l'équipe est retardé en attendant ce résultat « meilleur ».

Lorsque vous estimez le temps nécessaire à la réalisation d'une tâche, gardez à l'esprit que le travail sur une tâche ne se limite pas au travail initial, mais qu'il implique également d'obtenir les commentaires des autres et d'intégrer ces commentaires.
Si vous devez terminer en 3 jours, ne planifiez pas votre travail pour qu'il dure exactement 3 jours, car vous n'aurez alors pas le temps de le réviser et d'apporter les corrections nécessaires.

En général, il vaut mieux éviter les dépendances si possible, surtout lorsque plusieurs personnes dépendent d'une seule personne.
Si cette personne n'est plus disponible ou est en retard pour une raison quelconque, les autres prendront du retard.
Il peut être préférable de prévoir un peu de travail redondant plutôt que beaucoup de dépendances.

Pour mesurer le niveau de dépendance, utilisez le « _bus factor_ » : combien de membres de l'équipe peuvent être renversés par un bus avant que le projet échoue ?
C'est une façon plutôt morbide d'envisager les choses, on peut donc aussi penser aux vacances, aux maladies ou aux urgences personnelles.
De nombreuses équipes ont un _bus factor_ de 1, car il y a au moins un membre qui est la seule personne à connaître certaines tâches importantes, certains mots de passe, certains contacts externes, etc.
Si ce membre quitte l'équipe, tombe malade ou est incapable de travailler pour une raison quelconque, l'équipe s'arrête de fonctionner car elle ne peut plus accomplir les tâches essentielles.

Même sans bus ni maladie, s'il n'y a qu'une seule personne qui « sait tout » et prend le temps de tout vérifier, comme un manager, le travail s'accumule pour être vérifié.
Les membres de l'équipe ne pourront pas terminer leurs tâches à temps, car la vérification prend plus de temps que prévu.
S'il est raisonnable qu'une seule personne ait le dernier mot sur certaines décisions, elle doit déléguer certaines vérifications et noter à l'avance les critères d'acceptation afin que les vérifications ne s'accumulent pas.
Bien sûr, l'inverse, c'est-à-dire ne désigner personne comme responsable, n'est pas non plus une bonne idée, car cela conduit à un désalignement.
Les membres de l'équipe effectuent toutes sortes de tâches sans consulter personne, certaines tâches doivent être abandonnées car elles ne sont pas nécessaires, d'autres sont dupliquées parce que deux membres de l'équipe n'étaient pas au courant, etc.

Une forme particulièrement problématique de désalignement se produit lorsqu'une personne travaille sur une tâche, la présente à l'équipe et se voit dire que la majeure partie de son travail doit être refaite
car elle n'a pas fait ce que l'équipe souhaitait réellement. Cela peut par exemple se produire dans un projet open source sans workflow clair pour proposer de nouvelles fonctionnalités.
Il doit exister un moyen pour les contributeurs potentiels, qu'ils soient membres ou non de l'équipe, d'obtenir rapidement un retour d'information sur l'acceptabilité de ce qu'ils souhaitent faire.


## Comment une équipe peut-elle minimiser la friction ?

La réponse courte tient en trois points :
1. Communiquez
2. Communiquez
3. Communiquez
Ce n'est qu'à moitié une plaisanterie. La communication est absolument essentielle. Personne ne peut lire vos pensées.

Une façon de communiquer au sein d'une équipe de développement logiciel consiste à envoyer du code pour qu'il soit révisé et mergé.
Si vous fusionnez fréquemment votre code, le reste de l'équipe sait ce que vous avez fait et peut vous faire part de ses commentaires régulièrement.
En revanche, si vous disposez d'une branche à longue durée de vie sur laquelle vous poussez du code sans demander de commentaires et sans essayer de le merge, le reste de votre équipe ne saura pas ce que vous faites,
et vous risquez de vous rendre compte trop tard que votre travail n'est pas nécessaire ou qu'il fait double emploi avec celui de quelqu'un d'autre.

Au lieu d'ajouter « une chose de plus » à une tâche, faites le contraire : divisez-la en sous-tâches qui peuvent idéalement être effectuées en parallèle afin de pouvoir être attribuées à plusieurs personnes.
Même si vous êtes le seul à travailler sur toutes les sous-tâches, fusionner de petits morceaux de code qui effectuent chacun une sous-tâche spécifique permet à votre équipe de rester plus facilement synchronisée.

Il existe conceptuellement deux façons de diviser le travail : soit « horizontalement » en termes de couches d'application, soit « verticalement » en termes de fonctionnalité de bout en bout :

<p align="center"><img alt="Illustration de la division horizontale et verticale du travail" src="images/work-split.svg" width="50%" /></p>

Par exemple, l'ensemble du travail sur la base de données pourrait être attribué à une personne, l'ensemble du travail sur l'interface utilisateur à une autre, et ainsi de suite.
Cependant, si la personne chargée de la base de données ne peut pas faire son travail, par exemple pour cause de maladie, alors quoi que fassent les autres membres de l'équipe, rien ne fonctionnera de bout en bout.
De plus, si les mêmes personnes sont continuellement affectées aux mêmes couches, le bus factor devient 1.
Au lieu de cela, les membres de l'équipe devraient être affectés à des fonctionnalités, par exemple une personne chargée de la connexion des utilisateurs, une autre chargée des messages d'information et une autre chargée du chat.

Pour les tâches qui nécessitent vraiment une coordination, telles que la définition des interfaces des modules d'une application, il est préférable d'affecter plusieurs personnes à la sous-tâche qui doit être coordonnée,
puis de les laisser travailler en parallèle sur des sous-tâches dépendantes.
Par exemple, au lieu que Alice conçoive la classe `User` et développe le flux utilisateur, puis que Bob réutilise cette classe pour développer le profil utilisateur, vous pouvez demander à Alice et Bob de
conçoivent ensemble la classe `User`, puis travaillent en parallèle sur le flux et le profil. De cette façon, non seulement Bob peut commencer et donc terminer plus tôt, mais vous n'aurez pas à faire face à une situation
où Bob doit repenser ce qu'Alice a fait parce qu'il ne lui a pas parlé de certaines fonctionnalités nécessaires pour le profil utilisateur.

Une limite importante de la coordination est la taille de l'équipe.
Si vous avez une équipe de 3 personnes, vous n'avez besoin que de 3 canaux de communication individuels.
Avec une équipe de 4 personnes, il y a 6 communications individuelles différentes.
À mesure que la taille de l'équipe augmente, le nombre de paires individuelles augmente de manière quadratique, devenant de moins en moins efficace.

Une heuristique courante est l'équipe « deux pizzas », c'est-à-dire une équipe qui pourrait être nourrie avec deux grandes pizzas, soit 4 à 8 personnes.
Au-delà, il vaut mieux se diviser en deux équipes qui travaillent sur des parties entièrement distinctes du produit final.
Avec une équipe de taille raisonnable, vous pouvez avoir des discussions fréquentes afin que tout le monde soit synchronisé et que les gens n'aient pas à jeter le travail qui ne convient pas.

Une forme extrême de discussion fréquente est le « _pair programming_ » : au lieu que deux programmeurs se coordonnent de manière asynchrone, par exemple par e-mail ou messagerie instantanée,
ils peuvent tous deux s'asseoir devant le même ordinateur, l'un agissant comme le « pilote » chargé du clavier et de la souris, et l'autre comme le « passager » donnant un retour instantané.
Cela peut également se faire à distance par vidéoconférence.
Pour les tâches qui nécessitent beaucoup d'interactions, la programmation en binôme peut être extrêmement efficace.
Certaines équipes l'apprécient tellement qu'elles imposent la programmation en binôme pour toutes les tâches, sans exception.

Une forme encore plus extrême de discussion fréquente est le « _mob programming_ » : tous les membres de l'équipe sont devant le même écran, avec un « pilote » et tous les autres en tant que « passagers ».
Cela peut être, par exemple, une alternative à une réunion de conception. Au lieu de discuter des conceptions potentielles, toute l'équipe peut rédiger la conception en une seule session de programmation en groupe.


## Quelle est la méthode d’ingénierie traditionnelle ?

Avant d'aborder la manière dont les équipes modernes s'organisent, examinons la méthode d'ingénierie traditionnelle appliquée au développement logiciel.

Le travail à accomplir est divisé en phases, telles que « conception », « mise en oeuvre » et « test ».
Le coût de la correction d'un défaut dans les exigences augmente à chaque étape. Par exemple, il est facile de mettre à jour les exigences pendant leur rédaction,
tandis que la réécriture d'une exigence pendant les tests implique de refaire une grande partie du travail déjà effectué, par exemple lors de la mise en oeuvre.
Il est donc intuitivement utile de consacrer du temps à s'assurer que les exigences sont correctes.
De plus, le fait d'avoir une structure garantit que l'équipe saura quoi faire et quand, même si elle a peu d'expérience.

L'application de cette intuition à un petit programme, tel que celui destiné aux opérations internes d'une petite entreprise, conduit à un processus simple en deux étapes :

<p align="center"><img alt="Une étape d'analyse, avec une flèche menant à une étape de codage" src="images/royce-small.png" width="50%" /></p>

Cette figure est tirée de l'article influent de Winston W. Royce publié en 1970 et intitulé « Managing the Development of Large Software Systems » (Gérer le développement de grands systèmes logiciels).
Il poursuit avec un schéma pour le développement d'un programme plus important :

<p align="center"><img alt="Étapes avec des flèches reliant chaque étape à la suivante et à la précédente : « exigences du système », « exigences logicielles », « analyse », « conception du programme », « codage », « tests », « opérations »" src="images/royce-large.png" width="50%" /></p>

Notez que Royce précise explicitement qu'il ne s'agit pas d'une méthode particulièrement efficace pour développer des logiciels.
Elle reste néanmoins un bon modèle pour la manière dont de nombreuses organisations développent des logiciels.
Elle a été baptisée « Waterfall » (cascade) en raison de l'analogie avec le flux de l'eau : une fois qu'une étape est terminée, il est impossible de revenir en arrière, tout comme l'eau qui descend une cascade ne peut remonter.

Chaque étape de la méthode Waterfall se termine par des livrables.
L'un est spécifique à l'étape, comme les exigences, la conception ou le code.
Les autres sont la documentation et la validation par le client.
Ce n'est que lorsque le résultat est documenté et que le client est satisfait que le développement passe à l'étape suivante.

Waterfall présente certains avantages.
Tout d'abord, elle garantit que les exigences sont validées dès le début avec le client, car le développement ne peut se poursuivre qu'une fois que cela a été fait.
Deuxièmement, elle impose une structure avec des objectifs clairs, car l'équipe sait toujours à quelle étape elle se trouve et quel est le livrable.
Enfin, elle garantit que tout est documenté et qu'il n'y a pas de surprises, comme oublier d'effectuer une tâche qui a été retardée depuis longtemps, car ces tâches ne peuvent être retardées qu'au sein de chaque étape.

La méthode Waterfall est donc un bon choix pour les projets dont la technologie est stable, les exigences stables, l'équipe éventuellement inexpérimentée et qui impliquent une certaine bureaucratie externe imposant aux développeurs des étapes de type Waterfall.
Il est assez courant que les organisations non techniques souhaitent modéliser le développement de projets techniques selon un schéma qui leur est familier, auquel cas la méthode Waterfall peut s'avérer tout à fait adaptée.
Un exemple typique est celui des voyages spatiaux. Le développement d'un robot destiné à aller sur la Lune ou sur Mars est un bon cas d'utilisation de Waterfall, car les exigences sont connues et il n'y a aucune possibilité d'obtenir un feedback précoce, le lancement d'un seul robot étant extrêmement coûteux.

Cependant, Waterfall nécessite que toutes les exigences soient fixées très tôt et ne procède à la validation du produit qu'à un stade tardif, car il n'y a pas de produit fonctionnel avant la toute fin.
Elle est donc peu adaptée aux projets dont la technologie ou les exigences ne sont pas complètement stables, en particulier si l'équipe est expérimentée et qu'il n'y a pas trop de bureaucratie.
Cette description correspond en fait à la plupart des projets ! La méthode Waterfall n'est généralement pas adaptée au développement logiciel moderne.

Un exemple couramment utilisé pour illustrer les inconvénients de la méthode Waterfall est le système de bagages de l'aéroport de Denver, une histoire qui a donné lieu à de nombreuses études de cas (par exemple, [ici](https://peimpact.com/the-denver-international-airport-automated-baggage-handling-system/)).
Les travaux sur le système de bagages du nouvel aéroport de Denver ont commencé en juin 1991, la livraison étant prévue pour octobre 1993, date d'ouverture de l'aéroport.
Après de nombreux retards dus au fait que le système automatisé de bagages n'était pas prêt, l'aéroport a ouvert ses portes en février 1995.
Cependant, à ce moment-là, le système n'était utilisé que pour une partie des vols d'une seule compagnie aérienne, car il ne pouvait répondre à aucune des exigences initiales.
Le développement a été entravé par des exigences trop complexes pour être mises en oeuvre de manière réaliste et par des retours tardifs qui ont entraîné des changements majeurs, deux symptômes d'un développement des exigences isolé du reste du processus.
D'autres études de cas ont été rédigées, par exemple [les difficultés rencontrées par Ericsson](https://link.springer.com/chapter/10.1007/978-3-642-02152-7_29), là encore en raison de modifications tardives des exigences
et de tests compromis pour respecter les délais du projet.

Winston W. Royce a conclu son article par un plan plus « réaliste » pour le développement de logiciels, qui est beaucoup plus complexe que les diagrammes originaux :

<p align="center"><img alt="14 étapes, certaines en double, 11 entrées et sorties, et un nombre extrêmement élevé de flèches..." src="images/royce-final.png" width="50%" /></p>

Nous n'aborderons pas ce diagramme plus en détail, mais il est important de rappeler que même l'article originel sur la méthode Waterfall ne recommandait pas réellement cette méthode pour le développement logiciel en général.
Il existe de nombreuses autres méthodologies de développement logiciel, souvent inspirées des étapes de base de la méthode Waterfall.
Par exemple, le « [modèle en V](https://en.wikipedia.org/wiki/V-Model) » tente de représenter Waterfall avec davantage de liens entre la conception et les tests,
et le « [modèle en spirale](https://en.wikipedia.org/wiki/Spiral_model) » est conçu pour minimiser les risques en effectuant de nombreuses itérations du même cycle.

---

#### Exercice
Pour lequel des projets suivants pourriez-vous utiliser Waterfall ? Pourquoi ou pourquoi pas ?
- Une application compagnon pour campus
- Une fusée étudiante pour une compétition interuniversitaire
- Le noyau Linux
- Une réécriture de Microsoft Word (pour obtenir des fonctionnalités similaires avec un code plus simple)

<details>
<summary>Exemple de solution (cliquez pour développer)</summary>
<p>

- Une application compagnon pour le campus est un très mauvais candidat, car ses besoins ne sont pas clairs, les fonctionnalités possibles étant extrêmement nombreuses, et il faudrait régulièrement recueillir les commentaires des utilisateurs finaux pendant le développement
- Un concours de fusées étudiantes est un bon candidat, pour les mêmes raisons que celles qui s'appliquent aux voyages spatiaux en général
- Le noyau Linux pourrait utiliser Waterfall pour des sous-projets spécifiques, tels que la conception d'un pilote logiciel pour un matériel spécifique, mais pour l'ensemble du projet, Waterfall ne fonctionnerait pas
- La réécriture d'un logiciel, ou une « version 2 » en général, peut être un bon cas d'utilisation pour Waterfall, car les exigences sont précisément connues

</p>
</details>


## Comment les équipes modernes s’organisent-elles ?

En réaction aux lacunes des processus rigides de type Waterfall, les processus modernes tentent d'aller dans la direction opposée.
Au lieu d'attendre les commentaires tardifs des utilisateurs sur le produit, recueillez leurs commentaires aussi souvent que possible.
Au lieu d'un long cycle de développement au terme duquel le produit n'est utilisable qu'à la fin, prévoyez plusieurs cycles de développement courts qui aboutissent chacun à une amélioration utilisable.
Au lieu d'une bureaucratie lourde autour des délais et de la documentation, optez pour une bureaucratie légère et concentrez-vous sur les résultats.

Ces principes ont été formalisés dans le ["Manifeste agile"](https://agilemanifesto.org/), une déclaration rédigée par de nombreuses personnes intéressées par l'amélioration du développement de logiciels, qui comporte quatre valeurs fondamentales :
- Les individus et les interactions plutôt que les processus et les outils
- Les logiciels fonctionnels plutôt que la documentation exhaustive
- La collaboration avec les clients plutôt que la négociation de contrats
- Répondre au changement plutôt que suivre un plan
Comme ils l'affirment, bien qu'ils accordent de l'importance aux éléments de droite, ils accordent davantage d'importance à ceux de gauche.
Ils présentent en outre des [principes](https://agilemanifesto.org/principles.html) qu'ils considèrent comme fondamentaux pour les logiciels agiles.

Il est important de noter la différence entre le développement « agile », principe général auquel fait référence ce manifeste, et les différentes formes d'« Agile » avec un A majuscule qui ont vu le jour au fil des ans.
De nombreuses entités ont inventé leur propre version du développement agile, qu'elles ont formalisée en processus complexes qu'elles vendent aux entreprises comme une solution « Agile » magique à tous leurs problèmes de développement.
En général, si cela nécessite des formations ou des certifications, il est peu probable qu'il s'agisse d'une méthode de développement agile.

La forme la plus courante de développement agile pratiquée aujourd'hui est _Scrum_, qui a été [décrite](https://doi.org/10.1145/260111.260274) par ses auteurs de la manière suivante :

> La philosophie déclarée et acceptée pour le développement de systèmes est que [le] processus de développement de systèmes est une approche bien comprise qui peut être planifiée, estimée et menée à bien.
> Il s'agit là d'un postulat erroné.
> Scrum affirme que le processus de développement de systèmes est un processus imprévisible et complexe qui ne peut être décrit que de manière approximative comme une progression globale.
> Scrum définit le processus de développement de systèmes comme un ensemble d'activités souples qui combine des outils et des techniques connus et fonctionnels avec le meilleur de ce qu'une équipe de développement peut concevoir pour construire des systèmes.
> Ces activités étant souples, des contrôles sont utilisés pour gérer le processus et les risques inhérents.

L'idée centrale est que nous ne pouvons véritablement contrôler le développement qu'à un niveau élevé, lorsque nous réfléchissons à la progression globale, car les étapes individuelles sont imprévisibles.
Nous devons donc ajouter quelques garde-fous simples au niveau inférieur afin d'atténuer les risques à ce niveau.

Scrum se compose des éléments suivants :
- L'objectif du produit, qui est l'objectif vers lequel l'équipe travaille, par exemple un système logiciel spécifique pour un client
- Du « backlog » de produit, une liste ordonnée d'éléments à réaliser pour atteindre l'objectif produit, qui peut être élargie si nécessaire lorsque de nouveaux besoins apparaissent
- D'une séquence de « sprints », qui subdivisent le travail en unités de temps, chacune avec :
  - Son objectif, la partie du backlog de produit qui sera réalisée pour ce sprint et qui se transformera en « incréments » fonctionnels vers l'objectif produit
  - Son « backlog », une liste ordonnée de tâches à accomplir pour atteindre l'objectif du sprint
Dans chaque sprint, en plus de son travail quotidien, l'équipe Scrum commence par une réunion de _Sprint Planning_ pour définir le sprint, et termine par une _Sprint Review_ orientée vers le client et une _Sprint Retrospective_ pour décider des améliorations à apporter au processus.

Examinons maintenant chacun de ces éléments plus en détail.

L'équipe Scrum est composée d'un _Scrum Master_, qui facilite le processus, d'un _Product Owner_, qui représente les clients, et de développeurs.
Il n'y a ni hiérarchie ni sous-équipes au sein d'une équipe Scrum.
Le Scrum Master n'est pas un manager, mais plutôt un « leader serviteur », qui aide le reste de l'équipe en organisant et en animant les réunions souhaitées par l'équipe, en gérant les contraintes externes, etc.
En général, comme ce travail ne représente pas une charge de travail à temps plein, le Scrum Master est également développeur.
Le Product Owner est le seul représentant de tous les clients et gère les backlogs. Le Product Owner a le dernier mot sur ce qui est ajouté au backlog et dans quel ordre, et personne d'autre n'est autorisé à modifier directement le backlog.
En particulier, les utilisateurs ne peuvent pas demander directement des fonctionnalités à des développeurs individuels ni modifier eux-mêmes le backlog, car cela conduirait au chaos.

Lorsque vous travaillez dans des équipes de développement logiciel, vous pouvez rencontrer d'autres rôles tels que « Tech Lead », « Engineering Manager », « Product Manager », etc.
Ces rôles ont un objectif et peuvent être utiles dans certains cas, mais ils ne font pas partie de Scrum, même si de nombreuses organisations prétendent adhérer à Scrum tout en ayant de nombreux rôles sans rapport avec celui-ci et parfois même pas les rôles Scrum de base.
Comme Scrum et le développement agile en général sont très populaires, il existe un écart important entre les définitions originales et ce que les gens font dans la pratique sous ces noms.

Un sprint dans Scrum consiste en un objectif et un backlog, réalisables dans un laps de temps donné.
En général, tous les sprints ont la même durée, généralement comprise entre 1 et 4 semaines.
Scrum étant agile, si un sprint n'est plus utile ou nécessite des changements majeurs, il n'est pas nécessaire de le poursuivre uniquement pour respecter le processus.
Au contraire, le Product Owner peut modifier ou annuler un sprint si nécessaire.

La réunion de planification du sprint permet de définir le backlog du sprint afin de décider des incréments de travail que l'équipe souhaite réaliser au cours du sprint.
Un incrément est une combinaison d'un élément du backlog du produit et d'une "_Definition of Done_", c'est-à-dire une déclaration claire qui définit si une tâche a été accomplie d'une manière qui nécessite un minimum d'interprétation.
Au cours de la réunion de planification, l'équipe hiérarchise les tâches, par exemple en fonction de ce qui serait le plus utile pour l'utilisateur, de ce qui présente le moins de risques, etc.
Les éléments du backlog de produit sont divisés en tâches sur lesquelles les développeurs individuels peuvent travailler, en estimant leur temps d'achèvement afin qu'aucune tâche ne soit trop longue et qu'aucun développeur n'ait trop ou trop peu de travail.

Voici, par exemple, quelques _bons_ exemples de tâches, avec une définition implicite de ce qui est terminé :
- « _Ajouter un emplacement public aux profils des utilisateurs_ »
- « _Permettre aux utilisateurs de trier les restaurants par type ou par note_ » 

Voici quelques _mauvais_ exemples de tâches, qui sont beaucoup trop vagues :
- « _Mettre en place un profil utilisateur_ » (que doit-il contenir ? Qu'est-ce qui est modifiable et qu'est-ce qui ne l'est pas ? Qu'est-ce qui est visible publiquement et qu'est-ce qui ne l'est pas ?)
- « _Générer un meilleur contenu de cours_ » (que signifie « meilleur » ? Comment le contenu sera-t-il généré ?)

Idéalement, une seule tâche devrait représenter 1 à 2 jours de travail pour un seul développeur, avec des estimations de temps réalistes.
Il est important d'éviter la mentalité « tout ira parfaitement bien » et de garder à l'esprit la nécessité de tester, de réviser le code et de s'adapter aux commentaires issus de la révision.
Même si les tâches peuvent parfois être plus importantes que cela, plus une tâche est importante, plus elle risque d'être mal spécifiée et de causer plus tard des conflits de fusion.

La division des éléments du backlog en tâches relève davantage de l'art que de la science, et les développeurs s'améliorent à mesure qu'ils s'y exercent.
Prenons par exemple l'élément « _Permettre aux utilisateurs de trouver des lieux d'intérêt à proximité_ ». Nous pourrions le diviser en « _Permettre aux utilisateurs de définir ou de détecter automatiquement leur emplacement_ », « _Importer les emplacements depuis la base de données_ » et « _Trier les lieux par distance_ ».
Cela dépend bien sûr de la complexité de chaque élément dans son contexte. Il se peut que la détection automatique de l'emplacement soit difficile sur la plate-forme spécifique sur laquelle fonctionne l'application, et que la première tâche doive plutôt être divisée en deux tâches, par exemple.

Il est important de noter que les éléments du backlog de produit sont toujours traités de haut en bas, car le backlog est ordonné.
Le Product Owner peut décider de réorganiser le backlog de produit en fonction des commentaires des clients.

Pour en revenir aux composants du sprint, pendant la partie active du sprint, les développeurs doivent se réunir pour une réunion quotidienne dite "_Daily Scrum_", souvent appelée « _standup_ », car elle doit être suffisamment courte pour que la plupart des participants n'aient pas besoin de s'asseoir.
Le standup peut se dérouler en personne, par vidéoconférence ou même par messagerie instantanée, selon les préférences de l'équipe.
Au cours de la réunion standup, chaque développeur résume rapidement ce qu'il a fait la veille, ce sur quoi il va travailler aujourd'hui et s'il est bloqué par quelque chose.

Outre le fait de synchroniser l'équipe, l'objectif principal de la réunion standup est d'identifier les obstacles : les problèmes qui empêchent un développeur d'accomplir son travail.
Tout ce qui ressemble à « Je ne peux pas continuer mon travail parce que... » est un obstacle, même si ce n'est pas formulé ainsi.
En particulier, tout le monde ne sait pas forcément qu'il est bloqué ! Par exemple, quelqu'un peut supposer qu'il est normal qu'il ne puisse pas accomplir sa tâche de manière simple et déclarer qu'il cherche une méthode plus complexe qui prendra beaucoup plus de temps.
Un coéquipier peut alors déclarer qu'il s'attendait vraiment à ce que la méthode simple fonctionne et suggérer aux deux personnes de se rencontrer peu après la réunion debout pour en discuter, dans l'idéal afin de débloquer leur collègue.

À la fin du sprint, lors de la réunion de revue du sprint, l'équipe présente son travail au propriétaire du produit, généralement sous la forme d'une démonstration du logiciel.
Ce n'est pas nécessairement le seul moment où l'équipe peut faire une démonstration. Il est tout à fait acceptable de s'entretenir avec le propriétaire du produit pendant un sprint pour lui demander son avis sur une démonstration, par exemple.
La revue sert à discuter des résultats liés au produit, tels que ce que l'équipe a appris sur la faisabilité et la hiérarchisation possible des tâches futures.

Enfin, il y a la rétrospective du sprint, qui porte sur le processus.
L'équipe se réunit pour discuter de ce qui a fonctionné et de ce qui n'a pas fonctionné, dans une sorte d'« autopsie » du sprint.
Un résultat courant d'une rétrospective est une liste de trois catégories : « Arrêter de faire..., Commencer à faire..., Continuer à faire... ».
Comme Scrum est axé sur l'agilité, même le processus Scrum lui-même peut être modifié si nécessaire.
Par exemple, l'équipe estime peut-être qu'il serait préférable de n'avoir une réunion debout qu'un jour sur deux et souhaite tester cette solution pendant un sprint.

Dans l'ensemble, n'oubliez pas que les processus agiles sont avant tout une question d'agilité.
Si vous trouvez un bug mineur, vous pouvez et devez le corriger immédiatement. Il n'est pas nécessaire d'ouvrir un ticket officiel et de demander l'avis du Product Owner si vous pouvez le corriger en 10 minutes.
Si vous rencontrez un problème inhabituel qui, selon vous, pourrait compromettre le développement futur, tel qu'une bibliothèque externe ne disposant pas des fonctions attendues par l'équipe pour les tâches futures, discutez-en rapidement avec l'équipe.
Si vous avez une idée pour gagner du temps, par exemple un moyen de réaliser 80 % d'une tâche en 20 % du temps prévu, discutez-en rapidement avec l'équipe et le Product Owner. Ils seront peut-être d'accord et la définition de « terminé » pour votre tâche changera.
Ne suivez pas le processus pour le simple plaisir de suivre le processus.

Gardez également à l'esprit l'objectif global lorsque vous réfléchissez aux éléments du backlog et aux tâches.
Par exemple, si vous souhaitez construire un grand manoir avec des murs en pierre renforcés, il est inutile de commencer par des [murs en pierres sèches](https://fr.wikipedia.org/wiki/Ma%C3%A7onnerie_%C3%A0_pierres_s%C3%A8ches) comme forme simple de mur,
car vous aurez besoin de mortier pour construire la maison. Votre première tâche après avoir construit le mur en pierres sèches sera donc de le démanteler et de construire un mur avec du mortier cette fois-ci.
Il faut de l'expérience et de l'expertise pour savoir quels « raccourcis » sont réellement des raccourcis et lesquels vous mènent sur la mauvaise voie.


---

#### Exercice

Créez un objectif produit et un backlog produit, avec au moins 5 éléments, pour un projet que vous aimeriez réaliser.

Il peut s'agir de n'importe quoi, par exemple une application de podcasts, un gestionnaire de tournois d'échecs, un site web d'inscription à des événements, etc.

---

Si les itérations en sprints courts sont une bonne chose, les itérations en sprints extrêmement courts sont-elles extrêmement bonnes ? Peut-être.
C'est l'idée centrale derrière le Kanban en tant que philosophie de développement logiciel.
Au lieu de sprints explicites, le Kanban implique un tableau avec des colonnes pour les différents états des éléments.
L'équipe maintient la colonne « Backlog » dans un ordre trié, puis déplace les éléments au fur et à mesure du développement :

<p align="center"><img alt="Un tableau Kanban simple avec les colonnes « Backlog », « Specification », « Implementation », « Review », « Done » et « Blocked »" src="images/kanban.svg" width="50%" /></p>

Il est important de noter qu'il existe une limite pour chaque colonne, ce qui signifie qu'il ne peut y avoir plus d'un certain nombre d'éléments dans un statut donné à un moment donné.
Par exemple, si vous souhaitez soumettre votre code à une revue pour un élément, mais que la colonne Revue est pleine, vous devez effectuer une revue de code pour l'un des éléments de cette colonne afin de libérer une place.
Pour compenser cela, il existe une zone « bloquée » pour les éléments qui sont bloqués pour des raisons indépendantes de la volonté de l'équipe, par exemple parce qu'ils attendent une autre équipe.

Le concept de « tableau Kanban » est largement utilisé même en dehors du Kanban, souvent sans limite du nombre d'éléments par statut.
Il est courant d'utiliser un tableau de type Kanban pour les projets Scrum, par exemple.


## Comment fournir et recevoir du feedback utile sur du code ?

Que faire une fois que vous avez terminé une tâche de codage ? La merge directement dans la branche principale ?
Malheureusement, les êtres humains sont imparfaits et nous commettons tous des erreurs. Il peut y avoir des bugs, des cas limites non traités, des tests manquants, de mauvais choix de conception, etc.
Les interactions entre le code nouveau, modifié et existant peuvent cacher toutes sortes de problèmes.
Par exemple, une nouvelle sous-classe peut provoquer le plantage du code existant, soit parce que la nouvelle classe ne respecte pas les postconditions de sa classe de base, soit parce que le code existant faisait des hypothèses plus fortes que les postconditions de la classe existante.
Plus délicat encore, il peut manquer du code, par exemple pour gérer des cas limites spécifiques. Il est plus difficile de déterminer quel code n'a pas été ajouté mais devrait l'être que de déterminer si le code ajouté est correct.

Les revues de code réduisent la probabilité d'erreurs en faisant examiner le code par une autre personne.
Ce n'est bien sûr pas un concept nouveau, puisqu'il existe dans tout autre processus de création d'un résultat, comme donner son avis sur le brouillon d'un livre.
Et cela a commencé il y a longtemps, même dans le domaine du génie logiciel, avec Ada Lovelace [suppliant Charles Babbage](https://web.archive.org/web/20241212033625/https://www.iflscience.com/relatable-ada-lovelace-letter-shows-her-begging-charles-babbage-not-to-mess-with-her-math-65640) de cesser de modifier ses programmes, car il y introduisait des erreurs.

Si quelqu'un suggère des modifications au code et qu'une autre personne les examine, qui est responsable des bogues restants dans le code après avoir été merge sur la branche principale ?
Il s'agit d'une question piège : la réponse est « toute l'équipe ». L'objectif n'est pas de blâmer les individus pour leurs erreurs humaines, car nous savons que celles-ci continueront de se produire même si quelqu'un d'autre lit le code, mais simplement moins souvent.
Si la même personne commet systématiquement les mêmes erreurs, une intervention est nécessaire, mais sinon, l'objectif est de fournir un logiciel de qualité, et non de déterminer qui a commis le plus d'erreurs.

Une forme de revue est le "pair programming" : si deux personnes travaillent sur un morceau de code, elles pourraient décider de renoncer au processus de revue, car le code a déjà été vérifié par une deuxième paire d'yeux.
D'un autre côté, les deux personnes peuvent partager les mêmes préjugés et les mêmes angles morts si elles ont travaillé ensemble, les équipes doivent donc décider comment traiter le code programmé en binôme en termes de revue.

Les revues de code sont particulièrement importantes si vous recevez du code provenant d'une personne que vous ne connaissez pas ou en qui vous n'avez pas confiance, comme une proposition d'une personne sur Internet visant à fusionner du code dans votre projet accessible au public.
Cette personne a peut-être écrit un excellent code, ou elle a peut-être commis de nombreuses erreurs. Elle pourrait même être [malveillante](https://fr.wikipedia.org/wiki/Attaque_de_XZ_Utils_par_porte_d%C3%A9rob%C3%A9e) !

Alors, qu'est-ce qu'une revue de code ? Conceptuellement, c'est simple :
1. Lire le code
2. Écrire des commentaires sur le code
3. Accepter ou rejeter le code
En général, le « rejet » à la dernière étape n'est pas définitif, mais s'apparente davantage à « veuillez corriger les problèmes que j'ai signalés et soumettre à nouveau le code pour une autre révision ».

Les révisions de code peuvent se faire [par e-mail](https://marc.info/?l=linux-fsdevel&m=176284687628463&w=2) ou à l'aide d'outils en ligne tels que les [pull requests de GitHub](https://github.com/dotnet/runtime/pull/121489).
Mais quel est exactement l'objectif, qui doit les effectuer et comment donner et recevoir de bonnes révisions de code ? Examinons ces quatre points tour à tour.

### Objectifs de la revue du code

Au premier abord, l'objectif peut sembler se limiter à « trouver des bugs », mais en fait pas seulement.
Heureusement, il existe des recherches empiriques sur la révision du code, dans lesquelles des chercheurs interrogent de nombreux ingénieurs logiciels afin de recueillir leur opinion.
Voici, par exemple, les principales motivations des développeurs pour la révision, telles que recueillies par [Bacchelli et Bird](https://doi.org/10.1109/ICSE.2013.6606617) en 2013 :

<p align="center"><img alt="« Motivations classées par les développeurs », dans l'ordre : « Trouver des défauts », « Amélioration du code », « Solutions alternatives », « Transfert de connaissances », et quelques autres » src="images/bacchelli-bird-goals.png" width="50%" /></p>

Sans surprise, la recherche de défauts arrive en tête, suivie de près par l'amélioration du code, c'est-à-dire la proposition de meilleures méthodes même si le code soumis ne comporte pas de bugs, et les solutions alternatives, c'est-à-dire la proposition de meilleurs choix de conception.
Par exemple, au lieu d'une solution de 100 lignes, la personne qui lit le code pourrait signaler qu'il existe déjà une méthode dans la base de code qui fait ce que le soumissionnaire du code voulait faire.

Vient ensuite le transfert de connaissances, autre objectif clé de la révision de code dans la pratique.
Les revues de code ne sont pas un monologue, mais un dialogue entre l'auteur et le réviseur.
N'oubliez pas le « bus factor » : vous ne voulez pas qu'un projet échoue parce que la seule personne qui connaissait une partie du code est malade ou quitte l'équipe.
En imposant des révisions de code, vous garantissez qu'au moins deux personnes connaissent chaque partie du code.
Cela peut également être une bonne occasion pour les ingénieurs seniors d'expliquer certaines choses aux ingénieurs juniors.

### Auteurs de la revue de code

Qui devrait être le reliseur de code ? Si la recherche de défauts et la proposition de solutions alternatives nécessitent une connaissance approfondie du code modifié, comme l'ont constaté Bacchelli et Bird dans le même article,
d'autres objectifs, tels que le transfert de connaissances, peuvent bénéficier de réviseurs moins expérimentés.
Il y a un compromis évident : plus il y a de personnes qui relisent, plus il y a de commentaires et plus le transfert de connaissances est important, mais plus il faut de temps avant que le code puisse être mergé.

Dans la pratique, il est courant de désigner un « propriétaire » du code, c'est-à-dire une personne responsable de la partie du code en cours de modification.
Cette procédure peut être mise en oeuvre à l'aide d'outils tels que [le fichier `CODEOWNERS` de GitHub](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners),
qui exige que les pull requests soient approuvées par les personnes désignées comme propriétaires du code.
Il peut être utile de demander à d'autres personnes de relire le code afin d'apprendre et de fournir des commentaires mineurs, mais cela n'est généralement pas obligatoire.

### Réaliser une bonne revue de code

Examinons trois aspects de la revue de code : l'approche globale, les commentaires et certains facteurs humains.

Tout d'abord, afin d'aborder correctement la chose, vous devez prévoir du temps pour la réaliser, par exemple 10 à 15 minutes.
À moins que le code ne soit particulièrement complexe, vous ne devriez pas avoir besoin de beaucoup plus de temps.
Si vous avez besoin d'une heure pour comprendre une pull request, cela signifie soit que le code est trop confus, soit que la pull request devrait être divisée en plusieurs parties plus petites.

Vous pouvez lire le code en ligne sur la plateforme où la pull request est effectuée, ou localement en récupérant la branche et en l'ouvrant dans votre éditeur.
Certains éditeurs sont même intégrés à des outils de revue de code, ce qui vous permet d'ajouter des commentaires depuis l'éditeur.
Cependant, vous ne devriez généralement pas avoir besoin d'exécuter le code vous-même, c'est à cela que servent les tests automatisés et l'intégration continue.

Décidez quelles parties vous allez lire attentivement, parcourir rapidement et ignorer.
Il peut être utile d'ignorer certains codes si vous faites confiance à la personne qui les a soumis et que les modifications ne sont pas intéressantes, comme une refonte qui a changé le nom d'une méthode ou l'ajout d'un fichier de ressources dont vous connaissez déjà le contenu.
Si nécessaire, vous pouvez déléguer, par exemple parce que vous n'êtes pas sûr de votre capacité à examiner les modifications apportées à un module spécifique.
Une fois votre examen terminé, documentez ces choix à l'aide de commentaires tels que « Je n'ai examiné que... parce que... » ou « Je te fais confiance... donc je n'ai pas lu... ».

La connaissance peut être acquise grâce à la discussion.
Parfois, cette discussion consiste à souligner des faits, d'autres fois à poser des questions.
Voici quelques exemples de **bons** types de commentaires :
- « _Je ne comprends pas pourquoi..._ »
- « _Si `x = -1` ici, je pense que cela va planter, car..._ »
- « _Pourrions-nous déplacer ce bout de code vers la classe X, afin que..._ »
Tous les commentaires ne doivent pas nécessairement être critiques ou signaler des problèmes. Il est judicieux de laisser des commentaires tels que « _C'est génial ! J'aime beaucoup..._ » si vous pensez qu'une partie du code est bien faite !

Voici, en revanche, quelques exemples de **mauvais** commentaires et pourquoi :
- « _Je n'aime pas ça_ »  
  (Il ne s'agit pas de vos préférences personnelles, mais de celles de l'équipe)
- « _Améliore ça_ »  
  (Comment ? Ce n'est pas constructif)
- « _Ton code est stupide_ »  
  (Tout ce que cela fait, c'est mettre l'auteur sur la défensive, ce qui ne mène à rien)
- « _Faisons également cette modification sur ces 40 autres fichiers_ »  
  (Vous pouvez proposer de faire une autre pull request pour cela, mais n'étendez pas la portée d'une demande existante sauf si cela est vraiment nécessaire)
- « _Je l'aurais fait..._ »  
  (Quand quelqu'un d'autre effectue une tâche, il ne la fera jamais à 100 % comme vous le souhaitez)
- « _À mon avis..._ »  
  (Encore une fois, il s'agit de l'avis de l'équipe, vous devez étayer vos commentaires par des faits partagés, et non par des préférences personnelles)

Une façon de rendre vos commentaires plus exploitables consiste à les classer par catégorie, par exemple
- « _**Question** : Pourquoi devons-nous vérifier cette condition... ?_ »
- « _**Bloqueur** : Cette condition doit inclure..._ »
- « _**Mineur** : Peut-être qu'un meilleur nom pour cette méthode serait..._ »
De cette façon, l'auteur de la soumission sait ce qu'il doit traiter (= « bloqueurs »), ce qu'il peut choisir de prendre ou non (= « mineurs » / "_nitpicks_" en anglais) et quelles questions sont vraiment des questions par opposition à des questions rhétoriques.

N'oubliez pas de justifier vos commentaires, afin que l'auteur de la soumission dispose du contexte et puisse discuter de manière plus constructive, par exemple « _... conformément à nos conventions de formatage_ » ou « _... comme nous en avons discuté jeudi dernier_ ».
Il se peut qu'il y ait eu un malentendu sur ce qui devait être fait jeudi dernier, par exemple. Dans ce cas, ajouter ce contexte vous permet de clarifier directement ce malentendu.

Gardez une vue d'ensemble. Vous examinez le code pour trouver des problèmes et des améliorations potentiels, mais aussi pour en apprendre davantage à son sujet.
Demandez-vous si l'architecture est cohérente, quels tests pourraient manquer, etc. Il est inutile de laisser une révision composée uniquement de commentaires « mineurs ».
Parfois, vous pouvez simplement laisser « _LGTM_ », qui signifie « _Looks Good To Me_ » (ça me semble correct), si vous pensez que le code est correct. Cela est particulièrement vrai pour les petites demandes de modification qui effectuent des tâches simples.

Enfin, n'oubliez pas les facteurs humains.
Les revues de code ne visent pas à montrer qui est le plus intelligent, ce n'est pas « moi contre toi », mais « nous contre le problème ». Votre objectif global est de fournir un logiciel fonctionnel et vous collaborez avec la personne qui a soumis le code.
N'écrivez pas de commentaires tels que « Tu fais... », mais concentrez-vous sur le code, par exemple « Le code fait... », afin de ne pas mettre les gens sur la défensive.
Et n'oubliez pas que des malentendus culturels peuvent survenir. Par exemple, une personne originaire des États-Unis qui dit que le code est « _quite good_ » veut dire qu'il est bon, mais un lecteur britannique pensera qu'il est plutôt mauvais, car les mots ont des significations différentes selon les cultures.
Vous ne pouvez pas éviter les malentendus, mais vous pouvez garder leur possibilité à l'esprit afin de ne pas immédiatement faire une mauvaise interprétation et poser plutôt des questions pour clarifier les choses.

### Bien recevoir une revue de code

Les révisions de code sont collaboratives, donc la personne qui soumet le code a également la responsabilité de faire de son mieux.
Examinons trois aspects : aider les autres à vous aider, obtenir rapidement des commentaires et gérer les mauvaises révisions.

Commencez par résumer vos modifications dans la description de toute demande d'extraction que vous créez, en incluant tout ce que vous souhaitez signaler aux réviseurs potentiels.
Réfléchissez aux questions « évidentes » qu'un réviseur pourrait se poser au départ, afin de pouvoir passer immédiatement à l'étape suivante de la conversation.
Par exemple, vous pourriez dire certaines des choses suivantes :
- « _J'ai implémenté X comme décrit dans la tâche, mais cela m'a également obligé à modifier Y, car..._ »
- « _J'ai utilisé le modèle Middleware, car..._ »
- « _Je ne suis pas sûr de l'implémentation de..._ »

Avant de demander à quelqu'un d'autre de réviser votre code, comme pour tout autre résultat que vous produisez, effectuez vous-même une révision afin de détecter les erreurs élémentaires.
Peut-être avez-vous oublié de supprimer du code que vous aviez ajouté lors du débogage. Peut-être avez-vous commenté une ligne et oublié de la décommenter. Peut-être avez-vous modifié un fichier par accident.
Au lieu d'attendre que quelqu'un d'autre vous le signale, effectuez vous-même une révision pour le découvrir.
Vous pouvez également laisser des commentaires sur votre propre pull request, de la même manière que vous pouvez laisser une description générale.
Par exemple, vous pouvez laisser des commentaires tels que :
- « _À l'origine, je voulais écrire X ici, mais..._ »
- « _Je ne suis pas sûr que ce soit le bon endroit pour cette méthode, car..._ »
- « _Je prévois de réécrire ce fichier la semaine prochaine pour la fonctionnalité Y_ »
Ces commentaires doivent être utilisés lorsqu'ils sont importants pour la relecture, mais pas pour les futurs responsables de la maintenance. Si quelque chose doit être laissé à l'intention des responsables de la maintenance, laissez-le plutôt sous forme de commentaire dans le code.

Obtenez des commentaires dès le début, tout comme vous souhaitez obtenir rapidement les commentaires des utilisateurs dans le cadre d'un développement agile.
Vous n'avez pas besoin d'attendre d'avoir entièrement mis en oeuvre une tâche pour obtenir des commentaires sur la conception ou les cas de test.
Il est tout à fait acceptable de demander à un collègue « _pouvez-vous jeter un oeil [à la conception / aux tests / ...] ?_ ».
En fait, des plateformes telles que GitHub ont un concept de pull requests « brouillons » ("_drafts_" en anglais) spécialement conçu à cet effet.
Une pull request brouillon comporte une indication spéciale et ne peut pas être fusionnée, ce qui indique qu'elle a été ouverte uniquement pour obtenir des commentaires.

Si nécessaire, vous pouvez également diviser votre pull request en plusieurs.
De la même manière que vous pouvez diviser une tâche avant de la commencer, si vous vous rendez compte après avoir terminé une partie de la tâche que la partie suivante est indépendante de la précédente, ouvrez une pull request pendant que vous travaillez sur la partie suivante.
De cette façon, votre code sera relu plus rapidement et vous risquerez moins d'entrer en conflit avec la branche principale lors de la fusion.

Enfin, acceptez le fait que vous recevrez parfois de mauvaises relectures de code et que vous devrez les traiter de manière professionnelle et constructive.
Tout le monde ne sait pas comment laisser une bonne revue, et certaines personnes veulent vous micromanager ou imposer leur opinion à tout le monde.
Répondez à leurs commentaires en leur rappelant les justifications communes, telles que « _Conformément aux conventions de l'équipe..._ », ou en faisant appel à quelqu'un d'autre pour vous aider, par exemple « _Demandons à X ce qu'il en pense_ ».
Si vous pensez que quelqu'un écrit des commentaires "mineurs" sans les signaler comme tels, demandez-lui si les corrections demandées par ce commentaire peuvent attendre. Il répondra probablement oui, puis oubliera qu'il vous a demandé de les faire.

---
#### Exercice

Effectuez une revue du code de cette [pull request](https://github.com/sweng-example/pr-example-turing/pull/2).
Qu'en pensez-vous ? Y a-t-il des bugs ? Quels commentaires laisseriez-vous ?

Regardez ensuite une [revue](https://github.com/sweng-example/pr-example-turing/pull/1) existante pour le même code.
Êtes-vous d'accord avec les commentaires ? En désaccord ? Certains commentaires manquent-ils ?

<details>
<summary>Exemple de solution (cliquez pour développer)</summary>
<p>

Le plus gros problème est que la fonctionnalité « recherche » ne comporte pas de tests, ce qui explique que les deux fautes de frappe dans son implémentation n'aient pas été repérées.

L'appel à `sorted` dans le Model est inutile puisque cette fonction retourne une nouvelle valeur, qui ici n'est pas utilisée, au lieu de modifier son entrée.

D'un point de vue architectural, il n'est pas très logique que le présentateur formate les listes en texte, car le format exact est spécifique à la vue.
De même, le présentateur ne devrait pas connaître le concept de « Ctrl+C » pour arrêter. Il pourrait peut-être plutôt traiter « exit » comme une commande, et la vue pourrait invoquer cette commande lorsque l'utilisateur exécute une fonction de sortie spécifique à la vue.

Il serait également utile de documenter le format JSON.

De nombreuses questions pourraient être discutées en équipe, telles que le besoin ou non de documentation par classe ou méthode.

</p>
</details>


## Comment collaborer en open source ?

Tout d'abord, que signifie exactement « open source » ?
La liberté d'utiliser le code source comme on le souhaite, par exemple pour le lire, l'utiliser, le partager, l'étudier...
Il ne s'agit pas d'une définition très précise, et il n'existe d'ailleurs aucune définition objective, mais [celle de l'Open Source Initiative](https://opensource.org/osd) est couramment utilisée.
Il est important de noter qu'elle exige une distribution gratuite, que cette distribution concerne le code source et non une version compilée ou obscurcie, que les travaux dérivés soient autorisés et qu'il n'y ait aucune discrimination quant à l'attribution des droits.
Notez que l'open source ne signifie pas que vous pouvez soumettre des correctifs et les faire fusionner. Un projet peut être open source même s'il n'accepte aucune contribution extérieure.

Les licences sont la version formelle de « qui peut faire quoi et sous quelles conditions ? ».
Elles précisent, en termes juridiques, ce que veulent les auteurs du code.
Il peut être tentant de penser que vous n'avez pas besoin de licence pour un code simple, mais c'est tout le contraire.
Sans licence, dans la plupart des juridictions, votre code sera par défaut protégé par le droit d'auteur, ce qui signifie que vous ne donnez à personne le droit de faire quoi que ce soit.
Les gens ne toucheront généralement pas à un code qui n'a pas de licence, car en théorie, vous pourriez les poursuivre en justice, par exemple pour l'avoir réutilisé.

Alors, comment choisir une licence ?
Vous pouvez consulter, par exemple, [le comparatif de Wikipédia](https://fr.wikipedia.org/wiki/Liste_de_licences_libres) des licences open source, mais cela vous prendra un certain temps.
Il existe des versions plus courtes, telles que [choosealicense.com](https://choosealicense.com/). Mais voici une version très courte et partiale :
- La licence **MIT** est destinée aux cas où vous souhaitez simplement que l'on vous crédite pour toute utilisation
- La licence **GPL** est destinée aux cas où vous souhaitez que toute utilisation soit également open source sous la licence GPL
- Les licences telles que « Unlicense » ou « WTFPL » sont destinées aux cas où vous souhaitez une forme de « domaine public », c'est-à-dire que n'importe qui peut utiliser votre code pour n'importe quoi sans condition

Maintenant que nous avons défini l'open source, à quoi ressemble un projet open source ?
En termes de hiérarchie, on trouve généralement :
- Les _mainteneurs_, qui ont un accès en écriture au code et le dernier mot sur les décisions relatives au projet
- Les _contributeurs_, qui soumettent du code et des idées, mais dont les pull requests et les suggestions doivent être approuvées par les mainteneurs
- Les _utilisateurs_, qui ne contribuent pas au code

Les gens maintiennent des projets open source pour le plaisir, pour le travail et, très rarement, pour l'argent.
Par exemple, si vous consultez [la page des mainteneurs du noyau Linux](https://docs.kernel.org/process/maintainers.html), vous verrez que la plupart des composants du noyau ont quelqu'un qui s'en occupe, et que certains d'entre eux sont même rémunérés pour le faire.
En général, cela signifie qu'une entreprise qui utilise le noyau a décidé d'affecter un ingénieur à cette tâche, au moins à temps partiel.
Certains projets largement utilisés, tels que `curl`, ont même des [sponsors](https://curl.se/sponsors.html).
Certains projets commerciaux sont, pour diverses raisons, open source, comme [les compilateurs C# et Visual Basic .NET](https://github.com/dotnet/roslyn/).

Comment gravir les échelons et passer du statut d'« utilisateur » à celui de « contributeur » d'un projet qui vous plaît et auquel vous souhaitez apporter votre aide ?
En bref :
1. Trouvez une "issue"
2. Lisez les directives de contribution du projet
3. Travaillez sur le problème localement
4. Ouvrez une demande d'extraction

Pour trouver une "issue", recherchez de grands projets qui ont étiqueté des problèmes avec des labels tels que « bonne première issue » ("_good first issue_") ou « aide recherchée » ("_help wanted_"), comme [celui-ci](https://github.com/microsoft/terminal/issues/12632), et communiquez votre intention de travailler dessus aux mainteneurs.
Vous pouvez également ouvrir votre propre problème, par exemple [traduire l'interface utilisateur dans votre langue](https://github.com/microsoft/terminal/issues/19530).

Ces exemples sont tirés du dépôt `microsoft/terminal`, qui contient un [guide de contribution](https://github.com/microsoft/terminal/blob/main/CONTRIBUTING.md) expliquant le type de contributions acceptées, par où commencer, etc.

Avant que votre pull request ne soit examinée, vous devrez généralement signer un « Contribution License Agreement », ou « CLA » en abrégé.
Il s'agit d'un document qui donne effectivement aux responsables la propriété du code spécifique que vous avez soumis, de sorte que si, à l'avenir, ils ont besoin, par exemple, de modifier la licence du projet,
ils n'ont pas à rechercher les centaines de contributeurs passés qui ont soumis du code qui a été intégré dans le projet.

Enfin, n'oubliez pas que si vous contribuez à un projet open source, vous rejoignez une équipe avec des pratiques établies.
Ne commencez pas votre pull request en effectuant des refactorisations aléatoires pour l'adapter à votre idée de ce que devrait être la base de code.
Ne divisez pas un fichier en plusieurs fichiers simplement parce que vous préférez une certaine structure de code.
Ce type de comportement provoque beaucoup de frictions, rend votre code beaucoup plus difficile à réviser et peut entraîner le rejet de votre pull request sans révision appropriée.
Évitez également d'ouvrir de grandes pull requests sans avertissement, car la plupart des mainteneurs ne sont pas intéressés par la révision de milliers de lignes de code pour une fonctionnalité qu'ils n'ont pas explicitement demandée.

---

#### Exercice

Contribuez à un projet open source !

Vous pouvez par exemple trouver des projets avec le label « good first issue » ici, en filtrant par langage de programmation si nécessaire : <https://github.com/topics/good-first-issue>

Trouvez un sujet qui vous intéresse, planifiez votre travail et contribuez !

---


## Résumé

Dans ce cours, vous avez appris :
- Travail en équipe : éviter la friction, revues de code
- Méthodes de développement : Waterfall, Scrum, agilité
- Open source : Structure, licences, contributions
