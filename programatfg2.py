# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 13:32:29 2024

@author: pablo
"""
from numpy import*
import pandas as pd
from pylab import*
from astropy.io import fits


# Leemos el archivo FITS
hdul = fits.open('UNCOVER_DR2_LW_SUPER_catalog.fits')
data = hdul[1].data
hdul.close()

# Convierte los datos FITS en un DataFrame de pandas
df = pd.DataFrame(data)

f606w=df.iloc[:, 13]
f814w=df.iloc[:, 16]
usephot=df.iloc[:, 66]

#Pasamos a magnitudes
mf606w=-2.5*log10(f606w)+28.9
mf814w=-2.5*log10(f814w)+28.9
#Calculamos color
color606814=mf606w-mf814w

#Ascension recta y declinacion
ar=df.iloc[:,3]
dec=df.iloc[:,4]
ar = tuple(round(valor, 6) for valor in ar)
dec = tuple(round(valor, 6) for valor in dec)


#Vamos a obtener las que no son estrellas
estelaricidad=df.iloc[:, 69]

artefactos=df.iloc[:, 70]

zespectro=df.iloc[:, 72]

zphot=df.iloc[:,82]

#Los que no son ni estrellas ni artefactos

datos=list(zip(ar,dec,mf606w,mf814w,usephot))
datosconzphot=list(zip(ar,dec,zphot)) #Datos con z fotometrico
kron=df.iloc[: ,56]

coordenadasconrkron=list(zip(ar,dec,kron))


#Vamos a quedarnos con los que tienen z<1

datosconzphotbien = [fila for fila in datosconzphot if fila[2] < 1] #Solo los que tienen zphot<1


datos = [fila for fila in datos if fila[4] == 1]
#Vamos a obtener estos valores para los objetos que no son estrellas ni artefactos
arbien=[fila[0] for fila in datos]
decbien=[fila[1] for fila in datos]
mf606wbien=[fila[2] for fila in datos]
mf814wbien=[fila[3] for fila in datos]

datosbien=list(zip(arbien,decbien,mf606wbien,mf814wbien))

#Obtenemos color hay que restar asi porque son listas
colorbien= [a - b for a, b in zip(mf606wbien, mf814wbien)]

pdatos=plot(mf814wbien,colorbien, "b.")# Todos los datos sin estrellas ni artefactos

a=df.iloc[:,62]
b=df.iloc[:,63]

inclinacion=b/a
datosconinclinacion=list(zip(arbien,decbien,inclinacion))
#Nos quedamos solo con los que b/a >0.5
datosconinclinacionbien = [(fila[0], fila[1], fila[2]) for fila in datosconinclinacion if fila[2] >= 0.5]


#Vamos con los de Bergamini (Espectroscopicamente confirmadas)
id36034=[ 3.592037, -30.405741, 17.30]
id37824=[3.586257, -30.400172, 17.34]
id835=[3.589290, -30.369074, 16.88]
id40689=[3.594796, -30.391654, 17.58]
id736=[3.575038, -30.428344, 17.69]
id938=[3.610666, -30.395618, 17.70]
id814=[3.587469, -30.371246, 17.76]
id947=[3.612408, -30.409245, 17.84]
id34423= [3.579662, -30.409189, 17.84]
id40059=[3.585386, -30.394279, 17.89]
id783=[3.583084, -30.433553, 18.00]
id20227=[3.609542, -30.382110, 18.03]
id39382=[3.587646, -30.396426, 18.07]
id36210=[3.592510, -30.404611, 18.24]
id809=[3.586500, -30.367380, 18.29]
id697=[3.566354, -30.388260, 18.40]
id36527=[3.578511, -30.403375, 18.41] 
id38067=[3.574900, -30.398381, 18.46]
id740=[3.575081, -30.377074, 18.49]
id730=[3.573503, -30.422861, 18.50]
id37947=[3.592998, -30.399330, 18.57]
id834=[3.589103, -30.419803, 18.59]
id894=[3.602057, -30.377689, 18.60]
id41259=[3.593289, -30.384378, 18.60]
id40592=[3.589220, -30.389839, 18.64]
id41644=[3.570173, -30.386449, 18.66]
id37954=[3.586559, -30.399391, 18.70]
id35061=[3.573945, -30.408829, 18.71]
id39428=[3.588152, -30.395075, 18.71]
id41950=[3.589184, -30.387396, 18.72]
id38907=[3.585204, -30.394649, 18.81]
id642=[3.556336, -30.387018, 18.88]
id38117=[3.582159, -30.398571, 18.89]
id39072=[3.598969, -30.397533, 18.90]
id41856=[3.585314, -30.387545, 18.91]
id804=[3.585629, -30.366902, 18.98]
id37344=[3.604341, -30.400124, 18.98]
id41440=[3.605429, -30.384843, 18.99]
id38010=[3.588385, -30.398355, 19.01]
id678=[3.562510, -30.402406, 19.05]
id38930=[3.588680, -30.396077, 19.07]
id40243=[ 3.580953, -30.390808, 19.15]
id32284=[3.602650, -30.416956, 19.16]
id690=[3.565544, -30.387093, 19.16]
id40478=[3.571507, -30.390436, 19.18]
id20018=[3.581566, -30.376517, 19.22]
id902=[3.604284, -30.414554, 19.25]
id966=[3.618050, -30.403670, 19.26]
id42443=[3.594708, -30.389115, 19.26]
id40314=[3.590342, -30.390939, 19.26]
id720=[3.571365, -30.422840, 19.29]
id41363=[3.588146, -30.385006, 19.30]
id692=[3.565347, -30.382948, 19.38]
id768=[3.580711, -30.418875, 19.39]
id956=[3.615142, -30.383729, 19.41]
id38729=[3.578864, -30.397111, 19.42]
id973=[3.618739, -30.392932, 19.42]
id36892=[3.587938, -30.400852, 19.44]
id863=[3.593561, -30.426049, 19.46]
id35339=[3.595907, -30.406213, 19.49]
id950=[3.613184, -30.389698, 19.49]
id20132=[3.595399, -30.380404, 19.50]
id921=[3.607012, -30.403478, 19.51]
id655=[3.559037, -30.410659, 19.51]
id32547=[3.601355, -30.415365, 19.51]
id37068=[3.605266, -30.400808, 19.52]
id888=[3.600962, -30.417843, 19.59]
id41418=[3.592547, -30.385314, 19.62]
id931=[3.609576, -30.378771, 19.62]
id39503=[3.581389, -30.393932, 19.63]
id634=[3.555379, -30.384632, 19.66]
id34556=[3.591721, -30.407807, 19.71]
id816=[3.587541, -30.373945, 19.71]
id961=[3.616679, -30.402709, 19.72]
id41303=[3.583714, -30.384680, 19.75]
id33910=[3.589134, -30.409573, 19.75]
id42149=[3.598764, -30.388018, 19.76]
id33540=[3.588817, -30.410722, 19.77]
id787=[3.583285, -30.432301, 19.78]
id39646=[3.578948, -30.394119, 19.80]
id40884=[3.590278, -30.382698, 19.86]
id37229=[3.594463, -30.400350, 19.89]
id33328=[3.569589, -30.412164, 19.95]
id40270=[3.594239, -30.390462, 19.97]
id42269=[3.595506, -30.388688, 19.97]
id13996=[3.573450, -30.377932, 20.00]
id39710=[3.584986, -30.392877, 20.01]
id35693=[3.587039, -30.404948, 20.04]
id40551=[3.589520, -30.389499, 20.08]
id21367=[3.597859, -30.405556, 20.12]
id40832=[3.588038, -30.382557, 20.17]
id39876=[3.580373, -30.392204, 20.21]
id33699=[3.582507, -30.409986, 20.24]
id38275=[3.585521, -30.397156, 20.24]
id41655=[3.573735, -30.385976, 20.26]
id41651=[3.573383, -30.386313, 20.34]
id37230=[3.583991, -30.399260, 20.34]
id40802=[3.570861, -30.382004, 20.37]
id36220=[3.605275, -30.402932, 20.39]
id39283=[3.600830, -30.394896, 20.39]
id713=[3.569303, -30.384236, 20.42]
id20089=[3.597633, -30.379200, 20.51]
id32768=[3.585709, -30.413971, 20.59]
id42195=[3.578348, -30.387100, 20.61]
id13311=[3.560070, -30.389342, 20.61] 
id33870=[3.595124, -30.409366, 20.63]
id35908=[3.585035, -30.403315, 20.63]
id37609=[3.578591, -30.399109, 20.68]
id36043=[3.584377, -30.402887, 20.83]
id41908=[3.604401, -30.384960, 20.84]
id34439=[3.590280, -30.407401, 20.92] 
id40032=[3.593885, -30.390837, 20.96] 
id36339=[3.588145, -30.401980, 20.97] 
id32088=[3.603422, -30.416769, 20.99] 
id38143=[3.602200, -30.396988, 21.01] 
id44545=[3.578469, -30.381318, 21.04] 
id36953=[3.572810, -30.400534, 21.05] 
id37825=[3.602715, -30.397571, 21.08] 
id40428=[3.578347, -30.389464, 21.12] 
id20064=[3.577544, -30.378870, 21.26] 
id36298=[3.594832, -30.402130, 21.30] 
id35576=[3.587971, -30.404253, 21.31] 
id40239=[3.593166, -30.390349, 21.33]
id40239=[3.593166, -30.390349, 21.33]
id36849=[3.596757, -30.400513, 21.33] 
id34538=[3.573400, -30.407461, 21.46] 
id36843=[3.579074, -30.400089, 21.50] 
id40703=[3.596256, -30.388517, 21.54] 
id33671=[3.583831, -30.409506, 21.56] 
id33410=[3.589721, -30.410222, 21.57]
id40708=[3.571061, -30.388157, 21.61] 
id38252=[3.592874, -30.396356, 21.61] 
id37214=[3.585389, -30.399007, 21.67]
id36163=[3.588499, -30.402102, 21.70] 
id39727=[3.584373, -30.391755, 21.75] 
id41636=[3.573693, -30.385685, 21.79] 
id37542=[3.584458, -30.398342, 22.02] 
id38175=[3.583312, -30.396542, 22.05]
id35190=[3.601244, -30.404885, 22.11] 
id38267=[3.597298, -30.396046, 22.15] 
id33803=[3.593740, -30.409224, 22.18]
id37367=[3.601857, -30.398661, 22.22] 
id42079=[3.593478, -30.387595, 22.24] 
id8024000=[3.567362, -30.400881, 22.30] 
id34705=[3.594676, -30.405899, 22.31] 
id41265=[3.578737, -30.384233, 22.33] 
id37199=[3.603831, -30.399122, 22.37]
id41937=[3.573015, -30.387260, 22.43] 
id35514=[3.574778, -30.403672, 22.43] 
id32680=[3.592097, -30.413109, 22.45] 
id36814=[3.593414, -30.400024, 22.49] 
id36982=[3.582898, -30.399701, 22.49]
id40944=[3.593025, -30.382970, 22.50] 
id37231=[3.581618, -30.399105, 22.51] 
id10440000=[3.569048, -30.394963, 22.56] 
id33503=[3.597475, -30.409964, 22.56] 
id10657000=[3.569981, -30.394634, 22.61] 
id41388=[3.598749, -30.384458, 22.61]
id36872=[3.595752, -30.399971, 22.62]
id34828=[3.592717, -30.406107, 22.65]
id38459=[3.572068, -30.395969, 22.66]
id39956=[3.584993, -30.390870, 22.67]
id33933=[3.585939, -30.408434, 22.71]
id41467=[3.586832, -30.384627, 22.74]
id41842=[3.591221, -30.386717, 22.76]
id38253=[3.584471, -30.396056, 22.78]
id41531=[3.589828, -30.385639, 22.85]
id4206000=[3.600810, -30.409530, 22.87] 
id36346=[3.588851, -30.401771, 22.89] 
id41930=[3.608089, -30.387068, 22.90]
id33753=[3.567161, -30.408755, 22.92] 
id33911=[3.577555, -30.408196, 22.94] 
id39609=[3.605171, -30.392616, 22.98]
id35436=[3.589433, -30.404231, 23.10] 
id4136000=[3.590889, -30.410893, 23.11] 
id41419=[3.577521, -30.384813, 23.12 ]
id3476000=[3.585092, -30.412314, 23.13] 
id32671=[3.588878, -30.413346, 23.14] 
id35134=[3.598182, -30.404825, 23.15] 
id38748=[3.579869, -30.394391, 23.15] 
id12269000=[3.577314, -30.390297, 23.21]
id12325000=[3.605930, -30.390167, 23.24] 
id38900=[3.579626, -30.394091, 23.26]
id42040=[3.573600, -30.387182, 23.27] 
id10930000=[3.572670, -30.393633, 23.28] 
id35978=[3.596444, -30.403275, 23.28] 
id11577000=[3.590109, -30.391576, 23.31] 
id36776=[3.584729, -30.399826, 23.33] 
id3547000=[3.566721, -30.411992, 23.36] 
id33468=[3.595517, -30.409682, 23.42] 
id12191000=[3.581882, -30.390474, 23.44]
id37304=[3.583931, -30.398595, 23.45] 
id40432=[3.584083, -30.388909, 23.46] 
id34433=[3.588518, -30.406316, 23.47] 
id5079000=[3.586480, -30.407004, 23.54] 
id3795000=[3.592497, -30.412103, 23.55] 
id10265000=[3.597219, -30.395534, 23.56]
id12018000=[3.605043, -30.391671, 23.64]
id8216000=[3.597727, -30.400602, 23.69] 
id4938000=[3.582862, -30.408838, 23.70] 
id35340=[3.588510, -30.404209, 23.73] 
id7420000=[3.568412, -30.402023, 23.80] 
id8330000=[3.569485, -30.399955, 23.83] 


listabergamini=[id36034, id37824, id835, id40689, id736, id938, id814, id947, id34423, id40059, id783, id20227, id39382, id36210, id809, id697, id36527, id38067, id740, id730, id37947, id834, id894, id41259, id40592, id41644, id37954, id35061, id39428, id41950, id38907, id642, id38117, id39072, id41856, id804, id37344, id41440, id38010, id678, id38930, id40243, id32284, id690, id40478, id20018, id902, id966, id42443, id40314, id720, id41363, id692, id768, id956, id38729, id973, id36892, id863, id35339, id950, id20132, id921, id655, id32547, id37068, id888, id41418, id931, id39503, id634, id34556, id816, id961, id41303, id33910, id42149, id33540, id787, id39646, id40884, id37229, id33328, id40270, id42269, id13996, id39710, id35693, id40551, id21367, id40832, id39876, id33699, id38275, id41655, id41651, id37230, id40802, id36220, id39283, id713, id20089, id32768, id42195, id13311, id33870, id35908, id37609, id36043, id41908, id34439, id40032, id36339, id32088, id38143, id44545, id36953, id37825, id40428, id20064, id36298, id35576, id40239, id36849, id34538, id36843, id40703, id33671, id33410, id40708, id38252, id37214, id36163, id39727, id41636, id37542, id38175, id35190, id38267, id33803, id37367, id42079, id8024000, id34705, id41265, id37199, id41937, id35514, id32680, id36814, id36982, id40944, id37231, id10440000, id33503, id10657000, id41388, id36872, id34828, id38459, id39956, id33933, id41467, id41842, id38253, id41531, id4206000, id36346, id41930, id33753, id33911, id39609, id35436, id4136000, id41419, id3476000, id32671, id35134, id38748, id12269000, id12325000, id38900, id42040, id10930000, id35978, id11577000, id36776, id3547000, id33468, id12191000, id37304, id40432, id34433, id5079000, id3795000, id10265000, id12018000, id8216000, id4938000, id35340, id7420000, id8330000]

listabergaminiar = [sublista[0] for sublista in listabergamini] #Valor AR de Bergamini
listabergaminidc = [sublista[1] for sublista in listabergamini] #Valor DEC de Bergamini
coordenadasbergamini=list(zip(listabergaminiar, listabergaminidc))
ardc = tuple(zip(arbien,decbien)) #Nos quedamos solo con la AR y DEC de las galaxias

ardc = [(round(value1, 7), round(value2, 7)) for (value1, value2) in ardc] #Nos quedamos solo con 7 decimales



def find_matching_pairs_in_tuples(ardc, coordenadasbergamini, tolerance=0.0001, max_pairs=202):
    matching_pairs = []

    for value1, value2 in ardc:
        for value3, value4 in coordenadasbergamini:
            if (abs(value1 - value3) <= tolerance and abs(value2 - value4) <= tolerance) or \
               (abs(value1 - value4) <= tolerance and abs(value2 - value3) <= tolerance):
                matching_pairs.append(((value1, value2), (value3, value4)))

    # Ordenar la lista de coincidencias por la suma de las diferencias absolutas
    matching_pairs.sort(key=lambda pair: abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1]))

    # Devolver las primeras max_pairs tuplas
    return matching_pairs[:max_pairs]

# Encontrar pares coincidentes con una tolerancia de ±0.0001 y un máximo de 202 tuplas
matching_pairs = find_matching_pairs_in_tuples(ardc, coordenadasbergamini, tolerance=0.0001, max_pairs=202)
print(len(matching_pairs))



# Crea una nueva tupla con solo los valores de la primera componente 
nueva_tupla = tuple(item[0] for item in matching_pairs)

#Comparamos los valores de los que coinciden con nuestras coordenadas

def compare_tuples(nueva_tupla, ardc):
    common_pairs = set(nueva_tupla) & set(ardc)
    
    if common_pairs:
        #print("Common pairs:")
        #print(common_pairs)
        return tuple(common_pairs)
    else:
        #print("No common pairs found.")
        return ()



# Llamada a la función y asignación del resultado a la variable 'tupladefinitiva'
tupladefinitiva = compare_tuples(nueva_tupla, ardc) 


coordenadasymagnitudes2=list(zip(ar, dec, mf814w)) 


#Comparamos con la tupla de coordenadas y magnitudes y nos quedamos con las magnitudes para representarlas
def compare_and_save(tupladefinitiva, coordenadasymagnitudes2):
    terceras_componentes = []

    for par in tupladefinitiva:
        # Comprobamos si el primer y segundo elemento del par coinciden con algún trío
        for trio in coordenadasymagnitudes2:
            if par[0] == trio[0] and par[1] == trio[1]:
                terceras_componentes.append(trio[2])
                break  # Rompemos el bucle interno si encontramos una coincidencia

    return terceras_componentes

# Llamada a la función para comparar y guardar terceras componentes
magnitudescoinci = compare_and_save(tupladefinitiva, coordenadasymagnitudes2)

bcg=min(magnitudescoinci) #Galaxia mas brillante

#Necesitamos tambien tener el valor de mf606 de las galaxias de Bergamini, comparamos
coordenadasymagnitud606=list(zip(ar, dec, mf606w))

def compare_and_save2(tupladefinitiva, coordenadasymagnitud606):
    terceras_componentes = []

    for par in tupladefinitiva:
        # Comprobamos si el primer y segundo elemento del par coinciden con algún trío
        for trio in coordenadasymagnitud606:
            if par[0] == trio[0] and par[1] == trio[1]:
                terceras_componentes.append(trio[2])
                break  # Rompemos el bucle interno si encontramos una coincidencia

    return terceras_componentes


# Llamada a la función para comparar y guardar terceras componentes
magnitudescoinci606 = compare_and_save2(tupladefinitiva, coordenadasymagnitud606) #Obtenemos las magnitudes en 606 de los coincidentes

#Restamos magnitudes para obtener color, hay que hacerlo asi porque son listas 

def subtract_lists(magnitudescoinci606, magnitudescoinci):
    result = [x - y for x, y in zip(magnitudescoinci606, magnitudescoinci)]
    return result
color606814confirmadas = subtract_lists(magnitudescoinci606,magnitudescoinci ) #tenemos el color
#Quitamos valor dispratado por comparacion de AR y DEC
magnitudescoinci= tuple(valor for valor in magnitudescoinci if valor < 25)
color606814confirmadas=tuple(valor for valor in color606814confirmadas if valor > 0)


p2=plot(magnitudescoinci, color606814confirmadas, "r.") #Representamos las espectroscopicamente confirmadas
plt.axvline(x=24.5957, color='black', alpha=0.7, linestyle='--') # segunda raya vertical
plt.axvline(x=bcg, color='black', alpha=0.7, linestyle='--') # segunda raya vertical
plt.axhline(0.48491, color='black', alpha=0.7, linestyle="--") #Estrella joven
plt.axhline(1.0939, color='black', alpha=0.7, linestyle="--") #Estrella vieja

xlabel("Magnitud F814W")
ylabel("Color F606W-F814W")


magnitudesycolordentro = []
dentro=tuple(zip(ar,dec,mf814w,color606814)) #Definimos tupla con todos los datos ar, dec, magnitud y color, veamos cuales estan dentro
valores_cumplen_condiciones = []
for fila in dentro:
    valor_tercera_columna = fila[2]  # Índice 2 para la tercera columna
    valor_cuarta_columna = fila[3]   # Índice 3 para la cuarta columna

    # Verificar ambas condiciones
    if (
        bcg <= valor_tercera_columna <=24.5957
        and 0.48491 <= valor_cuarta_columna <= 1.0939
    
     ):
        magnitudesycolordentro.append((fila[0], fila[1], fila[2], fila[3]))  # Guardar la tupla completa

print(len(magnitudesycolordentro)) #Galaxias dentro numero
# Imprimir los valores que cumplen ambas condiciones

#Aqui tenemos los valores que cumplen zphot<1
dentrosinzphot= [fila_1 for fila_1 in magnitudesycolordentro  for fila_2 in datosconzphotbien if fila_1[:2] == fila_2[:2]]

#Ahora vamois a quedarnos con los que tienen buena inclinacion
datosdentroconbuenainclinacion=[(fila_4[0], fila_4[1], fila_4[2], fila_4[3],) for fila_4 in dentrosinzphot for fila_3 in datosconinclinacionbien if (fila_4[0], fila_4[1]) == (fila_3[0], fila_3[1])]

print(len(datosdentroconbuenainclinacion)) #Datos buenos definitivos

#Vamos a obtener los datos de rkron
def comparar_tuplas12(coordenadasconkron, datosdentroconbuenainclinacion):
    # Obtener las dos primeras columnas de cada tupla
    columnas_tupla1 = set((fila[0], fila[1]) for fila in coordenadasconkron)
    columnas_tupla2 = set((fila[0], fila[1]) for fila in datosdentroconbuenainclinacion)

    # Encontrar datos coincidentes
    coincidentes2 = columnas_tupla1.intersection(columnas_tupla2)

    # Filtrar datos coincidentes de las tuplas originales
    resultado_tupla1 = [fila for fila in coordenadasconkron if (fila[0], fila[1]) in coincidentes2]
    resultado_tupla2 = [fila for fila in datosdentroconbuenainclinacion if (fila[0], fila[1]) in coincidentes2]

    return resultado_tupla1, resultado_tupla2

resultado_tupla1, resultado_tupla2 = comparar_tuplas12(coordenadasconrkron, datosdentroconbuenainclinacion)
#Esto lo hemos usado para comparar y quedarnos con los datos de kron