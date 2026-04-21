# Scanner de Ports TCP en Python

Un outil en ligne de commande (CLI) développé en Python pour vérifier l'état des ports réseau d'une machine cible. 
Ce projet a été construit de manière itérative afin de comprendre en profondeur le fonctionnement des sockets réseau, du protocole TCP et de l'optimisation des performances en Python.

##  Évolution et Fonctionnalités

Ce projet a été développé en 3 phases distinctes :

* **Phase 1 : Sockets Basiques** * Création du noyau de connexion TCP utilisant le module `socket`.
  * Utilisation de `connect_ex` pour éviter les plantages lors de la détection de ports fermés.
  * Ciblage spécifique de ports critiques (FTP, SSH, HTTP/S, MySQL, services Windows).

* **Phase 2 : Interface CLI et Robustesse**
  * Implémentation du module `argparse` pour rendre l'adresse IP et les ports dynamiques.
  * Ajout de la gestion d'exceptions (`try...except`) pour prévenir les erreurs de saisie utilisateur et éviter les crashs inattendus.
  * Menu d'aide auto-généré (`-h`).

* **Phase 3 : Accélération par Multithreading**
  * Remplacement du scan séquentiel (très lent) par un scan asynchrone.
  * Utilisation de `concurrent.futures.ThreadPoolExecutor` pour déployer jusqu'à 50 *workers* simultanés, réduisant drastiquement le temps d'exécution.

##  Comment l'utiliser

Assurez-vous d'avoir Python installé sur votre machine. Aucune bibliothèque externe n'est requise.

**1. Afficher le menu d'aide :**
```bash
python port_scanner.py -h
