import streamlit as st
import pandas as pd

st.title("Método 2: Desde una Lista de Listas")

st.markdown("""
### Ejercicio
En este ejercicio debes crear un DataFrame partiendo de una **lista de listas** que represente el inventario de una tienda de tecnología.

1. Crea una lista de listas donde cada sub-lista contenga información de un producto: 
   `[Nombre del producto, Categoría, Precio, Cantidad en stock]`
   Agrega al menos 4 productos diferentes.
2. Crea un DataFrame llamado `df_inventario` a partir de esta lista y pásale el parámetro `columns=[]` definiendo cómo se llamarán tus columnas.
3. Muestra el DataFrame en la aplicación usando `st.dataframe()`.
""")

st.subheader("Tu resultado:")
# ESTUDIANTE: Escribe tu código a continuación

# Crear la lista de listas (inventario)
inventario = [
    ["Laptop Lenovo", "Computadores", 3200000, 10],
    ["Mouse Logitech", "Accesorios", 85000, 25],
    ["Teclado Mecánico", "Accesorios", 210000, 15],
    ["Monitor Samsung 24''", "Monitores", 950000, 8]
]

# Crear el DataFrame con nombres de columnas
df_inventario = pd.DataFrame(
    inventario,
    columns=["Producto", "Categoría", "Precio (COP)", "Stock"]
)

# Mostrar en Streamlit
st.dataframe(df_inventario)


# st.dataframe(...)
