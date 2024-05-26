# -*- coding: utf-8 -*-
"""
Created on Sun May 26 12:50:44 2024

@author: pablo
"""

import numpy as np
import pandas as pd
from astropy.io import fits

# Leemos el archivo FITS
hdul = fits.open('UNCOVER_DR2_LW_SUPER_catalog.fits')
data = hdul[1].data
hdul.close()

# Convierte los datos FITS en un DataFrame de pandas
df = pd.DataFrame(data)

f606w = df.iloc[:, 13]
f814w = df.iloc[:, 16]
usephot = df.iloc[:, 66]

# Pasamos a magnitudes
mf814w = -2.5 * np.log10(f814w) + 28.9
mf606w = -2.5 * np.log10(f606w) + 28.9

# Cálculo de las magnitudes absolutas
distancia_pc = 1262893867.37  # Con datos de Placnk
mag_absoluta_814 = mf814w - 5 * np.log10(distancia_pc) + 5
mag_absoluta_606 = mf606w - 5 * np.log10(distancia_pc) + 5

# Ascension recta y declinacion
ar = df.iloc[:, 3]
dec = df.iloc[:, 4]
ar = tuple(round(valor, 6) for valor in ar)
dec = tuple(round(valor, 6) for valor in dec)

datos = list(zip(ar, dec, mag_absoluta_814, mag_absoluta_606))

def leer_lista_desde_archivo(archivo):
    lista = []
    with open(archivo, 'r') as file:
        for line in file:
            ar, dec = line.strip().split()
            lista.append((float(ar), float(dec)))
    return lista

def comparar_listas(lista_existente, lista_nueva):
    coincidencias = []
    for ar1, dec1, mag1_814, mag1_606 in lista_existente:
        for ar2, dec2 in lista_nueva:
            if ar1 == ar2 and dec1 == dec2:
                coincidencias.append((ar1, dec1, mag1_814, mag1_606))
                break
    return coincidencias

def guardar_coincidencias(resultados, archivo_salida):
    with open(archivo_salida, 'w') as file:
        for ar, dec, mag_814, mag_606 in resultados:
            file.write(f"{ar} {dec} {mag_814} {mag_606}\n")

# Leer la lista nueva desde un archivo de texto
archivo_lista_nueva = 'C:/Users/pablo/OneDrive/Escritorio/Apuntes/TFG2/ar,dec,barras.txt'
lista_nueva = leer_lista_desde_archivo(archivo_lista_nueva)

# Comparar las dos listas
resultados = comparar_listas(datos, lista_nueva)

# Imprimir y guardar los resultados
if resultados:
    print("Las siguientes coincidencias se encontraron:")
    for ar, dec, mag_814, mag_606 in resultados:
        print(f"AR: {ar}, DEC: {dec}, Magnitud 814: {mag_814}, Magnitud 606: {mag_606}")
    archivo_resultados = 'magnitudes_absolutas_confirmadas_barras_606_814.txt'
    guardar_coincidencias(resultados, archivo_resultados)
    print(f"Las coincidencias han sido guardadas en {archivo_resultados}.")
else:
    print("No se encontraron coincidencias.")
