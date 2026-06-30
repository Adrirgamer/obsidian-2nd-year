"""Exécuter les cellules les unes après les autres après les avoir complétées
en cliquant sur Run puis Execute Cell (ou CTRL + Entrée)
Pour exécuter l'ensemble du fichier : CTRL + E
"""
# Simulation Monte-Carlo pour déterminer l'incertitude-type d'une grandeur composée

## Importation des bibliothèques
from matplotlib import pyplot as plt  # pour les représentations graphiques
import numpy as np                    # pour la manipulation des tableaux
import numpy.random as rd             # pour la génération de tirages aléatoires

## Données expérimentales

# Mesure de la distance D
D =        # Valeur mesurée en USI
u_D =      # Incertitude-type sur D en USI

# Mesure de la période T
T =         # Valeur mesurée en USI
u_T =       # Incertitude-type sur T en USI

## Tirages aléatoires : simulation de Monte Carlo (MC)

N = 100000           # Nombre de tirages
MC_D = D + u_D*np.sqrt(3)*rd.uniform(-1,1,N) # Tirage aléatoire de N valeurs de D avec une distribution uniforme
MC_T =       # Tirage aléatoire de N valeurs de T avec une distribution uniforme : à compléter
MC_c =       # Expression de la célérité c : à compléter

# Tracé histogramme
plt.hist(MC_c,bins='rice')
plt.xlabel('c (m/s)')
plt.ylabel('Effectifs')
plt.title('Histogramme des célérités')
plt.show()

# Etude statistique : valeur moyenne et incertitude-type sur la célérité c
c_moy =          # Valeur moyenne des N valeurs simulées de c = meilleur estimateur de la mesure (unique) : à compléter
u_c =           # Incertitude-type sur c : à compléter

# Affichage des résultats
print('\n')
print("Évaluation de l'incertitude-type avec une simulation de Monte-Carlo" )
print(f'Valeur moyenne : c = {c_moy:.2f} m/s')
print(f'Incertitude-type : u(c) = {u_c:.2f} m/s')


