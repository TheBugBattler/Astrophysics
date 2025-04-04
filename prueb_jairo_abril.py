# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 22:10:21 2025

@author: Pablo D
"""
import numpy as np
import pandas as pd
from astropy.io import fits

# Abrir el catálogo FITS
with fits.open("UNCOVER_DR2_LW_SUPER_catalog.fits") as hdul:
    data = hdul[1].data

# Convertir a DataFrame (corrigiendo endian)
df = pd.DataFrame(np.array(data).byteswap().newbyteorder())

# Extraer columnas necesarias
z_phot = df.iloc[:, 82]
z025 = df.iloc[:, 84]
z975 = df.iloc[:, 88]
flag_star = df.iloc[:, 69]
a = df.iloc[:, 62]
b = df.iloc[:, 63]
f_f125w = df.iloc[:, 28]
f_f140w = df.iloc[:, 31]
ra = df.iloc[:, 3]
dec = df.iloc[:, 4]

# Calcular elipticidad
elipticidad = 1 - (b / a)

# Calcular magnitudes AB
with np.errstate(divide='ignore', invalid='ignore'):
    mag_f125w = -2.5 * np.log10(f_f125w) + 28.9
    mag_f140w = -2.5 * np.log10(f_f140w) + 28.9

# Mostrar cuántos objetos hay en total
print(f"Total de objetos en el catálogo: {len(df)}")

# Aplicar filtros
mascara_final = (
    (z_phot >= 0.7) & (z_phot <= 1.04) &
    (z025 > 0.25) &
    (z975 < 1.4) &
    (flag_star == 0) &
    (elipticidad < 0.5) &
    (mag_f125w < 25)
)

# Mostrar cuántos sobreviven
total_final = mascara_final.sum()
print(f"Total de galaxias candidatas tras aplicar todos los filtros: {total_final}")

# Guardar resultados si hay alguna galaxia candidata
if total_final > 0:
    resultado = pd.DataFrame({
        'ra': ra[mascara_final],
        'dec': dec[mascara_final],
        'z_phot': z_phot[mascara_final],
        'z025': z025[mascara_final],
        'z975': z975[mascara_final],
        'elipticidad': elipticidad[mascara_final],
        'mag_f125w': mag_f125w[mascara_final],
        'mag_f140w': mag_f140w[mascara_final],  # Añadido
    })

    resultado.to_csv("galaxias_campo_filtradas_con_f140w.txt", index=False, sep=' ', float_format='%.6f')
    print("Archivo guardado: galaxias_campo_filtradas_con_f140w.txt")
else:
    print("No se encontraron galaxias que cumplan los criterios.")

