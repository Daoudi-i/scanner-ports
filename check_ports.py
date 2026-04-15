import socket


def etat_port(hote, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)     #force l'arrêt de la tentative de connexion après 1 sec
    resultat = sock.connect_ex((hote, port))    #on a eviter utiliser .connect car il renvoie une erreur si le port est ferme
    sock.close()      #fermer le socket
    return resultat == 0     #si le port est ouvert il renvoie 1

#bloc principal
if __name__ == "__main__":
    # on test avec les ports classiques (Web, FTP, SSH, Windows, Bases de données)
    sos = [21, 22, 80, 135, 443, 445, 631, 3306, 8080]

    #savoir si on a trouvé au moins un port ouvert
    au_moins_1_ouvert = False

    for port in sos:
        check = etat_port("127.0.0.1", port) #127.0.0.1 address de notre localhost
        if check:
            print(f"Le port {port} est : ouvert")
            au_moins_1_ouvert = True  # On retient qu'on a trouvé un port

    # Si la variable est toujours fausse à la fin de la boucle => tous les ports est ferme
    if not au_moins_1_ouvert:
        print("waaaaalo")