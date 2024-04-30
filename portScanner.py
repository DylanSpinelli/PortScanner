import socket # permet de créer des connexions grace aux IP et aux ports
import subprocess # permet de rentrer des commandes systèmes
import sys # permet d'effectuer des opérations système
from datetime import datetime # permet de créer et manipuler des objets de dates et heures

subprocess.call('clear', shell=True) # efface les précédentes commandes

remoteServerIP = input('Entrer l\'IP d\'un serveur à scanner : ') # récupère l'IP a scanner

print('-' * 60)
print('Lancement du scan des ports de la machine ' + remoteServerIP)
print('-' * 60)

t1 = datetime.now() # commence a mesurer le temps au lancement du programme

try: # exécute le bloc de code suivant sauf si des exceptions se produisent (except)
  for port in range(1, 1025): # on peut analyser 1024 ports
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET : IPv4, SOCK_STREAM : TCP
    sock.settimeout(1)
    result = sock.connect_ex((remoteServerIP, port)) # se connecte grace a l'IP et au port, renvoie 0 si la connexion est réussie
    if result == 0: # si le port est ouvert
      print('Port {}:   Ouvert'.format(port)) # on indique que le port est ouvert
    sock.close()

except KeyboardInterrupt: # exception : Ctrl+C
  print('Vous avez appuyé sur Ctrl+C.')
  sys.exit()

except socket.error: # exception : problème de connexion au serveur
  print('Impossible de se connecter au serveur.')
  sys.exit()

t2 = datetime.now() # mesure le temps a la fin du programme

total = t2 - t1 # calcule le temps d'exécution du programme

print('Scan complété en : {}'.format(str(total))) # affiche le temps d'exécution