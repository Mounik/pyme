import signal
import os
import time

def alarme(signal, contaxte):
    print("Réception du signal no %s " % signal )
    raise OSError("ALARME !!!")

MAX_TIME = 5 # en secondes

signal.signal(signal.SIGALRM, alarme)
signal.alarm(MAX_TIME)

print("Début du temps d'attente ...")
try:
    time.sleep(15)  # Ici le traitement qui ne doit pas exceder
                    # MAX_TIME
except:
    pass            # Ici l'interruption de l'erreur
                    # Mais aussi de l'alarme

# sinon on continue
print("Fin du temps d'attente ...")

signal.alarm(0)
