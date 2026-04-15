:) Scanner de Ports TCP (Version Basique) :)

Un script Python simple pour vérifier l'état de ports spécifiques sur une machine locale. Ce projet est construit de manière itérative pour comprendre le fonctionnement des sockets réseau et du protocole TCP.

______Fonctionnalités actuelles______

Dans cette version initiale, le script utilise le module `socket` pour tenter d'établir une connexion TCP (`connect_ex`) sur la machine locale (`127.0.0.1`). 

Il cible spécifiquement une liste de ports critiques ou couramment utilisés :
- 21 (FTP)
- 22 (SSH)
- 80 / 8080 (HTTP)
- 443 (HTTPS)
- 135 / 445** (Services Windows)
- 3306 (MySQL)

Si aucun de ces ports n'est ouvert, le script affiche un message personnalisé pour le signaler.

________Comment le lancer___________

Assurez-vous d'avoir Python installé, puis lancez simplement la commande dans votre terminal :
```bash
python check_ports.py

__________Prochaine Étape : Rendre l'outil dynamique (CLI)_______________

Actuellement, l'adresse IP (127.0.0.1) et la liste des ports sont "codées en dur" directement dans le fichier Python.
L'objectif de la prochaine phase est d'intégrer des arguments en ligne de commande. Cela permettra de cibler n'importe quelle adresse IP sans avoir à modifier le code source, par exemple : python scanner.py -t 192.168.1.1.
