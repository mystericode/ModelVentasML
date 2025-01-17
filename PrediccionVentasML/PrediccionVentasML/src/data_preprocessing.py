# src/data_preprocessing.py
import pandas as pd    #manipula datos numericos y aritmeticos 

def load_data(file_path):  #cargando data 
    data = pd.read_csv(file_path, parse_dates=['Fecha'])  #leyendo data y separando Fecha
    data['Dia'] = data['Fecha'].dt.dayofyear   #sacamos de la fecha lo que es el dia dependiendo del año
    return data   #retornamos lo que es la data 




