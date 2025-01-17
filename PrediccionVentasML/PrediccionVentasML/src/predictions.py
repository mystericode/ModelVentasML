# src/predictions.py
# Autor Dairo Delgadillo
# Fecha 13/01/2025
# Descripcion predice las ventas segun la fecha 
import pickle
import os
import pandas as pd
from .model_training import train_model
from .data_preprocessing import load_data

# Verifica si ya existe la carpeta y el modelo dentro de esta 
def ensure_model_exists():
    model_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models')
    model_path = os.path.join(model_dir, 'sales_model.pkl')

    # Verifica si existe la carpeta models y si existe el archivo
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    # Verificamos si ya existe la carpeta y los datos dentro de esta misma
    if not os.path.exists(model_path):
        data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'sales_data.csv')
        if not os.path.exists(data_path):
            raise FileNotFoundError("El archivo 'ventas.csv' no existe en la carpeta 'data'")
        
        data = load_data(data_path)
        train_model(data)
    
    return model_path

# predicsion de los dias, segun el año y normalizamos los datos para realizar predisiones evaluativas
def predict_sales(day):
    try:
        model_path = ensure_model_exists()
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        normalized_day = ((day - 1) % 365) + 1
        prediction = model.predict([[normalized_day]])
        prediction_value = round(float(prediction[0]))
        prediction_value = max(0, min(prediction_value, 500))
        return prediction_value
    except Exception as e:
        print(f"Error en predict_sales: {str(e)}")
        return None
