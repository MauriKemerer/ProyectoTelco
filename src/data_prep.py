import pandas as pd
from pathlib import Path

# --- Paths ---
RAW_DATA_PATH = Path("data/raw/telco_churn.csv")
PROCESSED_DATA_PATH = Path("data/processed/telco_churn_clean.csv")

def main():
    # 1️⃣ Cargar datos
    df = pd.read_csv(RAW_DATA_PATH)

    # 2️⃣ Limpieza básica (sin nulos)
    # Convertir columnas de texto a minúsculas uniformes
    df.columns = [c.strip().lower() for c in df.columns]

    # Eliminar espacios o caracteres extra en valores string
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].str.strip()

    # Convertir tipos numéricos donde corresponda
    if "total_charges" in df.columns:
        df["total_charges"] = pd.to_numeric(df["total_charges"], errors="coerce")

    # 3️⃣ Guardar dataset limpio
    PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"✅ Dataset limpio guardado en: {PROCESSED_DATA_PATH}")

if __name__ == "__main__":
    main()