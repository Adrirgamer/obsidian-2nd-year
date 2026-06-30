"""Exécuter les cellules les unes après les autres après les avoir complétées
en cliquant sur Run puis Execute Cell (ou CTRL + Entrée)
Pour exécuter l'ensemble du fichier : CTRL + E
"""
#TP Spectrogoniomètre à réseau

## Cellule 1 : Importation des bibliothèques
import matplotlib.pyplot as plt
import numpy as np

## Cellule 2 : Données expérimentales -> A COMPLETER
alpha1 =     # Tableau des angles alpha1 en degré : à compléter
alpha1n =    # Tableau des angles alpha-1 en degré : à compléter
lamb =       # Tableau des longueurs d'onde en nm : à compléter

y =          # Expression littérale de sin(i'1) : à compléter

## Cellule 3 : Tracé du nuage de points expérimentaux -> A COMPLETER

plt.plot(       ) # Tracé de sin(i'1) en fonction de lamb avec des ronds bleus : à compléter
plt.xlabel(r'$\lambda$ (nm)')
plt.ylabel(r"$\sin(i'_{1})$" )
plt.title(r"Courbe d'étalonnage : évolution de $\sin(i'_{1})$ en fonction de la longueur d'onde $\lambda$")
plt.grid()
plt.show()

## Cellule 4 : Régression linéaire : courbe d'étalonnage (lampe Hg) -> A COMPLETER
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
p =    # Modélisation de la courbe y = f(lamb) : obtention des coefficients de la régression linéaire : à compléter
ylin =   # Équation de la régression linéaire : à compléter

# Tracé de la caractéristique linéarisée
plt.plot(          ,label="Régression linéaire")# Tracé de la régression linéaire en trait rouge
plt.legend(loc="upper left")
plt.show()

#Affichage des paramètres du modèle linéaire
print(f"coefficient directeur {p[0]:.2e} ") #Affichage du coefficient directeur de la droite de régression (format scientifique avec 2 décimales)
print(     ) #Affichage de l'ordonnée à l'origine de la droite de régression (format scientifique avec 2 décimales) : à compléter

## Cellule 5 : Utilisation de la courbe d'étalonnage (lampe Na) -> A COMPLETER
alpha1_Na =    # Tableau des angles alpha1 en degré: : à compléter
alpha1n_Na =   #Tableau des angles alpha-1 en degré : : à compléter
y_Na =         # Expression littérale de sin(i'1) : à compléter
lamb_Na  =     # Tableau des longueurs d'onde du Na calculées grâce à la régression linéaire

print(f"Longueurs d'onde du sodium Na : {lamb_Na[0]:.1f} nm et {lamb_Na[1]:.1f} nm") #Affichage des longueurs d'onde du Na


