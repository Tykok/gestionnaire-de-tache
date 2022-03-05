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