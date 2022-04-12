# Mini-projet de Python-Django - IPYT011
## Avant-propos et conseils de réalisation
L'objectif est de réaliser une application Web qui réponde à un besoin identifier dans le cahier des charges. Le travail est à réaliser durant les séances de IPYT011 prévues à cet effet.
Le travail est à réaliser en groupe et déposer dans la boîte prévue à cet effet le mardi 12 avril 2022 à 16h30.
Veillez à bien réaliser votre projet en suivant une méthode de développement qui permettent d'analyser le cahier des charger, de concevoir l'application, de l'implémenter sous Django et de la tester. 
Pensez à prendre des notes et à rédiger votre rapport de réalisation et votre présentation au fur et à mesure du développement.
## Cahier des charges
### Contexte métier
Une entreprise a besoin d'une application permettant au personnel de suivre un tableau de tâches à réaliser dans le cadre d'un projet. L'objectif est que l'application soit capable de proposer une organisation de tâches la plus efficace en fonction de plusieurs facteurs qui permettront de les prioriser, répartir entre les membres des équipes de développement et les ordonnancer dans le temps.
Un processus de validation des tâches au fur et à mesure de leur statut (planifiée, en cours, réalisée, en pause, validée) permettra aux différent·es responsables d'évaluer l'état d'avancement du projet au regard d'une date de livraison imposée.
Ces responsables de projet auront la possibilité d'avancer ou de reculer la date de livraison et choisissant d'éliminer ou d'ajouter des tâches ou en réduisant ou augmentant le temps de réalisation planifié.
Les responsables sont également chargés de valider une tâche une fois celle-ci réalisée. 
Les personnes en charge de tâches doivent faire à rapport quotidien de l'état d'avancement d'une tâche en remplissant un formulaire. Une ou plusieurs personnes peuvent être en charge de la réalisation mais une seule est chargée du rapport sur l'état d'avancement mesuré en pourcentage.
Les personnels, exécutant les tâches ou responsables, peuvent 
•	prendre des congés,
•	tomber malades,
•	arriver en cours de projet,
•	partir en cours de projet,
•	changer de tâches en cours de réalisation.
 
### Tâches
Une tâche est associée à un projet, à une ou plusieurs personnes exécutant·es dont une chargée de l'état d'avancement. Elle dispose d'une description, d'une priorité (sur 3 niveaux), d'une date de démarrage, d'une durée en jours, d'un statut, d'un état d'avancement.  Elle peut aussi être associée à une ou plusieurs tâches précédentes nécessaires à sa réalisation.
Toutes les tâches dont les informations nécessaires à sa planification sont manquantes sont par défaut en pause.
Chaque tâche peut-être également associée à des sous-tâches qui la compose et/ou à une et une seule super-tâche dont elle est composante.
Projets
Un projet est associé à plusieurs tâches qui sont nécessaire à sa réalisation ainsi qu'à un·e responsable.
Il dispose d'une date de livraison, qui est fixée par le ou la responsable et d'une date de démarrage, qui correspond à celle de la première tâche planifiée.
Il dispose également d'un statut (en pause, planifié, en cours, livré). Un projet dont l'ensemble des tâches n'ont pas été planifiés est en pause, un projet en cours a été planifié et la date de démarrage de la première tâche planifiée a été passée. Un projet dont l'ensemble des tâches est en pause est en pause également. Un projet est livré si l'ensemble des tâches ont été validées et réalisées.
Il dispose enfin d'un état d'avancement en pourcentage dont le calcul sera laissé à appréciation.
### Diagramme de GANT automatisé (Bonus)
L'application sera capable de générer un diagramme de GANT automatiquement une fois l'ensemble des tâches d'un projet renseignées. 
Réalisation et évaluation
L'application devra permettre à l'ensemble de ses acteurs d'interagir avec elles en suivant le cahier des charges proposé. Vous réaliserez l'ensemble des pages web nécessaires selon vous à suivre le cahier des charges. 
L'ensemble du code source du projet devra être livré le jour de la présentation sous la forme d'une archive zippé.
Un rapport comprenant l'analyse du cahier des charges, la conception et les réalisations les plus significatives dans l'application devra être livré le même jour.
L'apparence de l'application ne sera pas évaluée. Le code HTML, CSS et Javascript doit être le plus succinct possible.





___

## Environnement virtuel

Un environnement virtuel permet d'avoir sur notre projet un environnement indépendant du Python installé de manière globale.

Un **environnement virtuel** permet d'avoir par ailleurs l'ensemble des librairies en local (sur le projet) plutôt qu'en global.
Cela permet tout simplement d'être sur les mêmes versions qu'importe ou le code sera exécuté.

> Par ailleurs, pour pouvoir effectuer cela, il faut que l'ensemble des librairies qui seront installés doivent êtres installés à l'intérieur de votre environnement virtuel.

Pour commencer, il faut déjà créer notre environnement virtuel. Et pour pouvoir faire cela on exécute la commande suivante :

```bash
python<version> -m venv env
```

Il est aussi possible d'utiliser la commande suivante :

```bash
virtualenv -p python<version> env
```

Si celle-ci ne fonctionne pas alors installé `virtualenv` grâce au gestionnaire de package `pip` grâce à la commande suivante : **`pip install virtualenv`**.

> Le nom de dossier **env** n'est pas obligatoire, il permet d'avoir un dossier avec l'intégralité de l'environnement a utilisé. Mais par habitude celui-ci s'appelle ainsi.

Une fois votre environnement virtuel créer, il ne vous reste plus qu'à l'activer. Pour pouvoir l'activer il suffit juste de vous mettre à la racine de votre projet et d'entrer la ligne de commande suivante :

```bash
source env/bin/activate
```

Une fois activé, il ne reste plus qu'à entrer la commande suivante pour savoir ou se trouve la version de Python que l'on exécute :

```bash
which python
```

> Sur certain terminal, il est affiché dans le prompt que votre environnement virtuel est activé.

Pour désactiver l'environnement virtuel, on peut utiliser la commande suivante :

```bash
deactivate
```

Pour en savoir plus sur l'utilisation de l'environnement virtuel avec Python, rendez-vous sur cette [page](https://python.doctor/page-virtualenv-python-environnement-virtuel).

## Sauvegarder les dépendances

Pour pouvoir sauvegarder les librairies installées, on va utiliser la commande `pip`. 

> Les librairies doivent être installés au sein de l'environnement virtuel pour éviter d'avoir d'autres librairies installés en global sur le PC.

```bash
pip freeze > requirements.txt
```

Par la suite, on peut réinstaller l'ensemble des librairies avec `pip` :

```bash
pip install -r requirements.txt
```