# Vecteurs

Un vecteur $\vec{V}$ est défini par trois caractéristiques :  

- Sa **norme**, notée $||\vec{V}||$  
- Sa **direction**  
- Son **sens**

---

## Vecteur lié et glisseur

- Un vecteur est **lié** lorsqu’il est associé à un point $A$.  
  On le note $(A,\vec{V})$ ou $\vec{V}(A)$.

- Un **glisseur** (ou vecteur glissant) est similaire, mais associé à une droite.  

---

## Composantes dans une B.O.N.D

Dans une B.O.N.D, un vecteur possède trois composantes selon $x$, $y$, et $z$.  
On peut l’écrire :  
$$\vec{V} = a\,\vec{x} + b\,\vec{y} + c\,\vec{z}.$$

Sa norme est :  
$$||\vec{V}|| = \sqrt{a^2 + b^2 + c^2}.$$

---

# Opérations sur les vecteurs

## Produit scalaire

Le **produit scalaire** de deux vecteurs $\vec{u}$ et $\vec{v}$ est défini par :  
$$\vec{u} \cdot \vec{v} = ||\vec{u}||\,||\vec{v}|| \cos \theta,$$  
où $\theta$ est l’angle entre $\vec{u}$ et $\vec{v}$.

Si $\vec{u}$ et $\vec{v}$ sont exprimés dans la même base :  
$$\vec{u} \cdot \vec{v} = u_x v_x + u_y v_y + u_z v_z.$$

**Projection sur un vecteur unitaire :**  
$$\text{proj}_{\vec{e}}(\vec{u}) = (\vec{u} \cdot \vec{e})\,\vec{e}.$$

---

## Produit vectoriel

Le **produit vectoriel** de $\vec{u}$ et $\vec{v}$ donne un vecteur $\vec{w}$ :  

$$\vec{w} = \vec{u} \mathbin{\wedge} \vec{v}, \quad ||\vec{w}|| = ||\vec{u}||\,||\vec{v}|| \sin \theta,$$  
où $\theta$ est l’angle entre $\vec{u}$ et $\vec{v}$, et $(\vec{u},\vec{v},\vec{w})$ forme un **trièdre direct**.

Propriétés :  
- Non commutatif : $\vec{u} \mathbin{\wedge} \vec{v} = -(\vec{v} \mathbin{\wedge} \vec{u})$  
- Distributif par rapport à un scalaire : $\alpha (\vec{u} \mathbin{\wedge} \vec{v}) = (\alpha \vec{u}) \mathbin{\wedge} \vec{v} = \vec{u} \mathbin{\wedge} (\alpha \vec{v})$

**Produit mixte** (vectoriel + scalaire) :  
$$\vec{u} \cdot (\vec{v} \mathbin{\wedge} \vec{w})$$

**Double produit vectoriel** :  
$$\vec{u} \mathbin{\wedge} (\vec{v} \mathbin{\wedge} \vec{w}) = (\vec{u} \cdot \vec{w}) \vec{v} - (\vec{u} \cdot \vec{v}) \vec{w}$$

---

# Moment en un point d’un vecteur lié

$$\vec{M}(P,(A,\vec{V})) = \overrightarrow{PA} \mathbin{\wedge} \vec{V}.$$

---

# Dérivation vectorielle

Formule de dérivée d’un vecteur $\vec{U}$ par rapport au temps et à la base $B$ :  
$$\frac{d\vec{U}}{dt}\Big|_B = \dot{U}_x \vec{x} + \dot{U}_y \vec{y} + \dot{U}_z \vec{z}$$

Notation alternative :  
$$\dot{\vec{U}} = \frac{d\vec{U}}{dt}$$

### Changement de base lors de la dérivation

$$\frac{d\vec{U}}{dt}\Big|_{B_j} = \frac{d\vec{U}}{dt}\Big|_{B_k} + \boldsymbol{\omega}_{k/j} \mathbin{\wedge} \vec{U},$$  
où $\boldsymbol{\omega}_{k/j}$ est le vecteur **vitesse angulaire** de $B_k$ par rapport à $B_j$.
