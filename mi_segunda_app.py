import streamlit as st

# Título de la aplicación
st.title("Conversor de Unidades")

# Funciones de conversión de temperatura
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Funciones de conversión de longitud
def pies_to_metros(pies):
    return pies * 0.3048

def metros_to_pies(metros):
    return metros / 0.3048

def pulgadas_to_centimetros(pulgadas):
    return pulgadas * 2.54

def centimetros_to_pulgadas(centimetros):
    return centimetros / 2.54

# Funciones de conversión de peso/masa
def libras_to_kilogramos(libras):
    return libras * 0.453592

def kilogramos_to_libras(kilogramos):
    return kilogramos / 0.453592

def onzas_to_gramos(onzas):
    return onzas * 28.3495

def gramos_to_onzas(gramos):
    return gramos / 28.3495

# Funciones de conversión de volumen
def galones_to_litros(galones):
    return galones * 3.78541

def litros_to_galones(litros):
    return litros / 3.78541

def pulgadas_cubicas_to_cm_cubicos(pulgadas_cubicas):
    return pulgadas_cubicas * 16.3871

def cm_cubicos_to_pulgadas_cubicas(cm_cubicos):
    return cm_cubicos / 16.3871

# Funciones de conversión de tiempo
def horas_to_minutos(horas):
    return horas * 60

def minutos_to_segundos(minutos):
    return minutos * 60

def dias_to_horas(dias):
    return dias * 24

def semanas_to_dias(semanas):
    return semanas * 7

# Funciones de conversión de velocidad
def mph_to_kmph(mph):
    return mph * 1.60934

def kmph_to_mps(kmph):
    return kmph * 1000 / 3600

def knots_to_mph(knots):
    return knots * 1.15078

def mps_to_fps(mps):
    return mps * 3.28084

# Funciones de conversión de área
def metros_cuadrados_to_pies_cuadrados(metros_cuadrados):
    return metros_cuadrados * 10.7639

def pies_cuadrados_to_metros_cuadrados(pies_cuadrados):
    return pies_cuadrados / 10.7639

def km_cuadrados_to_millas_cuadradas(km_cuadrados):
    return km_cuadrados * 0.386102

def millas_cuadradas_to_km_cuadrados(millas_cuadradas):
    return millas_cuadradas / 0.386102

# Funciones de conversión de energía
def julios_to_calorias(julios):
    return julios * 0.239006

def calorias_to_kilojulios(calorias):
    return calorias * 4.184

def kw_hora_to_megajulios(kw_hora):
    return kw_hora * 3.6

def megajulios_to_kw_hora(megajulios):
    return megajulios / 3.6

# Funciones de conversión de presión
def pascales_to_atmosferas(pascales):
    return pascales / 101325

def atmosferas_to_pascales(atmosferas):
    return atmosferas * 101325

def bares_to_libras_pulgada_cuadrada(bares):
    return bares * 14.5038

def libras_pulgada_cuadrada_to_bares(libras_pulgada_cuadrada):
    return libras_pulgada_cuadrada / 14.5038

# Funciones de conversión de tamaño de datos
def megabytes_to_gigabytes(megabytes):
    return megabytes / 1024

def gigabytes_to_terabytes(gigabytes):
    return gigabytes / 1024

def kilobytes_to_megabytes(kilobytes):
    return kilobytes / 1024

def terabytes_to_petabytes(terabytes):
    return terabytes / 1024

# Widget para seleccionar el tipo de conversión
tipo_conversion = st.selectbox("Selecciona el tipo de conversión", [
    "Temperatura",
    "Longitud",
    "Peso/Masa",
    "Volumen",
    "Tiempo",
    "Velocidad",
    "Área",
    "Energía",
    "Presión",
    "Tamaño de Datos",
    # Agregar más tipos de conversión aquí...
])

# Realizar la conversión según la selección
if tipo_conversion == "Temperatura":
    conversiones_temperatura = [
        "Celsius a Fahrenheit",
        "Fahrenheit a Celsius",
        "Celsius a Kelvin",
        "Kelvin a Celsius"
    ]
    
    conversion_seleccionada = st.selectbox("Selecciona la conversión de temperatura", conversiones_temperatura)
    
    if conversion_seleccionada == "Celsius a Fahrenheit":
        celsius = st.number_input("Ingresa la temperatura en Celsius", value=0.0)
        fahrenheit = celsius_to_fahrenheit(celsius)
        st.write(f"{celsius} °C = {fahrenheit:.2f} °F")
    
    elif conversion_seleccionada == "Fahrenheit a Celsius":
        fahrenheit = st.number_input("Ingresa la temperatura en Fahrenheit", value=0.0)
        celsius = fahrenheit_to_celsius(fahrenheit)
        st.write(f"{fahrenheit} °F = {celsius:.2f} °C")
    
    elif conversion_seleccionada == "Celsius a Kelvin":
        celsius = st.number_input("Ingresa la temperatura en Celsius", value=0.0)
        kelvin = celsius_to_kelvin(celsius)
        st.write(f"{celsius} °C = {kelvin:.2f} K")
    
    elif conversion_seleccionada == "Kelvin a Celsius":
        kelvin = st.number_input("Ingresa la temperatura en Kelvin", value=0.0)
        celsius = kelvin_to_celsius(kelvin)
        st.write(f"{kelvin} K = {celsius:.2f} °C")
    pass

elif tipo_conversion == "Longitud":
    conversiones_longitud = [
        "Pies a Metros",
        "Metros a Pies",
        "Pulgadas a Centímetros",
        "Centímetros a Pulgadas"
    ]
    
    conversion_seleccionada = st.selectbox("Selecciona la conversión de longitud", conversiones_longitud)
    
    if conversion_seleccionada == "Pies a Metros":
        pies = st.number_input("Ingresa la longitud en pies", value=0.0)
        metros = pies_to_metros(pies)
        st.write(f"{pies} pies = {metros:.2f} metros")
    
    elif conversion_seleccionada == "Metros a Pies":
        metros = st.number_input("Ingresa la longitud en metros", value=0.0)
        pies = metros_to_pies(metros)
        st.write(f"{metros} metros = {pies:.2f} pies")
    
    elif conversion_seleccionada == "Pulgadas a Centímetros":
        pulgadas = st.number_input("Ingresa la longitud en pulgadas", value=0.0)
        centimetros = pulgadas_to_centimetros(pulgadas)
        st.write(f"{pulgadas} pulgadas = {centimetros:.2f} centímetros")
    
    elif conversion_seleccionada == "Centímetros a Pulgadas":
        centimetros = st.number_input("Ingresa la longitud en centímetros", value=0.0)
        pulgadas = centimetros_to_pulgadas(centimetros)
        st.write(f"{centimetros} centímetros = {pulgadas:.2f} pulgadas")
    pass

elif tipo_conversion == "Peso/Masa":
    conversiones_peso = [
        "Libras a Kilogramos",
        "Kilogramos a Libras",
        "Onzas a Gramos",
        "Gramos a Onzas"
    ]
    
    conversion_seleccionada = st.selectbox("Selecciona la conversión de peso/masa", conversiones_peso)
    
    if conversion_seleccionada == "Libras a Kilogramos":
        libras = st.number_input("Ingresa el peso en libras", value=0.0)
        kilogramos = libras_to_kilogramos(libras)
        st.write(f"{libras} libras = {kilogramos:.2f} kilogramos")
    
    elif conversion_seleccionada == "Kilogramos a Libras":
        kilogramos = st.number_input("Ingresa el peso en kilogramos", value=0.0)
        libras = kilogramos_to_libras(kilogramos)
        st.write(f"{kilogramos} kilogramos = {libras:.2f} libras")
    
    elif conversion_seleccionada == "Onzas a Gramos":
        onzas = st.number_input("Ingresa el peso en onzas", value=0.0)
        gramos = onzas_to_gramos(onzas)
        st.write(f"{onzas} onzas = {gramos:.2f} gramos")
    
    elif conversion_seleccionada == "Gramos a Onzas":
        gramos = st.number_input("Ingresa el peso en gramos", value=0.0)
        onzas = gramos_to_onzas(gramos)
        st.write(f"{gramos} gramos = {onzas:.2f} onzas")
    pass

elif tipo_conversion == "Volumen":
    conversiones_volumen = [
        "Galones a Litros",
        "Litros a Galones",
        "Pulgadas cúbicas a Centímetros cúbicos",
        "Centímetros cúbicos a Pulgadas cúbicas"
    ]
    
    conversion_seleccionada = st.selectbox("Selecciona la conversión de volumen", conversiones_volumen)
    
    if conversion_seleccionada == "Galones a Litros":
        galones = st.number_input("Ingresa el volumen en galones", value=0.0)
        litros = galones_to_litros(galones)
        st.write(f"{galones} galones = {litros:.2f} litros")
    
    elif conversion_seleccionada == "Litros a Galones":
        litros = st.number_input("Ingresa el volumen en litros", value=0.0)
        galones = litros_to_galones(litros)
        st.write(f"{litros} litros = {galones:.2f} galones")
    
    elif conversion_seleccionada == "Pulgadas cúbicas a Centímetros cúbicos":
        pulgadas_cubicas = st.number_input("Ingresa el volumen en pulgadas cúbicas", value=0.0)
        cm_cubicos = pulgadas_cubicas_to_cm_cubicos(pulgadas_cubicas)
        st.write(f"{pulgadas_cubicas} pulgadas cúbicas = {cm_cubicos:.2f} cm³")
    
    elif conversion_seleccionada == "Centímetros cúbicos a Pulgadas cúbicas":
        cm_cubicos = st.number_input("Ingresa el volumen en centímetros cúbicos", value=0.0)
        pulgadas_cubicas = cm_cubicos_to_pulgadas_cubicas(cm_cubicos)
        st.write(f"{cm_cubicos} cm³ = {pulgadas_cubicas:.2f} pulgadas cúbicas")
    pass

elif tipo_conversion == "Tiempo":
    conversiones_tiempo = [
        "Horas a Minutos",
        "Minutos a Segundos",
        "Días a Horas",
        "Semanas a Días"
    ]
    
    conversion_seleccionada = st.selectbox("Selecciona la conversión de tiempo", conversiones_tiempo)
    
    if conversion_seleccionada == "Horas a Minutos":
        horas = st.number_input("Ingresa la cantidad de horas", value=0.0)
        minutos = horas_to_minutos(horas)
        st.write(f"{horas} horas = {minutos:.2f} minutos")
    
    elif conversion_seleccionada == "Minutos a Segundos":
        minutos = st.number_input("Ingresa la cantidad de minutos", value=0.0)
        segundos = minutos_to_segundos(minutos)
        st.write(f"{minutos} minutos = {segundos:.2f} segundos")
    
    elif conversion_seleccionada == "Días a Horas":
        dias = st.number_input("Ingresa la cantidad de días", value=0.0)
        horas = dias_to_horas(dias)
        st.write(f"{dias} días = {horas:.2f} horas")
    
    elif conversion_seleccionada == "Semanas a Días":
        semanas = st.number_input("Ingresa la cantidad de semanas", value=0.0)
        dias = semanas_to_dias(semanas)
        st.write(f"{semanas} semanas = {dias:.2f} días")
    pass

elif tipo_conversion == "Velocidad":
    conversiones_velocidad = [
        "Millas por hora a Kilómetros por hora",
        "Kilómetros por hora a Metros por segundo",
        "Nudos a Millas por hora",
        "Metros por segundo a Pies por segundo"
    ]
    
    conversion_seleccionada = st.selectbox("Selecciona la conversión de velocidad", conversiones_velocidad)
    
    if conversion_seleccionada == "Millas por hora a Kilómetros por hora":
        mph = st.number_input("Ingresa la velocidad en millas por hora", value=0.0)
        kmph = mph_to_kmph(mph)
        st.write(f"{mph} mph = {kmph:.2f} km/h")
    
    elif conversion_seleccionada == "Kilómetros por hora a Metros por segundo":
        kmph = st.number_input("Ingresa la velocidad en kilómetros por hora", value=0.0)
        mps = kmph_to_mps(kmph)
        st.write(f"{kmph} km/h = {mps:.2f} m/s")
    
    elif conversion_seleccionada == "Nudos a Millas por hora":
        knots = st.number_input("Ingresa la velocidad en nudos", value=0.0)
        mph = knots_to_mph(knots)
        st.write(f"{knots} nudos = {mph:.2f} mph")
    
    elif conversion_seleccionada == "Metros por segundo a Pies por segundo":
        mps = st.number_input("Ingresa la velocidad en metros por segundo", value=0.0)
        fps = mps_to_fps(mps)
        st.write(f"{mps} m/s = {fps:.2f} ft/s")
    pass

elif tipo_conversion == "Área":
    conversiones_area = [
        "Metros cuadrados a Pies cuadrados",
        "Pies cuadrados a Metros cuadrados",
        "Kilómetros cuadrados a Millas cuadradas",
        "Millas cuadradas a Kilómetros cuadrados"
    ]
    
    conversion_seleccionada = st.selectbox("Selecciona la conversión de área", conversiones_area)
    
    if conversion_seleccionada == "Metros cuadrados a Pies cuadrados":
        metros_cuadrados = st.number_input("Ingresa el área en metros cuadrados", value=0.0)
        pies_cuadrados = metros_cuadrados_to_pies_cuadrados(metros_cuadrados)
        st.write(f"{metros_cuadrados} m² = {pies_cuadrados:.2f} ft²")
    
    elif conversion_seleccionada == "Pies cuadrados a Metros cuadrados":
        pies_cuadrados = st.number_input("Ingresa el área en pies cuadrados", value=0.0)
        metros_cuadrados = pies_cuadrados_to_metros_cuadrados(pies_cuadrados)
        st.write(f"{pies_cuadrados} ft² = {metros_cuadrados:.2f} m²")
    
    elif conversion_seleccionada == "Kilómetros cuadrados a Millas cuadradas":
        km_cuadrados = st.number_input("Ingresa el área en kilómetros cuadrados", value=0.0)
        millas_cuadradas = km_cuadrados_to_millas_cuadradas(km_cuadrados)
        st.write(f"{km_cuadrados} km² = {millas_cuadradas:.2f} mi²")
    
    elif conversion_seleccionada == "Millas cuadradas a Kilómetros cuadrados":
        millas_cuadradas = st.number_input("Ingresa el área en millas cuadradas", value=0.0)
        km_cuadrados = millas_cuadradas_to_km_cuadrados(millas_cuadradas)
        st.write(f"{millas_cuadradas} mi² = {km_cuadrados:.2f} km²")
    pass

    elif tipo_conversion == "Energía":
    conversiones_energia = [
        "Julios a Calorías",
        "Calorías a Kilojulios",
        "Kilovatios-hora a Megajulios",
        "Megajulios a Kilovatios-hora"
    ]
    
    conversion_seleccionada = st.selectbox("Selecciona la conversión de energía", conversiones_energia)
    
    if conversion_seleccionada == "Julios a Calorías":
        julios = st.number_input("Ingresa la energía en julios", value=0.0)
        calorias = julios_to_calorias(julios)
        st.write(f"{julios} J = {calorias:.2f} cal")
    
    elif conversion_seleccionada == "Calorías a Kilojulios":
        calorias = st.number_input("Ingresa la energía en calorías", value=0.0)
        kilojulios = calorias_to_kilojulios(calorias)
        st.write(f"{calorias} cal = {kilojulios:.2f} kJ")
    
    elif conversion_seleccionada == "Kilovatios-hora a Megajulios":
        kw_hora = st.number_input("Ingresa la energía en kilovatios-hora", value=0.0)
        megajulios = kw_hora_to_megajulios(kw_hora)
        st.write(f"{kw_hora} kWh = {megajulios:.2f} MJ")
    
    elif conversion_seleccionada == "Megajulios a Kilovatios-hora":
        megajulios = st.number_input("Ingresa la energía en megajulios", value=0.0)
        kw_hora = megajulios_to_kw_hora(megajulios)
        st.write(f"{megajulios} MJ = {kw_hora:.2f} kWh")
    pass

elif tipo_conversion == "Presión":
    conversiones_presion = [
        "Pascales a Atmosferas",
        "Atmosferas a Pascales",
        "Bares a Libras por pulgada cuadrada",
        "Libras por pulgada cuadrada a Bares"
    ]
    
    conversion_seleccionada = st.selectbox("Selecciona la conversión de presión", conversiones_presion)
    
    if conversion_seleccionada == "Pascales a Atmosferas":
        pascales = st.number_input("Ingresa la presión en pascales", value=0.0)
        atmosferas = pascales_to_atmosferas(pascales)
        st.write(f"{pascales} Pa = {atmosferas:.6f} atm")
    
    elif conversion_seleccionada == "Atmosferas a Pascales":
        atmosferas = st.number_input("Ingresa la presión en atmosferas", value=0.0)
        pascales = atmosferas_to_pascales(atmosferas)
        st.write(f"{atmosferas} atm = {pascales:.2f} Pa")
    
    elif conversion_seleccionada == "Bares a Libras por pulgada cuadrada":
        bares = st.number_input("Ingresa la presión en bares", value=0.0)
        libras_pulgada_cuadrada = bares_to_libras_pulgada_cuadrada(bares)
        st.write(f"{bares} bar = {libras_pulgada_cuadrada:.2f} psi")
    
    elif conversion_seleccionada == "Libras por pulgada cuadrada a Bares":
        libras_pulgada_cuadrada = st.number_input("Ingresa la presión en libras por pulgada cuadrada", value=0.0)
        bares = libras_pulgada_cuadrada_to_bares(libras_pulgada_cuadrada)
        st.write(f"{libras_pulgada_cuadrada} psi = {bares:.2f} bar")
    pass

    elif tipo_conversion == "Tamaño de Datos":
    conversiones_tamanio_datos = [
        "Megabytes a Gigabytes",
        "Gigabytes a Terabytes",
        "Kilobytes a Megabytes",
        "Terabytes a Petabytes"
    ]
    
    conversion_seleccionada = st.selectbox("Selecciona la conversión de tamaño de datos", conversiones_tamanio_datos)
    
    if conversion_seleccionada == "Megabytes a Gigabytes":
        megabytes = st.number_input("Ingresa el tamaño en megabytes", value=0.0)
        gigabytes = megabytes_to_gigabytes(megabytes)
        st.write(f"{megabytes} MB = {gigabytes:.6f} GB")
    
    elif conversion_seleccionada == "Gigabytes a Terabytes":
        gigabytes = st.number_input("Ingresa el tamaño en gigabytes", value=0.0)
        terabytes = gigabytes_to_terabytes(gigabytes)
        st.write(f"{gigabytes} GB = {terabytes:.6f} TB")
    
    elif conversion_seleccionada == "Kilobytes a Megabytes":
        kilobytes = st.number_input("Ingresa el tamaño en kilobytes", value=0.0)
        megabytes = kilobytes_to_megabytes(kilobytes)
        st.write(f"{kilobytes} KB = {megabytes:.6f} MB")
    
    elif conversion_seleccionada == "Terabytes a Petabytes":
        terabytes = st.number_input("Ingresa el tamaño en terabytes", value=0.0)
        petabytes = terabytes_to_petabytes(terabytes)
        st.write(f"{terabytes} TB = {petabytes:.6f} PB")
