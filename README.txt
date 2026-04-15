                 ####Scanner de Ports TCP (Version CLI Dynamique)####

Ce projet est un scanner de ports TCP développé en Python. Cette deuxième étape de développement transforme le script basique en un véritable outil en ligne de commande (CLI) professionnel, interactif et robuste.

#:)Nouveautés de la Phase 2
  Fini le "codage en dur" ! L'outil utilise désormais la bibliothèque standard `argparse` pour interagir dynamiquement avec l'utilisateur via le terminal.

  Cible dynamique :Possibilité de spécifier n'importe quelle adresse IP ou nom de domaine à scanner via l'argument `-t`.
  Ports personnalisables :Choix d'une liste de ports spécifiques via l'argument `-p`, ou utilisation d'une liste de ports critiques par défaut si l'argument est omis.
  Menu d'aide automatisé :Génération automatique d'un manuel d'utilisation intégré accessible via l'argument `-h`.
  Robustesse (Exceptions) :Intégration de blocs `try...except` pour gérer proprement les erreurs de saisie (ex: taper des lettres au lieu de numéros de ports) sans faire planter le script de manière brutale.

#:)Comment utiliser l'outil

 Afficher le menu d'aide complet :

>>python scanner.py -h