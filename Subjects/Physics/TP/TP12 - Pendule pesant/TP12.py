"""Exécuter les cellules les unes après les autres après les avoir complétées
en cliquant sur Run puis Execute Cell ou CTRL + Entrée
Pour exécuter l'ensemble du fichier : CTRL + E
"""
# Période du pendule pesant

## Cellule 1 :Importation des bibliothèques utiles
import numpy as np                  # pour la manipulation des tableaux
import matplotlib.pyplot as plt     # pour les représentations graphiques
import scipy.integrate as sci       # pour les calculs d'intégrales
from math import *

## Cellule 2: Vérification de la formule de Borda
tab_theta0_exp = np.array(['à compléter'])   # Tableau des theta0 en degrés
tab_T_exp = np.array(['à compléter'])   # Tableau des périodes T en secondes
x = 'à compléter'   # Tableau des abscisses
y = 'à compléter'   # Tableau des ordonnées
"""
p = np.polyfit(x, y, n)
Modélise la courbe y = f(x) par un polynôme de degré n
Arguments:
    x : tableau des abscisses
    y : tableau des ordonnées
    n : degré du polynôme (pour n = 1 : régression linéaire)
Renvoie:
    p : tableau des coefficients du polynôme tel que :
    p[0] : coefficient de degré n, p[1] : coefficient de degré n-1...
    p[n] : coefficient de degré 0
"""
p = 'à compléter'  # Tableau des coefficients de la régression linéaire de y en fonction de x
ymodele = 'à compléter'  # Equation de la régression linéaire ymodele en fonction de x

plt.figure(figsize = (12,8))
plt.plot('à compléter', label="Points expérimentaux") # Tracé des points expérimentaux avec des ronds bleus
plt.plot('à compléter', label="Régression linéaire") # Tracé de la régression linéaire en trait rouge
plt.xlabel(r"$\theta _0 ^2$ (en rad$^2$)")
plt.ylabel(r"$T$ (en s)")
plt.title('Vérification expérimentale de la formule de Borda')
plt.grid()
plt.legend(loc = 'upper left')
plt.show()

# Affichage des coefficients de la formule de Borda
print(f'Pente : a = {p[0]:.2e} s')
print(f'Pente théorique : T0/16 = {p[1]/16:.2e} s')
print(f"Ordonnée à l'origine : b = T0 = {p[1]:.2f} s")

## Cellule 3: Calculs de la période pour une valeur de theta0
T0 = 'à compléter'          # Période propre en seconde
theta0 = 'à compléter'     # Amplitude en radian
# Expression analytique
def periode(theta0):
    def diff(theta):
        return 'à compléter' # Expression à intégrer
    return sci.quad(diff,0,theta0)[0] # Renvoie l'intégrale entre 0 et theta0 de la fonction diff(theta)

# Formule de Borda
def Borda(theta0):
    return 'à compléter'
print(f'Pour theta0 = {theta0 * 180 / pi:.0f} deg')
print(f'Expression analytique : T = {periode(theta0):.2f} s')
print(f'Formule de Borda : T = {Borda(theta0):.2f} s')

## Cellule 4: Calculs et tracés de la période pour N valeurs de theta0
N = 50      #Nombre d'amplitudes theta0
tab_theta0 = np.array([i*pi/N for i in range(1,N)]) # Tableau de N valeurs de theta0 en radian
tab_T = np.vectorize(periode)(tab_theta0) # Tableau de N valeurs de périodes calculées avec l'expression analytique

# Tracés de la période T en fonction de theta0
theta0_deg = 'à compléter' # Abscisse correspondant à theta0 en degré

plt.figure(figsize = (12,8))
plt.plot([0.,180.], [T0,T0], 'b:', label="Période propre") # Tracé de la période propre avec des pointillés bleus
plt.plot('à compléter') # Tracé de la période calculée avec l'expression analytique en trait rouge, en fonction de theta0
plt.plot(t'à compléter') # Tracé de la période calculée avec la formule de Borda en tirets noirs, en fonction de theta0
plt.xlabel(r"$\theta _0$ (en deg)")
plt.ylabel(r"$T$ (en s)")
plt.title("Période du pendule pesant en fonction de l'amplitude")
plt.grid()
plt.legend(loc = 'upper left')
plt.show()


