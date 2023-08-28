import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Conversor de Unidades", page_icon=":1234:")

# Título de la aplicación
st.title("Conversor de Unidades")

# Opciones de conversión
conversion_type = st.selectbox("Selecciona el tipo de conversión:", [
    "Temperatura",
    "Longitud",
    "Peso/Masa",
    "Volumen",
    "Tiempo",
    "Velocidad",
    "Área",
    "Energía",
    "Presión",
    "Tamaño de Datos"
])

# Conversión de temperatura
if conversion_type == "Temperatura":
    temperature_option = st.selectbox("Selecciona la conversión de temperatura:", [
        "Celsius a Fahrenheit",
        "Fahrenheit a Celsius",
        "Celsius a Kelvin",
        "Kelvin a Celsius"
    ])
    
    temperature_value = st.number_input("Ingresa la temperatura:")
    
    if temperature_option == "Celsius a Fahrenheit":
        result = (temperature_value * 9/5) + 32
        st.write(f"{temperature_value} °C son aproximadamente {result:.2f} °F.")
    elif temperature_option == "Fahrenheit a Celsius":
        result = (temperature_value - 32) * 5/9
        st.write(f"{temperature_value} °F son aproximadamente {result:.2f} °C.")
    elif temperature_option == "Celsius a Kelvin":
        result = temperature_value + 273.15
        st.write(f"{temperature_value} °C son aproximadamente {result:.2f} K.")
    else:
        result = temperature_value - 273.15
        st.write(f"{temperature_value} K son aproximadamente {result:.2f} °C.")

# Puedes agregar más bloques de conversión para cada categoría de unidades aquí...

else:
    st.write("Seleccione una categoría de conversión.")
