# ProyectoTelco
Proyecto dedicado al trabajo de la asignatura Laboratorio de Minería de Datos

# Proyecto Final:

Este repositorio contiene el pipeline de Machine Learning reproducible para predecir la rotación (churn) de clientes de la empresa ficticia TelcoVision, como parte del examen final de la materia.

El proyecto aplica prácticas de MLOps, incluyendo versionado de datos y modelos con DVC, seguimiento de experimentos, y automatización de CI/CD con GitHub Actions.


# Video de Entrega Final

Aquí está la presentación y demostración en vivo del proyecto (10-15 min), cubriendo todo el pipeline, desde el `git clone` hasta la revisión de experimentos y CI/CD.

**[Enlace al video (YouTube/Google Drive)]** 


# Caso de Uso y Objetivo

Empresa: TelcoVision
Objetivo: Reducir la rotación de clientes (churn).
Entregable: Un pipeline de ML reproducible que entrena un modelo capaz de predecir si un cliente (churn = 1) o no (churn = 0), basado en sus datos demográficos y de uso.


# Cómo Reproducir este Proyecto

Para obtener exactamente los mismos resultados (modelos, métricas y datasets) que se muestran en este proyecto, sigue estos pasos:

Requisitos previos:
Tener git, python 3.9 y conda (o pip) instalados.
Tener acceso a (https://dagshub.com/).

Pasos de Reproducción:

1.  Clonar el repositorio:
    bash
    git clone https://github.com/MauriKemerer/ProyectoTelco
    cd C:\Telco\ProyectoTelco
    

2.  Instalar dependencias:
    Se recomienda crear un entorno virtual
    bash
    Crear entorno Conda
    conda create -n telco_env python=3.9
    conda activate telco_env
    
    pip install -r requirements.txt


3.  Descargar Datos y Modelos (DVC):
    Este comando descarga los datos procesados y el modelo final (model.pkl) desde el DVC remote (DagsHub) sin necesidad de re-entrenar.
    bash
    dvc pull


4.  Re-ejecutar el pipeline completo:
    Si querés verificar todo el pipeline desde cero (limpieza, entrenamiento y evaluación), podés borrar los artefactos y ejecutar:
    bash
    Borrar el modelo model.pkl
    dvc repro

# Experimentos y Modelo Final

Durante la Etapa 4, se realizaron múltiples experimentos variando los hiperparámetros del modelo (definidos en params.yaml) para encontrar la mejor performance.

Modelo Final Elegido:

Se seleccionó el modelo del experimento "sun mink" (Regresión Logística con C=1.0 y solver='liblinear') ya que presentó el mejor balance de métricas.

Las métricas finales de este modelo (obtenidas del archivo metrics.json) son:
Accuracy: 0.6715
Precision: 0.6231155778894473
Recall: 0.17563739376770537
F1: 0.2740331491712707


# CI/CD y Colaboración

Integración Continua (CI): Se configuró un workflow de GitHub Actions (.github/workflows/ci.yaml) que se dispara con cada Pull Request. Este workflow instala dependencias, ejecuta dvc pull y dvc repro para validar que el pipeline no se rompa con nuevos cambios.

Colaboración: El proyecto siguió un flujo de trabajo basado en ramas (Git-Flow). Cada nueva funcionalidad o etapa (ejemplo: etapa-6) se desarrolló en una rama separada y se integró a main mediante un Pull Request (PR), asegurando la validación del CI antes de la fusión.

Muchas gracias!

# Equipo

Mauricio Kemerer Ferrisi
Juan Ignacio Centanaro
Yamil Vogel Dumit
