import socket
import argparse

def etat_port(hote, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        resultat = sock.connect_ex((hote, port))
        sock.close()
        return resultat == 0
    except socket.gaierror:
        print("[!] Erreur : Adresse IP invalide")# Erreur si l'adresse IP ou le nom de domaine est invalide
        exit()
    except Exception as e:
        print(f"[!] Erreur : {e}")# Capture toute autre erreur réseau
        return False


# NOUVEAU: Fonction dédiée à la configuration du terminal:)
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


# Bloc principal:)
if __name__ == "__main__":
    # On lit ce que l'utilisateur a tapé dans le terminal
    args = configurer_arguments()
    ip_cible = args.target

    # Le terminal envoie les ports sous forme String ("22,21").
    #=> On doit le transformer en une liste de nombres entiers [22, 21] pour fonction.
    str_ports = args.ports.split(",")  # On coupe le texte à chaque virgule
    try:
        liste_ports = [int(p.strip()) for p in str_ports]  # On convertit chaque morceau en chiffre (int)
    except ValueError:
        print("[!] Erreur : Format des ports invalide")
        exit()

    print(f"[:)] Lancement du scan sur l'hôte : {ip_cible}")
    print(f"[:)] Ports à vérifier : {liste_ports}\n")

    au_moins_1_ouvert = False

    #boucle de check :)
    for port in liste_ports:
        check = etat_port(ip_cible, port)
        if check:
            print(f"[#_#] Le port {port:4} est : OUVERT")
            au_moins_1_ouvert = True  # Correction de la variable ici !

    if not au_moins_1_ouvert:
        print("waaaaalo (Aucun port ouvert trouvé)")