import streamlit as st
from tab_analisis import contenido as analisis_contenido
from tab_calibracion import contenido as calibracion_contenido

st.set_page_config(
    page_title="Sitio para analizar espectros a partir de imágenes",
    page_icon = "assets/icon.png",
    layout="wide"
)

# Encabezado
st.title("Sitio para analizar espectros a partir de imágenes")
st.markdown("---")
st. write("Bienvenido (a)")

#Pestañas
tab1, tab2 = st.tabs(["Análisis de imágenes","Calibración de escala"])

analisis_contenido(tab1)
calibracion_contenido(tab2)
