from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def convertir_8bit(imagen):
    """ Convierte una imagen a excala de grises 8-bit"""
    # imagen PIL
    gris = np.array(imagen.convert('L'))

    # normalizacion de rango (0-255) de ser necesario
    if gris.max() > 255:
        gris = (gris / gris.max() * 255).astype(np.uint8)
    else:
        gris = gris.astype(np.uint8)
    
    return gris

def extraer_perfil_intensidad(imagen_8bit, bins_verticales=50):
    """
    Extrae intensidad vs posición horixontal con binning vertical
    Devuelve: posiciones_x (en pixeles), valores_intensidad
    """
    altura, ancho = imagen_8bit.shape

    altura_bin = altura // bins_verticales
    imagen_binned = np.zeros((bins_verticales, ancho))

    for i in range(bins_verticales):
        fila_inicial = i * altura_bin
        fila_final = fila_inicial + altura_bin if i < bins_verticales - 1 else altura
        imagen_binned[i, :] = np.mean(imagen_8bit[fila_inicial:fila_final, :], axis=0)
    
    valores_intensidad = np.mean(imagen_binned, axis=0)
    posiciones_x = np.arange(ancho)

    return posiciones_x, valores_intensidad

def graficar_perfil_de_intensidad(posiciones_x,valores_intensidad, titulo="Intensidad de pixel vs posición horizontal"):
    """Genera un gráfico de matplotlib de intensidad vs posición"""
    fig,ax = plt.subplots(figsize=(12,6))
    ax.plot(posiciones_x, valores_intensidad, 'b-', linewidth=2)

    ax.set_xlabel("Posición horizontal (pixeles)", fontsize=12)
    ax.set_ylabel("Intensidad", fontsize=12)
    ax.set_title(titulo, fontsize=14)
    ax.set_xlim(0, len(posiciones_x))
    ax.set_ylim(0,255)
    # feature opcional, por consultar retroalimentación del usuario final
    ax.grid(True, alpha=0.3)

    return fig
