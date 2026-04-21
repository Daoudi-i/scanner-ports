import socket
import argparse
import sys     #interagir avec le système (ex: quitter le programme)
import concurrent.futures  # NOUVEAU : La bibliothèque pour le multithreading

# Fonction qui vérifie l'état d'un port donné sur un hôte
def etat_port(hote, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)      # Définir un timeout de 1 seconde
    resultat = sock.connect_ex((hote, port))
    sock.close()

    if resultat == 0:
        print(f"Le port' {port:4}'est : OUVERT")
        return True
    return False

def configurer_arguments():
    # On crée l'objet qui va lire le terminal
    parser = argparse.ArgumentParser(description="Scanner de Ports TCP Dynamique")

    # !!OBLIGATOIRE : L'adresse IP (-t ou --target)
    parser.add_argument("-t", "--target", required=True, help="Adresse IP de la machine cible (ex: 127.0.0.1)")
    df_ports="21,22,80,135,443,445,631,3306,8080";  #ports usuel
    # Argument OPTIONNEL : Les ports (-p ou --ports). Si l'utilisateur ne met rien, on utilise ta liste par défaut !
    parser.add_argument("-p", "--ports", default=df_ports,
                        help="Ports à scanner séparés par des virgules (ex: 22,80,443)")

    return parser.parse_args()


if __name__ == "__main__":
    args = configurer_arguments()  # Récupérer les arguments fournis par user
    ip_cible = args.target

    # Gestion des erreurs de saisie
    try:
        str_ports = args.ports.split(",")
        liste_ports = [int(p.strip()) for p in str_ports]
    except ValueError:
        print("[-] ERREUR : Le format des ports est invalide. Utilisez des chiffres.")
        sys.exit()   #quiter

    print(f"[*] Lancement du scan sur l'hôte : {ip_cible}")
    print(f"[*] Ports à vérifier : {len(liste_ports)} port(s)\n")

    au_moins_1_ouvert = False


    # NOUVEAU : On crée une petite fonction "ouvrier" qui sait quelle IP attaquer
    def worker(port):
        return etat_port(ip_cible, port)


    # NOUVEAU : Le gestionnaire de Threads (multithreading)
    try:
        # On embauche 50 ouvriers virtuels (max_workers=50) /  # Création d'un pool de 50 threads
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            # On leur donne la liste des ports à vérifier tous en même temps
            resultats = executor.map(worker, liste_ports)

            # Si au moins un résultat est "True" (ouvert), on retient l'info
            if any(resultats):
                au_moins_1_ouvert = True

    except KeyboardInterrupt:  # NOUVEAU : Gestion propre si l'utilisateur fait Ctrl+C
        print("\n[!] Scan annulé par l'utilisateur.")
        sys.exit()    # Quitter le programme

    if not au_moins_1_ouvert:
        print("waaaaalo (Aucun port ouvert trouvé)")
