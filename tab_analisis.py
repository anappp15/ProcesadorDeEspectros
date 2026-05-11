import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from procesos import convertir_8bit, extraer_perfil_intensidad, graficar_perfil_de_intensidad

# Titulo de la pestaña
tab_tit = "Análisis de imágenes"

def contenido(tab):
    with tab:
        st.header("Suba un espectro para generar un perfil de intensidad")
        col1, col2 = st.columns([1,1])
        with col1:
            st.subheader("Carga de imagen")
            archivo_recibido = st.file_uploader(
                "Seleccione un archivo",
                type= ['png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif'],
                help= "Suba una archivo con información espectroscópica en cualquier formato estándar de imágen"
            )
            # Procesado de la imagen
            if archivo_recibido is not None:
                # conversion a 8 bits
                imagen_recibida = Image.open(archivo_recibido)
                imagen_convertida = convertir_8bit(imagen_recibida)
                st.session_state.current_image = imagen_convertida
                # info de la imagen
                st.subheader("Imagen procesada en 8-bit")
                st.image(imagen_convertida, caption="Imagen en escala de grises 8-bit", use_container_width=True)
                st.info(f"Dimensiones de la imagen: {imagen_convertida.shape[1]} x {imagen_convertida.shape[0]} pixeles")
                with col2:
                    # configuración del binning
                    st.subheader("Ajustes del perfil de intenisdad")
                    num_bins = st.slider(
                        "Cantidad de bins verticales",
                        min_value=10,
                        max_value=200,
                        value=50
                    )
                    # construcción del perfil de intensidad
                    if st.button("Extraer perfil de intensidad", type= "primary"):
                        posiciones, intensidad = extraer_perfil_intensidad(imagen_convertida, num_bins)
                        st.session_state.posiciones = posiciones
                        st.session_state.intensidad = intensidad
                        # grafica
                        st.subheader("Perfil de intensidad")
                        fig = graficar_perfil_de_intensidad(posiciones,intensidad)
                        st.pyplot(fig)
                        plt.close(fig)
                        # Extra: informacion de picos (máximos)
                        peak_intensidad = np.max(intensidad)
                        peak_posicion = posiciones[np.argmax(intensidad)]
                        st.success(f"Máximo en {peak_posicion:.0f} px con intensidad {peak_intensidad:.1f}")
