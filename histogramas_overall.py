# -*- coding: utf-8 -*-
"""
Created on Sun May 12 20:26:01 2024

@author: pablo
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos desde los archivos
datos_seguras = pd.read_csv('magnitudes_absolutas_confirmadas_barras.txt', header=None, delim_whitespace=True, names=['ra', 'dec', 'mag_abs'])
datos_todas = pd.read_csv('magnitudes_absolutas_datos_todas.txt', header=None, delim_whitespace=True, names=['ra', 'dec', 'mag_abs'])
datos_dudosas_jairo = pd.read_csv('magnitudes_absolutas_uncertain_jairo.txt', header=None, delim_whitespace=True, names=['ra', 'dec', 'mag_abs'])
datos_dudosas_pablo = pd.read_csv('magnitudes_absolutas_uncertain_pablo.txt', header=None, delim_whitespace=True, names=['ra', 'dec', 'mag_abs'])

# Unir los datos de barras seguras y dudosas para identificarlas
datos_seguras['tipo'] = 'segura'
datos_dudosas_jairo['tipo'] = 'dudosa_jairo'
datos_dudosas_pablo['tipo'] = 'dudosa_pablo'

# Combinar todos los datos de clasificaciones en un único DataFrame
datos_clasificaciones = pd.concat([datos_seguras, datos_dudosas_jairo, datos_dudosas_pablo])

# Fusionar con el DataFrame de todas las galaxias para etiquetar las galaxias
datos_fusionados = datos_todas.merge(datos_clasificaciones, on=['ra', 'dec', 'mag_abs'], how='left')

# Rellenar galaxias no clasificadas como 'no_barra'
datos_fusionados['tipo'] = datos_fusionados['tipo'].fillna('no_barra')

# Definir bins de magnitud absoluta con un paso de 0.25
bins_finos = np.arange(-23, -15, 0.5)
labels_finos = [f"{b+0.25:.2f} to {b:.2f}" for b in bins_finos[:-1]]  # Ajustar para que coincida con la cantidad correcta de bins

# Agrupar por los nuevos bins de magnitud absoluta
datos_fusionados['mag_bin_fino'] = pd.cut(datos_fusionados['mag_abs'], bins=bins_finos, labels=labels_finos, right=False)

# Contar el número total de galaxias y número de barras por bin
resumen_bins_finos = datos_fusionados.groupby('mag_bin_fino').agg(
    total_galaxias=('tipo', 'size'),
    barras_seguras=('tipo', lambda x: (x == 'segura').sum()),
    barras_dudosas=('tipo', lambda x: ((x == 'dudosa_jairo') | (x == 'dudosa_pablo')).sum())
)

# Calcular la fracción de barras seguras y superior por bin
resumen_bins_finos['fraccion_segura'] = resumen_bins_finos['barras_seguras'] / resumen_bins_finos['total_galaxias']
resumen_bins_finos['fraccion_superior'] = (resumen_bins_finos['barras_seguras'] + resumen_bins_finos['barras_dudosas']) / resumen_bins_finos['total_galaxias']

# Crear el gráfico de barras
plt.figure(figsize=(14, 8))
plt.bar(resumen_bins_finos.index, resumen_bins_finos['fraccion_superior'] - resumen_bins_finos['fraccion_segura'], bottom=resumen_bins_finos['fraccion_segura'], color='red', label='Fracción de Barras', width=0.05)

# Anotaciones con el número total de galaxias
for idx, row in resumen_bins_finos.iterrows():
    plt.text(idx, row['fraccion_superior'] + 0.02, f"n={row['total_galaxias']}", ha='center', va='bottom', color='black')

plt.xlabel('Magnitud Absoluta $M_r$ [mag]')
plt.ylabel('Fracción de Barras')
plt.gca().invert_xaxis()
plt.xticks(np.arange(len(labels_finos)), labels_finos, rotation=90)
plt.legend()
plt.tight_layout()
plt.show()

