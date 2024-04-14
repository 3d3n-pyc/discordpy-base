## Discord.py base
### Description
Ce projet est un bot Discord écrit en Python. Il utilise la bibliothèque discord.py pour interagir avec l'API Discord. Le bot est capable de charger des plugins, de gérer les dépendances des plugins, de synchroniser les commandes à Discord.

### Installation
- Clonez ce dépôt sur votre machine locale.
- Installez les dépendances nécessaires en utilisant pip: `python -m pip install -r requirements.txt`
- Configurer le bot Discord à partir du fichier `config.json`
- Exécutez le bot: `python main.py`

### Utilisation
Pour ajouter un nouveau plugin, créez un dossier dans le répertoire plugins/ avec le nom de votre plugin. Dans ce dossier, créez un fichier plugin.yml qui contient les informations sur le plugin et ses dépendances. Le bot chargera automatiquement le plugin lors de son démarrage.

### Licence
Ce projet est sous licence `GNU-3.0`. Voir le fichier [LICENSE](/LICENSE) pour plus de détails
