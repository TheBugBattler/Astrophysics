# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 23:49:21 2024

@author: Pablo D
"""

import pandas as pd

# Cargar el archivo CSV
file_path = 'datos_organizados_definitivos.csv'  # Asegúrate de tener el archivo en el mismo directorio o proporciona la ruta completa
data = pd.read_csv(file_path)

# Eliminar clasificaciones repetidas de "Astrophys", dejando solo una entrada por imagen
data_astrophys = data[data['user_name'] == 'Astrophys'].drop_duplicates(subset='image_name')
data_otros = data[data['user_name'] != 'Astrophys']
data = pd.concat([data_astrophys, data_otros])

# Filtrar las clasificaciones por barra "Sí" para los usuarios "Astrophys" y "jairomendezabreu"
barra_si_astrophys = set(data[(data['user_name'] == 'Astrophys') & (data['Does it have a bar?'] == 'Yes')]['image_name'])
barra_si_jairo = set(data[(data['user_name'] == 'jairomendezabreu') & (data['Does it have a bar?'] == 'Yes')]['image_name'])

# Obtener la lista de imágenes que coinciden en barras seguras para ambos usuarios
barra_seguro_coincidente = barra_si_astrophys & barra_si_jairo



# Filtrar las clasificaciones por "Disco" para los usuarios "Astrophys" y "jairomendezabreu"
disco_astrophys = set(data[(data['user_name'] == 'Astrophys') & (data['Eliptical, disk or irregular?'].str.strip() == 'Disk')]['image_name'])
disco_jairo = set(data[(data['user_name'] == 'jairomendezabreu') & (data['Eliptical, disk or irregular?'].str.strip() == 'Disk')]['image_name'])

# Obtener la lista de imágenes que coinciden en discos seguros para ambos usuarios
disco_seguro_coincidente = disco_astrophys & disco_jairo



# Filtrar las clasificaciones por barra "Uncertain" para los usuarios "Astrophys" y "jairomendezabreu"
barra_uncertain_astrophys = set(data[(data['user_name'] == 'Astrophys') & (data['Does it have a bar?'] == 'Uncertain')]['image_name'])
barra_uncertain_jairo = set(data[(data['user_name'] == 'jairomendezabreu') & (data['Does it have a bar?'] == 'Uncertain')]['image_name'])

# Combinar las listas de inciertos
barra_incierta = barra_uncertain_astrophys | barra_uncertain_jairo



# Filtrar las clasificaciones que no son "Disco" para los usuarios "Astrophys" y "jairomendezabreu"
no_disco_astrophys = set(data[(data['user_name'] == 'Astrophys') & (data['Eliptical, disk or irregular?'].str.strip() != 'Disk')]['image_name'])
no_disco_jairo = set(data[(data['user_name'] == 'jairomendezabreu') & (data['Eliptical, disk or irregular?'].str.strip() != 'Disk')]['image_name'])

# Obtener la lista de imágenes que son inciertas en discos (uno dice disco y el otro no)
disco_incierto = (disco_astrophys & no_disco_jairo) | (disco_jairo & no_disco_astrophys)
