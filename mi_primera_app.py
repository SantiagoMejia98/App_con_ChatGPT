import streamlit as st

# Título y autor
st.title("Mi primera app")
st.write("Esta app fue elaborada por Santiago Andrés Mejía García.")

# Pregunta al usuario por su nombre
nombre_usuario = st.text_input("Por favor, ingresa tu nombre:")

# Verifica si se ingresó un nombre
if nombre_usuario:
    mensaje_bienvenida = f"{nombre_usuario}, te doy la bienvenida a mi primera app."
    st.write(mensaje_bienvenida)
