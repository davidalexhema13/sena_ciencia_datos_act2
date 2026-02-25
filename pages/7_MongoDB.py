import streamlit as st
import pandas as pd

st.title("Bases de Datos en la Nube: MongoDB")

st.markdown("""
### Ejercicio
MongoDB es una base de datos NoSQL muy popular que almacena la información de forma muy similar a JSON.

**Instrucciones:**
1. Imagina que tienes acceso a un clúster de MongoDB Atlas. Para este ejercicio no necesitas conectarte realmente a la base de datos a menos que tengas un clúster de prueba.
2. Basándote en el material de clase, escribe el **código necesario (comentado si no tienes conexión)** para conectarte usando `pymongo` y la clase `MongoClient`.
3. Supón que la base de datos se llama `Veterinaria` y la colección se llama `mascotas`.
4. El código debe incluir cómo extraer los documentos y convertirlos en el DataFrame `df_mongo`.
""")

st.subheader("Tu resultado:")
st.markdown("Si no tienes la conexión real, escribe tu código usando `st.code()` para demostrar cómo lo harías teóricamente.")

# ESTUDIANTE: Escribe tu código (o tu st.code teórico) a continuación

import streamlit as st
import pandas as pd
from pymongo import MongoClient

st.title("Conexión REAL a MongoDB Atlas")

# 🔗 Cadena de conexión 
uri = "mongodb+srv://david_user:dBUul0GjVWXXcRLs@cluster0.nrf3ht0.mongodb.net/?appName=Cluster0"

# Crear cliente
client = MongoClient(uri)

# Crear / conectar base de datos
db = client["Veterinaria"]

# Crear / conectar colección
coleccion = db["mascotas"]

st.success("✅ Conectado correctamente a MongoDB Atlas")

# Insertar un dato de prueba (solo la primera vez)
coleccion.insert_one({
    "nombre": "Firulais",
    "especie": "Perro",
    "edad": 3
})

st.write("Dato insertado")

# Leer datos de la colección
datos = list(coleccion.find({}, {"_id": 0}))

df_mongo = pd.DataFrame(datos)

st.subheader("Datos desde MongoDB:")
st.dataframe(df_mongo)



