

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ Créer le dataset
data = pd.DataFrame({
    "taille": [150, 160, 170, 180, 190],
    "poids": [50, 60, 65, 75, 85]
})

# 2️⃣ Calculer l'IMC et catégoriser
def calcul_imc(poids, taille_cm):
    return poids / ((taille_cm / 100) ** 2)

def categorie_imc(imc):
    if imc < 18.5:
        return "Maigre"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Surpoids"
    else:
        return "Obèse"

data['IMC'] = data.apply(lambda row: calcul_imc(row['poids'], row['taille']), axis=1)
data['categorie_IMC'] = data['IMC'].apply(categorie_imc)

# 3️⃣ Préparer les données pour le modèle
X = data[['taille']].values  # Feature
y = data['poids'].values     # Target

# 4️⃣ Créer et entraîner le modèle
model = LinearRegression()
model.fit(X, y)

# 5️⃣ Prédire pour une taille de 175 cm
taille_test = np.array([[175]])
poids_pred = model.predict(taille_test)
print(f"Poids prédit pour une taille de 175 cm : {poids_pred[0]:.2f} kg")

# 6️⃣ Visualiser le dataset et la régression
sns.scatterplot(x="taille", y="poids", hue="categorie_IMC", data=data, s=100)
plt.plot(X, model.predict(X), color='red', linewidth=2, label="Régression")
plt.title("Régression linéaire : Taille vs Poids")
plt.xlabel("Taille (cm)")
plt.ylabel("Poids (kg)")
plt.legend()
plt.show()