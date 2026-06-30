"""Exécuter les cellules les unes après les autres après les avoir complétées
en cliquant sur Run puis Execute Cell (ou CTRL + Entrée)
Pour exécuter l'ensemble du fichier : CTRL + E
"""
#TP Caractérisation d'une bobine

## Cellule 1 :Importation des bibliothèques nécessaires

import numpy as np                  # pour la manipulation des tableaux
import matplotlib.pyplot as plt     # pour les représentations graphiques

## Cellule 2 : Données expérimentales
"""
x = np.array([1., 1.1, 1.2])
L'objet x créé est un tableau à une dimension (nécessité d'importer le module numpy).
Le tableau est défini ici à partir d'une liste de réels (les valeurs expérimentales mesurées en physique doivent toujours être déclarées en Python comme des réels!)
"""
R =             # Tableau des valeurs de R en Ohm : à compléter
inv_tau =       # Tableau des valeurs de 1/tau en s-1 : à compléter

tau = 1 / inv_tau # Expression de tau

r =    # Valeur de r de la bobine en Ohm : à compléter
Rg =   # Valeur de Rg du GBF en Ohm : à compléter
Réq =  # Expression de Réq : à compléter

## Cellule 3 :  Calcul des valeurs de L
L =        #  Expression de L en mH (attention à l'unité!) : à compléter

## Cellule 4 : Histogramme
plt.hist(     )  # Compléter entre les parenthèses
plt.xlabel(    ) # Compléter entre les parenthèses
plt.ylabel(    ) # Compléter entre les parenthèses
plt.title(     ) # Compléter entre les parenthèses
plt.show()

## Cellule 5 : Etude statistique et affichage des résultats
Lmoy = np.mean(L)              # Calcul de la valeur moyenne
u_L = np.std(L,ddof=1)         # Calcul de l'écart-type expérimental
u_Lmoy =                       # Calcul de l'incertitude-type sur la valeur moyenne : à compléter

print(f"La valeur moyenne de L est Lmoy = {Lmoy:.2f} mH\n")
print(f"L'écart-type expérimental est u_L = {u_L:.2f} mH \n")
print(f"L'incertitude-type sur la valeur moyenne est u_Lmoy = {u_Lmoy:.2f} mH \n")


