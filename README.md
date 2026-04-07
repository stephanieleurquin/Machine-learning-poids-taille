# MachineLearning2026

## Description
Ce projet est un **premier exemple de Machine Learning** utilisant Python et scikit-learn.  
L’objectif est de prédire le **poids d’une personne à partir de sa taille** en utilisant une **régression linéaire simple**.

---

## Technologies utilisées
- Python 3  
- Pandas (gestion des données)  
- NumPy (calcul numérique)  
- Matplotlib & Seaborn (visualisation)  
- scikit-learn (modèle de régression linéaire)

---

## Contenu du projet
1. **Création d’un dataset simple** :  
   - Colonnes : `taille` (cm), `poids` (kg)  
   - Exemple : 150 cm → 50 kg  

2. **Calcul de l’IMC** (Indice de Masse Corporelle) :  
   - Fonction Python `calcul_imc(poids, taille)`  
   - Ajout d’une colonne `categorie_IMC` : "Maigre", "Normal", "Surpoids", "Obèse"  

3. **Visualisation des données** :  
   - Scatter plot taille vs poids  
   - Couleurs selon la catégorie IMC  

4. **Machine Learning** :  
   - Modèle : `LinearRegression` de scikit-learn  
   - Entrée : `taille`  
   - Sortie : `poids`  
   - Prédiction pour une taille donnée (ex : 175 cm)  

5. **Visualisation du modèle** :  
   - Ligne rouge représentant la régression linéaire sur le scatter plot  

---

## Instructions pour exécuter le projet
1. Cloner le projet ou télécharger les fichiers.

2. 1. Cloner le projet ou télécharger les fichiers.  
2. Installer les bibliothèques nécessaires :
bash
   pip install pandas numpy matplotlib seaborn scikit-learn


   ##Exemple de sortie:
   Poids prédit pour une taille de 175 cm : 71.25 kg

   Auteur

   Vansch.
4. Installer les bibliothèques nécessaires :
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
