import pandas as pd
import json
import yaml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import os

# Leer parámetros desde params.yaml
params = yaml.safe_load(open("params.yaml"))["train"]

# Cargar dataset limpio
data = pd.read_csv("data/processed/telco_churn_clean.csv")

# Separar features y label
X = data.drop(columns=["churn", "customer_id"])
y = data["churn"]

# 🔹 Convertir variables categóricas a numéricas (One-Hot Encoding)
X = pd.get_dummies(X, drop_first=True)

# Dividir en train y test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=params["test_size"], random_state=params["random_state"]
)

# Entrenar modelo
model = LogisticRegression(
    solver=params["solver"],
    max_iter=params["max_iter"],
    C=params["C"]
)
model.fit(X_train, y_train)

# Predicciones
y_pred = model.predict(X_test)

# Calcular métricas
metrics = {
    "accuracy": accuracy_score(y_test, y_pred),
    "precision": precision_score(y_test, y_pred),
    "recall": recall_score(y_test, y_pred),
    "f1": f1_score(y_test, y_pred)
}

# Guardar métricas
os.makedirs("metrics", exist_ok=True)
with open("metrics/metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)

# Guardar modelo
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/model.pkl")

print("✅ Entrenamiento completado. Métricas guardadas en metrics/metrics.json")
