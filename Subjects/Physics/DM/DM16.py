"""Exécuter les cellules les unes après les autres après les avoir complétées
en cliquant sur Run puis Execute Cell (ou CTRL + Entrée)
Pour exécuter l'ensemble du fichier : CTRL + E
"""
# 3ème loi de Kepler

## Cellule 1 :Importation des bibliothèques utiles
import numpy as np                  # pour la manipulation des tableaux
import matplotlib.pyplot as plt     # pour les représentations graphiques

## Cellule 2: Vérification de la 3ème loi de Kepler
tabT = np.array(['à compléter'])    # Tableau des périodes T en secondes!
taba = np.array(['à compléter'])    # Tableau des demi-grand axes a en mètres!
x = 'à compléter'               # Tableau des abscisses a^3
y = 'à compléter'               # Tableau des ordonnées T^2
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
p = 'à compléter'    # Tableau des coefficients de la régression linéaire de y en fonction de x
ymodele = 'à compléter'    # Equation de la régression linéaire ymodele en fonction de x

plt.figure(figsize = (16,9))
plt.plot(x, y, 'bo', label="Points expérimentaux") # Tracé des points expérimentaux avec des ronds bleus
plt.plot('à compléter') # Tracé de la régression linéaire en trait rouge
plt.xlabel(r"$a^3$ (en m$^3$)")
plt.ylabel(r"$T^2$ (en s$^2$)")
plt.grid()
plt.legend(loc = 'upper left')
plt.show()

## Cellule 3 : Masse du trou noir
tabK = 'à compléter'        # Tableau des valeurs T^2 / a^3
K = np.mean(tabK)             #Valeur moyenne
sK = np.std(tabK,ddof=1)      #Ecart-type expérimental
uK = 'à compléter'  #Incertitude-type

G = 'à compléter' # Constante de gravitation
M = 'à compléter'   # Expression de la masse M
uM ='à compléter'          # Expression de l'incertitude-type uM
print(f"Masse du trou noir : M = {M:.4e}  kg") #Affichage de la masse du trou noir
print(f"Incertitude-type : u(M) = {uM:.2e} kg ") #Affichage de l'incertitude-type

## Cellule 4 : Ecart normalisé
'à compléter'

EN = 'à compléter' #Calcul de l'écart normalisé
print(f"Ecart normalisé : EN = {EN:.1f}") #Affichage de l'écart normalisé


