import streamlit as st
import pandas as pd

st.title("Bases de Datos en la Nube: Firebase Firestore")

st.markdown("""
### Ejercicio
Firebase es otra opción excelente adoptada por múltiples startups para almacenar datos en tiempo real.

**Instrucciones:**
1. Asume que se te proporcionó un archivo de credenciales de servicio `llave_secreta.json`.
2. Escribe el **código teórico (usando st.code() o conectándote si tienes tu propia bd)** que emplearías con `firebase_admin` para arrancar la aplicación y obtener el cliente de la base de datos.
3. El objetivo sería conectarse a la colección `vehiculos` de tu Firestore y traer todos los documentos.
4. Indica cómo convertirías la respuesta iterando los documentos para extraer su `to_dict()`.
5. Convierte esa lista a un DataFrame `df_firebase` final.
""")

st.subheader("Tu resultado:")
st.markdown("Escribe en la parte de abajo el código que usarías para lograr el objetivo. Si usas código comentado/teórico, compártelo adentro de `st.code()`.")

# ESTUDIANTE: Escribe tu código a continuación

import firebase_admin
from firebase_admin import credentials, firestore

# Evita reinicializar si Streamlit recarga
if not firebase_admin._apps:
    cred = credentials.Certificate("llave_secreta.json")
    firebase_admin.initialize_app(cred)

# Conectar a Firestore
db = firestore.client()

# Leer colección tourist_places
docs = db.collection("tourist_places").stream()

# Convertir a lista de diccionarios
lugares = []
for doc in docs:
    data = doc.to_dict()
    data["id"] = doc.id  # opcional
    lugares.append(data)

# Convertir a DataFrame
df_firebase = pd.DataFrame(lugares)

# Mostrar en Streamlit
st.dataframe(df_firebase)



