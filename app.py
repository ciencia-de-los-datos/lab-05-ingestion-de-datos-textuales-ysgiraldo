import pandas as pd
import zipfile
import os

# Descomprimir data.zip
with zipfile.ZipFile('data.zip', 'r') as zip_ref:
    zip_ref.extractall()

# Leer archivos .txt y crear un conjunto de datos
def create_dataset(base_path):
    data = []

    for sentiment in os.listdir(base_path):
        sentiment_dir = os.path.join(base_path, sentiment)
        if os.path.isdir(sentiment_dir):
            # Ignorar archivos ocultos y directorios que comiencen con un punto
            if not sentiment.startswith("."):
                files = os.listdir(sentiment_dir)
                for file_name in files:
                    # Doble verificación
                    if not file_name.startswith("."):
                        file_path = os.path.join(sentiment_dir, file_name)
                        with open(file_path, 'r', encoding='utf-8') as file:
                            phrase = file.read().strip()
                            data.append({'phrase': phrase, 'sentiment': sentiment})

    return pd.DataFrame(data)

# Crear csv
train_data = create_dataset("train")
test_data = create_dataset("test")

train_data.to_csv("train_dataset.csv", index=False)
test_data.to_csv("test_dataset.csv", index=False)