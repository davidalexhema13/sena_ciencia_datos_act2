import streamlit as st
import pandas as pd

st.title("Método 1: Juntando varias Series")

st.markdown("""
### Ejercicio
En este ejercicio debes crear un DataFrame agrupando información sobre **películas favoritas**.

1. Crea tres Series de Pandas diferentes:
    - Una serie llamada `titulos` con al menos 4 nombres de películas.
    - Una serie llamada `directores` con los directores de esas películas.
    - Una serie llamada `años` con el año de estreno.
2. Une estas tres series en un único DataFrame llamado `df_peliculas`, asignando nombres descriptivos a las columnas (por ejemplo: `Título`, `Director`, `Año de Estreno`).
3. Muestra el DataFrame en la aplicación usando `st.dataframe()`.
""")

st.subheader("Tu resultado:")
# ESTUDIANTE: Escribe tu código a continuación

# Crear las Series
titulos = pd.Series([
    "Inception",
    "The Matrix",
    "Interstellar",
    "Parasite"
])

directores = pd.Series([
    "Christopher Nolan",
    "Lana y Lilly Wachowski",
    "Christopher Nolan",
    "Bong Joon-ho"
])

años = pd.Series([
    2010,
    1999,
    2014,
    2019
])

# Unir las Series en un DataFrame
df_peliculas = pd.DataFrame({
    "Título": titulos,
    "Director": directores,
    "Año de Estreno": años
})

# Mostrar el DataFrame en Streamlit
st.dataframe(df_peliculas)


# st.dataframe(...)
