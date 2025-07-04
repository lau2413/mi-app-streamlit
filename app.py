# -*- coding: utf-8 -*-
"""Despliegue videpjuegos.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Wve1P2rgPp_3aqklP0kNDt-XiWm9R9nc

# Despliegue

- Cargamos el modelo
- Cargamos los datos futuros
- Aplicar tubería
"""

#Importamos librerías básicas
import pandas as pd # manipulacion dataframes
import numpy as np  # matrices y vectores
import matplotlib.pyplot as plt #gráfica

#Paso 1: Limpiar atípicos
def remove_outliers(X):
    #Se asigna valor nulo a los atípicos
    X.loc[(X["Edad"] < 12) | (X["Edad"] > 50), "Edad"] = np.nan
    X.loc[(X["Sexo"] != "Mujer") & (X["Sexo"] != "Hombre"), "Sexo"] = np.nan
    return X

#Cargamos el pipeline con el modelo
import pickle
filename = 'pipeline_modelo.pkl'
pipeline = pickle.load(open(filename, 'rb'))
#pipeline para que no salga el gráfico

#Cargamos los datos futuros
#data = pd.read_csv("videojuegos-datosFuturos.csv")
#data.head()

#Streamlit

#Se crea interfaz gráfica con streamlit para captura de los datos

import streamlit as st

st.title('Predicción de inversión en una tienda de videojuegos')

Edad = st.slider('Edad', min_value=14, max_value=52, value=20, step=1)
videojuego = st.selectbox('Videojuego', ["'Mass Effect'","'Battlefield'", "'Fifa'","'KOA: Reckoning'","'Crysis'","'Sim City'","'Dead Space'","'F1'"])
Plataforma = st.selectbox('Plataforma', ["'Play Station'", "'Xbox'","PC","Otros"])
Sexo = st.selectbox('Sexo', ['Hombre', 'Mujer'])
Consumidor_habitual = st.selectbox('Consumidor_habitual', ['True', 'False'])

#mismo orden y nombres que esta en el df
#Dataframe
datos = [[Edad, videojuego,Plataforma,Sexo,Consumidor_habitual]]
data = pd.DataFrame(datos, columns=['Edad', 'videojuego','Plataforma','Sexo','Consumidor_habitual']) #Dataframe con los mismos nombres de variable

#Hacemos la predicción con el Tree
Y_Tree = pipeline.predict(data)
print(Y_Tree)

data['Prediccion']=Y_Tree
data