# Simulation Monte-Carlo pour déterminer l'incertitude-type d'une grandeur composée :
# le grossissement d'une lunette afocale

# Exécuter les cellules les unes après les autres après les avoir complétées
# en cliquant sur Run puis Execute Cell (ou CTRL + Entrée)

## Cellule 1 : Importation des bibliothèques
from matplotlib import pyplot as plt  # pour les représentations graphiques
from math import *
import numpy as np                    # pour la manipulation des tableaux
import numpy.random as rd             # pour la génération de tirages aléatoires

## Cellule 2 : Détermination de l'angle alpha et de son incertitude-type (à compléter)
# Grandeurs mesurées (mesures uniques)
AB =                 # Taille de l'objet mesurée en cm
fprim0 =             # Distance focale mesurée en cm

# Incertitudes-type associées (à partir de plages de valeurs)
u_AB =             # Incertitude-type associée à l'objet AB en cm
u_fprim0 =         # Incertitude-type associée à f_prim0 en cm

# Tirages aléatoires : simulation de Monte Carlo (MC)
N = 100000        # Nombre de tirages
MC_AB = AB + u_AB*sqrt(3)*rd.uniform(-1,1,N)
MC_fprim0 = fprim0 + u_fprim0*sqrt(3)*rd.uniform(-1,1,N)

# Calcul de la grandeur recherchée : angle alpha
MC_alpha =              # Expression à compléter

# Tracé histogramme
plt.figure(1)
plt.hist(MC_alpha,bins='rice')
plt.xlabel('alpha (rad)')
plt.ylabel('Effectifs')
plt.show()

# Etude statistique : valeur moyenne et incertitude-type
alpha = np.mean(MC_alpha)           # Valeur moyenne des N valeurs simulées de alpha = meilleur
                                    # estimateur de la mesure (unique)
u_alpha = np.std(MC_alpha,ddof=1)   # Incertitude-type sur alpha

# Affichage des résultats
print('Étude statistique après une simulation de Monte Carlo')
print(f'Valeur : alpha = {alpha:.4f} rad')   # Formatage de l'affichage avec 4 décimales
print(f'Incertitude-type : u(alpha) = {u_alpha:.4f} rad \n')

## Cellule 3 : Détermination de l'angle alpha_prim et de son incertitude-type (à compléter)
# Grandeurs mesurées (mesures uniques)
AB_prim =            # Taille de l'image mesurée en cm
fprim3 =             # Distance focale mesurée en cm

# Incertitudes-type associées (à partir de plages de valeurs)
u_AB_prim =          # Incertitude-type associée à l'objet AB en cm
u_fprim3 =           # Incertitude-type associée à f_prim0 en cm

# Tirages aléatoires : simulation de Monte Carlo (MC) pour N = 100000
MC_AB_prim = AB_prim + u_AB_prim*sqrt(3)*rd.uniform(-1,1,N)
MC_fprim3 = fprim3 + u_fprim3*sqrt(3)*rd.uniform(-1,1,N)

# Calcul de la grandeur recherchée : angle alpha_prim
MC_alpha_prim =           # Expression à compléter

# Tracé histogramme
plt.figure(2)
plt.hist(MC_alpha_prim,bins='rice')
plt.xlabel('alpha_prim (rad)')
plt.ylabel('Effectifs')
plt.show()

# Etude statistique : valeur moyenne et incertitude-type
alpha_prim = np.mean(MC_alpha_prim)  # Valeur moyenne des N valeurs simulées de alpha_prim
u_alpha_prim = np.std(MC_alpha_prim,ddof=1)   # Incertitude-type sur alpha_prim

# Affichage des résultats
print('Étude statistique après une simulation de Monte Carlo')
print(f'Valeur : alpha_prim = {alpha_prim:.4f} rad')   # Formatage de l'affichage avec 4 décimales
print(f'Incertitude-type : u(alpha_prim) = {u_alpha_prim:.4f} rad \n')

## Cellule 4 : Grossissement de la lunette afocale (à compléter)
# Calcul de G par tirages aléatoires : Monte Carlo
MC_G =              # Expression à compléter

# Tracé histogramme : à compléter






# Etude statistique : valeur moyenne et incertitude-type sur le grossissement G : à compléter
G =         # Valeur moyenne des N valeurs simulées de G
u_G =     # Incertitude-type sur G
print('Étude statistique')
                                # Affichage de G avec 4 décimales
                                # Affichage de u_G avec 4 décimales
                                # Saut de ligne

## Cellule 5 : Grossissement à partir des distances focales (à compléter)
# Lentille objectif
f1 =           # Valeur mesurée en cm
u_f1 =         # Incertitude-type en cm

# Lentille oculaire
f2 =           # Valeur mesurée en cm
u_f2 =         # Incertitude-type en cm

# Tirages aléatoires : Monte Carlo
MC_f1 =          # Expression à compléter
MC_f2 =          # Expression à compléter

# Grossissement G1 = Rapport des distances focales de la lunette
MC_G1 =          # Expression à compléter

# Etude statistique : valeur moyenne et incertitude-type sur le grossissement G1
G1 = np.mean(MC_G1)       # Valeur moyenne des N valeurs simulées de G1
u_G1 = np.std(MC_G1,ddof=1)   # Incertitude-type sur G1
print('Étude statistique')
print(f'Valeur moyenne : G1 = {G1:.4f}')
print(f'Incertitude-type : u(G1) = {u_G1:.4f}')
print('\n')

## Cellule 6 : Ecart normalisé ou z-score (à compléter)
z =                              # Expression à compléter
                                 # Affichage de z avec 4 décimales