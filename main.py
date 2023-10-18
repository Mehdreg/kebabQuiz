import time

# États des buzzers
BUZZER1_ACTIVATED = False
BUZZER2_ACTIVATED = False

# États des LEDs
LED1_ON = False
LED2_ON = False

# Fonction pour changer la couleur des LEDs
def change_color():
    global LED1_ON, LED2_ON
    LED1_ON, LED2_ON = not LED1_ON, not LED2_ON
    print("Changement de couleur des LEDs.")

try:
    print("Attente d'une activation des buzzers...")
    while True:
        # Simulation de l'activation des buzzers (remplacez cela par votre logique d'activation)
        BUZZER1_ACTIVATED = input("Buzzer 1 activé ? (oui/non) ").lower() == 'oui'
        BUZZER2_ACTIVATED = input("Buzzer 2 activé ? (oui/non) ").lower() == 'oui'

        # Vérification des buzzers et changement de couleur des LEDs
        if BUZZER1_ACTIVATED or BUZZER2_ACTIVATED:
            change_color()
        time.sleep(1)  # Attente d'une seconde avant de vérifier à nouveau les buzzers

except KeyboardInterrupt:
    print("Arrêt du programme.")